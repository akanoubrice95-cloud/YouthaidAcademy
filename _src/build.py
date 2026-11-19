#!/usr/bin/env python3
"""Génère le site Youthaid Academy (français à la racine, anglais dans /en/).

Utilisation :  python3 _src/build.py
Les pages sont décrites dans _src/content.py ; ce script produit les fichiers .html,
l'index de recherche, le sitemap et robots.txt.
"""
import html
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import (OFFICES, ORG_EMAIL, ORG_PHONE, SITE_URL, SOCIALS, brand, icon,  # noqa: E402
                 office_line, phone_href, social_links, tr)
import content  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
VERSION = time.strftime("%Y%m%d%H%M")
PAGES = {p["slug"]: p for p in content.PAGES}


def href(slug):
    return "./" if slug == "index" else f"{slug}.html"


def title_of(slug, t):
    return PAGES[slug]["nav"](t) if "nav" in PAGES[slug] else PAGES[slug]["title"](t)


def nav_html(t, current):
    def link(slug):
        cur = ' aria-current="page"' if slug == current else ""
        return f'<li><a href="{href(slug)}"{cur}>{title_of(slug, t)}</a></li>'

    def group(label, slugs):
        return (f'<li class="has-sub"><button class="nav-parent" type="button" aria-expanded="false">{label}</button>'
                f'<ul class="sub">{"".join(link(s) for s in slugs)}</ul></li>')

    return ('<nav class="main-nav" id="main-nav" aria-label="' + t("Menu principal", "Main menu") + '"><ul>'
            + group(t("Qui sommes-nous", "About us"), ["a-propos", "mission", "impact", "partenaires"])
            + group(t("Nos actions", "What we do"), ["programmes", "mentorat", "formations", "opportunites", "evenements"])
            + group(t("S’engager", "Get involved"), ["adherer", "devenir-mentor", "devenir-benevole", "don"])
            + link("actualites") + link("contact")
            + f'<li class="mobile-only"><a href="{href("don")}">{title_of("don", t)}</a></li>'
            + f'<li class="mobile-only"><a href="{href("espace-membre")}">{title_of("espace-membre", t)}</a></li>'
            + "</ul></nav>")


def footer_html(t):
    def col(label, slugs):
        return f'<div><h4>{label}</h4><ul>' + "".join(
            f'<li><a href="{href(s)}">{title_of(s, t)}</a></li>' for s in slugs) + "</ul></div>"

    phone = (f'<li>{icon("chat", 18)}<a href="{phone_href(ORG_PHONE)}">{ORG_PHONE}</a></li>' if ORG_PHONE else "")
    offices = "".join(f'<li>{icon("globe", 18)}<span>{office_line(o, t)}</span></li>' for o in OFFICES)
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        {brand("./", dark=True)}
        <p>{t("Agir pour l’égalité des chances : accompagner les jeunes vers la réussite scolaire, professionnelle et entrepreneuriale.",
              "Acting for equal opportunities: supporting young people towards academic, professional and entrepreneurial success.")}</p>
        <ul class="footer-contact">
          <li>{icon("mail", 18)}<a href="mailto:{ORG_EMAIL}">{ORG_EMAIL}</a></li>
          {phone}
          {offices}
        </ul>
        {social_links(t, "socials socials-dark")}
      </div>
      {col(t("Découvrir", "Discover"), ["a-propos", "mission", "impact", "partenaires", "actualites"])}
      {col(t("Nos actions", "What we do"), ["programmes", "mentorat", "formations", "opportunites", "evenements"])}
      {col(t("S’engager", "Get involved"), ["adherer", "devenir-mentor", "devenir-benevole", "don", "espace-membre"])}
      {col(t("Aide", "Help"), ["faq", "contact", "mentions-legales", "confidentialite", "cgu", "cookies"])}
    </div>
    <div class="footer-bottom">
      <span>© <span class="year"></span> Youthaid Academy. {t("Tous droits réservés.", "All rights reserved.")}</span>
      <span>youthaidacademy.org</span>
    </div>
  </div>
</footer>"""


def org_jsonld(lang):
    t = tr(lang)
    data = {
        "@context": "https://schema.org",
        "@type": "NGO",
        "name": "Youthaid Academy",
        "url": SITE_URL + "/",
        "logo": f"{SITE_URL}/assets/img/logo.png",
        "description": t("Fondation pour l’égalité des chances : mentorat, formations et opportunités pour les jeunes issus de milieux défavorisés.",
                         "Foundation for equal opportunities: mentoring, training and opportunities for young people from disadvantaged backgrounds."),
        "email": ORG_EMAIL,
        "address": [{"@type": "PostalAddress", "addressLocality": o["city"], "addressRegion": o["region"],
                     "addressCountry": o["cc"]} for o in OFFICES],
        "areaServed": ["CI", "FR"],
        "founder": {"@type": "Person", "name": "Brice Akanou"},
        "sameAs": [url for _, url, _ in SOCIALS],
    }
    if ORG_PHONE:
        data["telephone"] = ORG_PHONE
        data["contactPoint"] = {"@type": "ContactPoint", "contactType": "customer support", "email": ORG_EMAIL,
                                "telephone": ORG_PHONE, "availableLanguage": ["French", "English"]}
    else:
        data["contactPoint"] = {"@type": "ContactPoint", "contactType": "customer support", "email": ORG_EMAIL,
                                "availableLanguage": ["French", "English"]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def layout(lang, slug, body):
    t = tr(lang)
    page = PAGES[slug]
    base = "" if lang == "fr" else "../"
    title = page["title"](t)
    full_title = "Youthaid Academy" if slug == "index" else f"{title} — Youthaid Academy"
    if slug == "index":
        full_title = t("Youthaid Academy — Égalité des chances pour les jeunes",
                       "Youthaid Academy — Equal opportunities for young people")
    desc = html.escape(page["desc"](t), quote=True)
    path = "" if slug == "index" else f"{slug}.html"
    url_fr = f"{SITE_URL}/{path}"
    url_en = f"{SITE_URL}/en/{path}"
    canonical = url_fr if lang == "fr" else url_en
    other = (f"en/{href(slug)}" if lang == "fr" else f"../{href(slug)}")
    other_label = "EN" if lang == "fr" else "FR"
    other_name = "English" if lang == "fr" else "Français"
    return f"""<!doctype html>
<html lang="{lang}" data-base="{base}" data-v="{VERSION}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{html.escape(full_title)}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="fr" href="{url_fr}">
  <link rel="alternate" hreflang="en" href="{url_en}">
  <link rel="alternate" hreflang="x-default" href="{url_fr}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Youthaid Academy">
  <meta property="og:title" content="{html.escape(full_title)}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="{"fr_FR" if lang == "fr" else "en_GB"}">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" href="{base}assets/img/logo-icone.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">
  <meta property="og:image" content="{SITE_URL}/assets/img/logo.png">
  <link rel="stylesheet" href="{base}assets/css/style.css?v={VERSION}">
  {org_jsonld(lang) if slug in ("index", "contact", "a-propos") else ""}
</head>
<body>
  <a class="skip-link" href="#contenu">{t("Aller au contenu", "Skip to content")}</a>
  <header class="site-header">
    <div class="container header-inner">
      {brand("./")}
      {nav_html(t, slug)}
      <div class="header-tools">
        <div class="search-wrap">
          <button class="icon-btn search-toggle" type="button" aria-label="{t("Rechercher sur le site", "Search the site")}" aria-expanded="false" aria-controls="search-panel">{icon("search", 20)}</button>
          <div class="search-panel" id="search-panel" hidden>
            <form role="search"><input type="search" class="search-input" placeholder="{t("Rechercher sur le site…", "Search the site…")}" aria-label="{t("Rechercher", "Search")}" autocomplete="off"></form>
            <ul class="search-results" aria-live="polite"></ul>
          </div>
        </div>
        <a class="icon-btn lang-switch" href="{other}" hreflang="{"en" if lang == "fr" else "fr"}" lang="{"en" if lang == "fr" else "fr"}" aria-label="{other_name}">{other_label}</a>
        <a class="btn btn-primary btn-sm btn-don" href="{href("don")}">{t("Faire un don", "Donate")}</a>
        <button class="icon-btn menu-toggle" type="button" aria-label="{t("Ouvrir le menu", "Open menu")}" aria-expanded="false" aria-controls="main-nav">{icon("menu", 20)}</button>
      </div>
    </div>
  </header>
  <main id="contenu">
{body}
  </main>
{footer_html(t)}
  <script src="{base}assets/js/main.js?v={VERSION}" defer></script>
</body>
</html>
"""


def page_text(body):
    text = re.sub(r"<(script|style|svg)[^>]*>.*?</\1>", " ", body, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def main():
    written = []
    for lang in ("fr", "en"):
        t = tr(lang)
        outdir = ROOT if lang == "fr" else ROOT / "en"
        outdir.mkdir(exist_ok=True)
        index = []
        for slug, page in PAGES.items():
            body = page["render"](t)
            name = "index.html" if slug == "index" else f"{slug}.html"
            out = layout(lang, slug, body).replace("%BASE%", "" if lang == "fr" else "../")
            if slug == "404":
                # La page 404 peut s'afficher à n'importe quelle adresse : liens absolus.
                out = re.sub(r'(href|src)="(?!https?:|/|#|mailto:)(?:\./)?', r'\1="/', out)
                out = out.replace('data-base=""', 'data-base="/"')
            (outdir / name).write_text(out, encoding="utf-8")
            written.append(str((outdir / name).relative_to(ROOT)))
            if slug != "404":
                index.append({"url": ("" if lang == "fr" else "en/") + href(slug).replace("./", ""),
                              "title": page["title"](t), "text": page_text(body)})
        (ROOT / "assets" / f"search-{lang}.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    # 404 : GitHub Pages utilise /404.html pour toutes les langues ; on retire la copie anglaise.
    (ROOT / "en" / "404.html").unlink(missing_ok=True)

    urls = []
    for slug in PAGES:
        if slug == "404":
            continue
        p = "" if slug == "index" else f"{slug}.html"
        urls += [f"{SITE_URL}/{p}", f"{SITE_URL}/en/{p}"]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print(f"{len(written)} pages générées (version {VERSION})")


if __name__ == "__main__":
    main()
