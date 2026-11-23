"""Briques communes du site : logo, icônes, blocs HTML réutilisables."""
import os
from pathlib import Path

SITE_URL = "https://youthaidacademy.org"

# ---------- Coordonnées officielles de la fondation ----------
ORG_EMAIL = "contact@youthaidacademy.org"
ORG_PHONE = "+33 7 66 16 10 14"
# Compte PayPal qui reçoit les dons, contributions et paiements.
PAYPAL_EMAIL = "akanoubrice95@gmail.com"
PAYPAL_CURRENCY = "EUR"
OFFICES = [
    dict(district="Cocody", city="Abidjan", region="District autonome d’Abidjan",
         country_fr="Côte d’Ivoire", country_en="Côte d’Ivoire", cc="CI"),
    dict(district="", city="Clermont-Ferrand", region="Auvergne-Rhône-Alpes",
         country_fr="France", country_en="France", cc="FR"),
]


def office_line(o, t):
    """« Cocody, Abidjan, Côte d’Ivoire » / « Clermont-Ferrand, France »."""
    return ", ".join(x for x in (o["district"], o["city"], t(o["country_fr"], o["country_en"])) if x)
SOCIALS = [  # (nom, url, tracé SVG 24x24)
    ("LinkedIn", "https://www.linkedin.com/company/youthaidacademy/",
     '<path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.83v1.54h.05c.53-1.01 1.84-2.07 3.79-2.07 4.05 0 4.8 2.67 4.8 6.13V21h-4v-4.98c0-1.19-.02-2.72-1.66-2.72-1.66 0-1.91 1.3-1.91 2.63V21h-4z"/>'),
    ("Facebook", "https://www.facebook.com/p/Youthaid-Academy-100067297629689/",
     '<path fill="currentColor" d="M13.5 21v-7.5h2.53l.38-2.94H13.5V8.69c0-.85.24-1.43 1.46-1.43h1.55V4.63A20.6 20.6 0 0 0 14.24 4.5c-2.24 0-3.78 1.37-3.78 3.89v2.17H7.93v2.94h2.53V21z"/>'),
    ("Instagram", "https://www.instagram.com/youthaid.academy/",
     '<rect x="3.5" y="3.5" width="17" height="17" rx="5" fill="none" stroke="currentColor" stroke-width="1.9"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.9"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor"/>'),
]


def social_links(t, cls="socials"):
    """Pastilles des réseaux sociaux officiels (s'ouvrent dans un nouvel onglet)."""
    items = "".join(
        f'<a href="{url}" target="_blank" rel="noopener noreferrer me" '
        f'aria-label="{name} — Youthaid Academy ({t("nouvel onglet", "new tab")})" title="{name}">'
        f'<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">{svg}</svg></a>'
        for name, url, svg in SOCIALS)
    return f'<div class="{cls}">{items}</div>'


WA_SVG = ('<path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.23 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.17.24-.64.8-.78.97-.14.17-.29.18-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/>')


def whatsapp_href(t):
    """Lien qui ouvre directement la conversation WhatsApp, avec un message de départ."""
    from urllib.parse import quote
    digits = "".join(c for c in ORG_PHONE if c.isdigit())
    msg = t("Bonjour Youthaid Academy, je vous contacte depuis votre site internet.",
            "Hello Youthaid Academy, I’m contacting you from your website.")
    return f"https://wa.me/{digits}?text={quote(msg)}"


def wa_icon(size=20):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true">{WA_SVG}</svg>'


def paypal_href(t):
    """Lien vers la page de don PayPal sécurisée (montant libre, carte bancaire ou compte PayPal)."""
    from urllib.parse import urlencode
    params = {"business": PAYPAL_EMAIL, "currency_code": PAYPAL_CURRENCY,
              "item_name": t("Don à Youthaid Academy", "Donation to Youthaid Academy")}
    return "https://www.paypal.com/donate/?" + urlencode(params)


def paypal_btn(t, label=None):
    """Bouton « Donner avec PayPal » (s'ouvre dans un nouvel onglet)."""
    label = label or t("Donner avec PayPal", "Donate with PayPal")
    return (f'<a class="btn btn-primary" href="{paypal_href(t)}" target="_blank" rel="noopener noreferrer" '
            f'aria-label="{label} ({t("nouvel onglet", "new tab")})">{label}</a>')


def phone_href(num):
    return "tel:" + "".join(c for c in num if c.isdigit() or c == "+")


def _read_contact_email():
    """Adresse de réception des formulaires : variable CONTACT_EMAIL (environnement ou .env)."""
    if os.environ.get("CONTACT_EMAIL"):
        return os.environ["CONTACT_EMAIL"].strip()
    env = Path(__file__).resolve().parent.parent / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("CONTACT_EMAIL="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ORG_EMAIL


CONTACT_EMAIL = _read_contact_email()


def tr(lang):
    """Renvoie une fonction t(fr, en) qui choisit le texte selon la langue."""
    return lambda fr, en: fr if lang == "fr" else en


# Logos officiels (assets/img). %BASE% est remplacé par le chemin vers la racine du site.
# logo.png = logo principal (logo 1) ; logo-blanc.png = version texte blanc pour fonds sombres ;
# logo-icone.svg = le personnage seul (illustrations, icône d'onglet).
LOGO_MARK = '<img class="logo-mark" src="%BASE%assets/img/logo-icone.svg" alt="">'


def brand(home, dark=False):
    src = "logo-blanc.png" if dark else "logo.png"
    return (f'<a class="brand" href="{home}">'
            f'<img src="%BASE%assets/img/{src}" alt="Youthaid Academy" width="720" height="348"></a>')


_I = {
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.6-3.6 3.3-6 6.5-6s5.9 2.4 6.5 6"/><circle cx="17" cy="9" r="2.6"/><path d="M16.5 14.2c2.6.3 4.4 2.5 4.9 5.8"/>',
    "book": '<path d="M4 5.5C4 4.7 4.7 4 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5z"/><path d="M20 5.5c0-.8-.7-1.5-1.5-1.5H13v16h5.5c.8 0 1.5-.7 1.5-1.5z"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2.5"/><path d="M8.5 7V5.5C8.5 4.7 9.2 4 10 4h4c.8 0 1.5.7 1.5 1.5V7"/><path d="M3 12.5h18"/>',
    "heart": '<path d="M12 20s-7.5-4.6-8.8-9.4C2.3 7.4 4.4 4.5 7.5 4.5c1.9 0 3.4 1 4.5 2.6 1.1-1.6 2.6-2.6 4.5-2.6 3.1 0 5.2 2.9 4.3 6.1C19.5 15.4 12 20 12 20z"/>',
    "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17"/><path d="M12 3.5c2.4 2.5 3.6 5.3 3.6 8.5s-1.2 6-3.6 8.5c-2.4-2.5-3.6-5.3-3.6-8.5s1.2-6 3.6-8.5z"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    "star": '<path d="M12 3.8l2.5 5.1 5.6.8-4 3.9.9 5.6-5-2.6-5 2.6.9-5.6-4-3.9 5.6-.8z"/>',
    "hand": '<path d="M7 11V6.5a1.5 1.5 0 0 1 3 0V11M10 10V5a1.5 1.5 0 0 1 3 0v5M13 10V6a1.5 1.5 0 0 1 3 0v6"/><path d="M16 9.5a1.5 1.5 0 0 1 3 0V14c0 3.6-2.7 6.5-6.3 6.5h-.9c-2 0-3.5-.8-4.7-2.4L4.3 14.5a1.5 1.5 0 0 1 2.3-1.9L8 14"/>',
    "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
    "shield": '<path d="M12 3.5l7 2.8v5.2c0 4.3-2.9 7.6-7 9-4.1-1.4-7-4.7-7-9V6.3z"/><path d="M9 12l2 2 4-4"/>',
    "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M3.5 7l8.5 6 8.5-6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M16.5 16.5L21 21"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
    "cap": '<path d="M2.5 9.5L12 5l9.5 4.5L12 14z"/><path d="M6.5 11.5v4c1.4 1.5 3.3 2.3 5.5 2.3s4.1-.8 5.5-2.3v-4"/><path d="M21.5 9.5v5"/>',
    "chat": '<path d="M4 5.5h16v10H9l-5 4z"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
    "building": '<rect x="4" y="3.5" width="11" height="17" rx="1.5"/><path d="M15 9h4.5v11.5H15M7.5 7.5h4M7.5 11h4M7.5 14.5h4"/>',
    "leaf": '<path d="M5 19c0-8 5-13.5 15-14 0 9.5-5.5 14.5-13 14.5"/><path d="M5 19c3-4 6-6.5 9.5-8.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}


def icon(name, size=None):
    s = f' width="{size}" height="{size}"' if size else ""
    return (f'<svg viewBox="0 0 24 24"{s} fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>')


def page_hero(eyebrow, title, lead, accent="var(--teal)", buttons=""):
    return f"""<section class="page-hero" style="--accent:{accent}">
  <div class="container">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    {buttons}
  </div>
</section>"""


def section(inner, cls="", head=None, center=False):
    h = ""
    if head:
        eyebrow, title, lead = (list(head) + [None, None])[:3]
        h = f'<div class="section-head{" center" if center else ""}">'
        if eyebrow:
            h += f'<span class="eyebrow">{eyebrow}</span>'
        h += f"<h2>{title}</h2>"
        if lead:
            h += f'<p class="lead">{lead}</p>'
        h += "</div>"
    return f'<section class="section {cls}"><div class="container">{h}{inner}</div></section>'


COLORS = ["c-teal", "c-sun", "c-red", "c-orange"]


def card(ic, title, text, color="c-teal", link=None, link_label=None, extra=""):
    lk = f'<a class="card-link" href="{link}">{link_label} →</a>' if link else ""
    ico = f'<div class="icon {color}">{icon(ic)}</div>' if ic else ""
    return f'<article class="card hover">{ico}<h3>{title}</h3><p>{text}</p>{extra}{lk}</article>'


def cards(items, cols=3):
    out = []
    for i, it in enumerate(items):
        it = dict(it)
        it.setdefault("color", COLORS[i % 4])
        out.append(card(**it))
    return f'<div class="grid grid-{cols}">' + "".join(out) + "</div>"


def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def btn(href, label, kind="primary"):
    return f'<a class="btn btn-{kind}" href="{href}">{label}</a>'


def btns(*items):
    return '<div class="btn-row">' + "".join(items) + "</div>"


def cta_band(title, text, buttons, teal=False):
    return (f'<div class="cta-band{" teal" if teal else ""}"><div><h2>{title}</h2><p>{text}</p></div>'
            f'<div class="btn-row" style="margin:0">{buttons}</div></div>')


def steps(items):
    return '<div class="steps">' + "".join(
        f'<div class="step"><h3>{a}</h3><p>{b}</p></div>' for a, b in items) + "</div>"


def faq(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def empty(title, text, buttons=""):
    return f'<div class="empty"><h3>{title}</h3><p>{text}</p>{buttons}</div>'


def todo(text):
    return f'<span class="todo">{text}</span>'


def two_col(left, right):
    return f'<div class="grid grid-2" style="align-items:start;gap:48px">{left}<div>{right}</div></div>'


# ---------- Formulaires ----------
def field(fid, label, kind="text", required=True, options=None, hint=None, placeholder=""):
    req = " required" if required else ""
    star = " *" if required else ""
    ph = f' placeholder="{placeholder}"' if placeholder else ""
    if kind == "textarea":
        ctrl = f'<textarea id="{fid}" name="{fid}"{req}{ph}></textarea>'
    elif kind == "select":
        opts = "".join(f"<option>{o}</option>" for o in options)
        ctrl = f'<select id="{fid}" name="{fid}"{req}><option value="">—</option>{opts}</select>'
    else:
        auto = {"email": "email", "tel": "tel"}.get(kind, "")
        ac = f' autocomplete="{auto}"' if auto else ""
        ctrl = f'<input id="{fid}" name="{fid}" type="{kind}"{req}{ph}{ac}>'
    h = f'<div class="hint">{hint}</div>' if hint else ""
    return f'<div class="field"><label for="{fid}">{label}{star}</label>{ctrl}{h}</div>'


def row(*fields):
    return '<div class="form-row">' + "".join(fields) + "</div>"


def form(t, subject, fields_html, submit_label):
    consent = (f'<label class="check"><input type="checkbox" name="consent" required '
               f'data-label="{t("J’accepte la politique de confidentialité", "I accept the privacy policy")}">'
               '<span>' + t('J’accepte que mes données soient utilisées pour traiter ma demande, conformément à la <a href="confidentialite.html">politique de confidentialité</a>.',
                            'I agree that my data will be used to process my request, in line with the <a href="confidentialite.html">privacy policy</a>.') + ' *</span></label>')
    if CONTACT_EMAIL:
        note = t("Envoyer ouvre votre messagerie avec votre message pré-rempli, prêt à partir. Les champs marqués * sont obligatoires.",
                 "Sending opens your email app with your message pre-filled, ready to go. Fields marked * are required.")
        attrs = f'data-mailto="{CONTACT_EMAIL}" data-subject="{subject}"'
        button = f'<button class="btn btn-primary" type="submit">{submit_label}</button>'
    else:
        note = t("Ce formulaire sera activé très prochainement.", "This form will be activated very soon.")
        attrs = 'onsubmit="return false"'
        button = f'<button class="btn btn-primary" type="submit" disabled>{submit_label}</button>'
    return (f'<form class="form card" {attrs}>'
            f'{fields_html}{consent}<p class="form-note">{note}</p>'
            f'<div>{button}</div><p class="form-status" role="status" hidden></p></form>')
