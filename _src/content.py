"""Contenu des pages du site Youthaid Academy (français / anglais).

Chaque page : slug (nom du fichier), title, desc (description pour Google), render(t).
t(fr, en) choisit le texte selon la langue.
Ajouter une page ici l'ajoute automatiquement au site, à la recherche et au sitemap.
"""
from lib import (LOGO_MARK, OFFICES, ORG_EMAIL, ORG_PHONE, btn, btns, card, cards, checklist, cta_band, empty, faq, field, form,
                 icon, office_line, page_hero, phone_href, row, section, social_links, steps, todo, two_col)

PAGES = []


def page(slug, title, desc, accent="var(--teal)", nav=None):
    def deco(fn):
        p = {"slug": slug, "title": title, "desc": desc, "render": fn, "accent": accent}
        if nav:
            p["nav"] = nav
        PAGES.append(p)
        return fn
    return deco


# =====================================================================
# ACCUEIL
# =====================================================================
@page("index",
      lambda t: t("Accueil", "Home"),
      lambda t: t("Youthaid Academy accompagne les jeunes issus de milieux défavorisés vers la réussite scolaire, professionnelle et entrepreneuriale : mentorat, formations, opportunités et engagement citoyen.",
                  "Youthaid Academy supports young people from disadvantaged backgrounds towards academic, professional and entrepreneurial success: mentoring, training, opportunities and civic engagement."))
def home(t):
    h1 = t("Construire ton <span class='w-orange'>avenir</span>, saisir chaque <span class='w-teal'>opportunité</span>.",
           "Build your <span class='w-orange'>future</span>, seize every <span class='w-teal'>opportunity</span>.")
    hero = f"""<section class="hero">
  <div class="container hero-grid">
    <div class="hero-text">
      <h1>{h1}</h1>
      <p class="lead">{t("Youthaid Academy accompagne les jeunes issus de milieux défavorisés vers la réussite scolaire, professionnelle et entrepreneuriale : des mentors qui s’engagent, des formations pour monter en compétences et des opportunités concrètes.",
                         "Youthaid Academy supports young people from disadvantaged backgrounds towards academic, professional and entrepreneurial success: committed mentors, training to build your skills and real opportunities.")}</p>
      <div class="hero-search search-box">
        <form role="search">
          <input type="search" class="search-input" placeholder="{t("Mentorat, formation, stage…", "Mentoring, course, internship…")}" aria-label="{t("Rechercher sur le site", "Search the site")}" autocomplete="off">
          <button type="submit" aria-label="{t("Rechercher", "Search")}">{icon("search", 22)}</button>
        </form>
        <ul class="search-results" aria-live="polite"></ul>
      </div>
      {btns(btn("adherer.html", t("Je rejoins Youthaid", "Join Youthaid")), btn("devenir-mentor.html", t("Je deviens mentor", "Become a mentor"), "outline"))}
    </div>
    <div class="hero-visual">
      <svg class="hv-ring" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="44" pathLength="100"/></svg>
      <div class="hv-disc"><img src="%BASE%assets/img/brice-akanou.jpg" alt="{t("Brice Akanou, fondateur de Youthaid Academy", "Brice Akanou, founder of Youthaid Academy")}" width="820" height="820"></div>
      <svg class="hv-squiggle" viewBox="0 0 120 160" aria-hidden="true"><path d="M100 10c-30 10-10 45-40 55S30 110 50 125s-20 30-40 25"/></svg>
      <svg class="hv-arc" viewBox="0 0 100 60" aria-hidden="true"><path d="M8 10c35-6 66 10 84 42"/></svg>
      <div class="hv-card hv-c1">
        <span class="hv-tag">Youthaid Academy</span>
        <strong>{t("Un mentor à tes côtés", "A mentor by your side")}</strong>
        <span class="hv-dot" style="background:var(--teal)">{icon("users", 18)}</span>
      </div>
      <div class="hv-card hv-c2">
        <span class="hv-dot" style="background:var(--sun)">{icon("star", 18)}</span>
        <strong class="hv-big">Brice Akanou</strong>
        <span>{t("Fondateur", "Founder")}</span>
      </div>
      <div class="hv-card hv-c3">
        <span class="hv-tag">{t("Formations", "Training")}</span>
        <strong>Youthaid Academy’s Compétences</strong>
        <p>{t("Des cours en ligne structurés, des quiz et des attestations pour avancer.", "Structured online courses, quizzes and certificates to move forward.")}</p>
        <div class="hv-pills"><span>{t("En ligne", "Online")}</span><span>Quiz</span><span>{t("Attestation", "Certificate")}</span></div>
      </div>
    </div>
  </div>
</section>
<section class="statement">
  <div class="container">
    <p class="statement-big">{t("Youthaid Academy est une fondation qui permet aux jeunes de développer leurs compétences et de se connecter à des opportunités pour construire leur avenir et libérer leur potentiel.",
                                "Youthaid Academy is a foundation that helps young people build their skills and connect with opportunities to shape their future and unlock their potential.")}</p>
    <p class="lead">{t("Peu importe d’où tu viens : mentorat, formations, opportunités et engagement citoyen sont réunis au même endroit, pour que chaque jeune puisse tracer son propre chemin.",
                       "Wherever you come from: mentoring, training, opportunities and civic engagement come together in one place, so every young person can find their own path.")}</p>
  </div>
</section>"""

    what = section(cards([
        dict(ic="users", title=t("Un mentor à tes côtés", "A mentor by your side"),
             text=t("Des professionnels de tous horizons t’écoutent, te conseillent et t’ouvrent leur réseau, à ton rythme.",
                    "Professionals from every background listen, advise and open their networks to you, at your own pace."),
             link="mentorat.html", link_label=t("Découvrir le mentorat", "Discover mentoring")),
        dict(ic="cap", title="Youthaid Academy’s Compétences",
             text=t("Des cours en ligne structurés, des quiz et des attestations pour développer les compétences qui comptent.",
                    "Structured online courses, quizzes and certificates to build the skills that matter."),
             link="formations.html", link_label=t("Voir les formations", "See the courses")),
        dict(ic="briefcase", title=t("Des opportunités ciblées", "Targeted opportunities"),
             text=t("Emplois, stages, alternances, jobs étudiants, bourses et bénévolat, sélectionnés pour toi.",
                    "Jobs, internships, apprenticeships, student jobs, scholarships and volunteering, picked for you."),
             link="opportunites.html", link_label=t("Explorer les opportunités", "Explore opportunities")),
        dict(ic="globe", title=t("S’engager pour sa communauté", "Engage in your community"),
             text=t("Des actions citoyennes, des événements et des rencontres pour agir localement et au-delà.",
                    "Civic actions, events and meet-ups to make a difference locally and beyond."),
             link="evenements.html", link_label=t("Voir les événements", "See events")),
    ], cols=4), head=(t("Ce que nous faisons", "What we do"),
                      t("Tout ce qu’il faut pour avancer, au même endroit", "Everything you need to move forward, in one place"),
                      t("Youthaid Academy réunit l’accompagnement humain, la formation et l’accès aux opportunités pour que chaque jeune puisse construire son parcours.",
                        "Youthaid Academy brings together personal support, training and access to opportunities so every young person can build their own path.")))

    how = section(steps([
        (t("Je m’inscris", "I sign up"), t("Je crée mon profil et je partage mes envies, mes besoins et mes centres d’intérêt.", "I create my profile and share my goals, needs and interests.")),
        (t("Je suis accompagné", "I get support"), t("Un mentor m’est proposé selon mon projet, et l’équipe valide chaque mise en relation.", "I’m matched with a mentor based on my project, and the team approves every match.")),
        (t("Je me forme", "I learn"), t("Je suis des parcours de formation en ligne et je gagne des attestations.", "I follow online learning paths and earn certificates.")),
        (t("Je saisis ma chance", "I seize my chance"), t("Je candidate aux opportunités qui me correspondent : stage, emploi, alternance, bourse…", "I apply to opportunities that suit me: internship, job, apprenticeship, scholarship…")),
    ]), cls="section-soft", head=(t("Comment ça marche", "How it works"), t("Ton parcours en 4 étapes", "Your journey in 4 steps")))

    who = section(cards([
        dict(ic="spark", title=t("Tu es un jeune", "You’re a young person"),
             text=t("Tu as des rêves, des questions ou besoin d’un coup de pouce ? Rejoins la communauté.", "Got dreams, questions or need a boost? Join the community."),
             link="adherer.html", link_label=t("Rejoindre", "Join")),
        dict(ic="chat", title=t("Tu veux transmettre", "You want to give back"),
             text=t("Partage ton expérience et aide un jeune à trouver sa voie en devenant mentor.", "Share your experience and help a young person find their way as a mentor."),
             link="devenir-mentor.html", link_label=t("Devenir mentor", "Become a mentor")),
        dict(ic="hand", title=t("Tu as du temps à donner", "You have time to give"),
             text=t("Ateliers, événements, communication : rejoins nos bénévoles.", "Workshops, events, communications: join our volunteers."),
             link="devenir-benevole.html", link_label=t("Devenir bénévole", "Volunteer")),
        dict(ic="building", title=t("Tu représentes une organisation", "You represent an organisation"),
             text=t("Entreprises, institutions, associations : publiez des offres et construisons ensemble.", "Companies, institutions, associations: post opportunities and let’s build together."),
             link="partenaires.html", link_label=t("Devenir partenaire", "Become a partner")),
    ], cols=4), head=(t("Pour qui ?", "Who is it for?"), t("Chacun a sa place chez Youthaid", "There’s a place for everyone at Youthaid")))

    values = section(
        '<div class="grid grid-3">' + "".join(
            f'<div><h3 style="color:#fff">{a}</h3><p>{b}</p></div>' for a, b in [
                (t("Égalité des chances", "Equal opportunities"), t("Le talent est partout ; les opportunités doivent l’être aussi.", "Talent is everywhere; opportunities should be too.")),
                (t("Accompagnement humain", "Human support"), t("Chaque jeune est suivi par des personnes engagées, pas par un algorithme.", "Every young person is supported by committed people, not an algorithm.")),
                (t("Confiance et sécurité", "Trust and safety"), t("Les données des jeunes sont protégées et chaque mise en relation est validée.", "Young people’s data is protected and every match is approved.")),
            ]) + "</div>",
        cls="section-dark",
        head=(t("Nos engagements", "Our commitments"), t("Ce qui nous guide", "What guides us")))

    news = section(
        '<div class="grid grid-3">' + news_card(t) + "</div>"
        + btns(btn("actualites.html", t("Toutes les actualités", "All news"), "outline")),
        head=(t("Actualités", "News"), t("Les dernières nouvelles", "Latest news")))

    cta = section(cta_band(
        t("Chaque don ouvre une porte", "Every donation opens a door"),
        t("Soutenez l’accompagnement, la formation et l’accès aux opportunités des jeunes.", "Support mentoring, training and access to opportunities for young people."),
        btn("don.html", t("Faire un don", "Donate"), "light") + btn("partenaires.html", t("Devenir partenaire", "Become a partner"), "dark")))

    return hero + what + how + who + values + news + cta


def news_card(t):
    return f"""<article class="card hover post-card">
  <div class="post-visual" aria-hidden="true">{LOGO_MARK}</div>
  <div class="meta">19/11/2026 · {t("Vie de la fondation", "Foundation news")}</div>
  <h3>{t("Youthaid Academy lance son site internet", "Youthaid Academy launches its website")}</h3>
  <p>{t("Découvrez notre mission, nos programmes et toutes les façons de rejoindre l’aventure.", "Discover our mission, our programmes and all the ways to join the adventure.")}</p>
  <a class="card-link" href="actualites.html#lancement">{t("Lire l’article", "Read the article")} →</a>
</article>"""


# =====================================================================
# QUI SOMMES-NOUS
# =====================================================================
@page("a-propos",
      lambda t: t("À propos", "About"),
      lambda t: t("Youthaid Academy est une initiative à vocation sociale dédiée à l’égalité des chances pour les jeunes issus de milieux défavorisés.",
                  "Youthaid Academy is a social initiative dedicated to equal opportunities for young people from disadvantaged backgrounds."))
def about(t):
    intro = page_hero(t("À propos", "About"),
                      t("Une fondation pour que chaque jeune ait sa chance", "A foundation so every young person gets their chance"),
                      t("Youthaid Academy est une initiative à vocation sociale dédiée à l’égalité des chances pour les jeunes issus de milieux défavorisés.",
                        "Youthaid Academy is a social initiative dedicated to equal opportunities for young people from disadvantaged backgrounds."))
    story = section(two_col(
        f"<div><h2>{t('Pourquoi Youthaid Academy ?', 'Why Youthaid Academy?')}</h2>"
        f"<p>{t('Trop de jeunes talentueux voient leurs ambitions freinées faute de réseau, d’information ou d’accompagnement. Youthaid Academy est née pour changer cela.', 'Too many talented young people see their ambitions held back by a lack of network, information or support. Youthaid Academy was created to change that.')}</p>"
        f"<p>{t('Nous accompagnons les jeunes en difficulté vers la réussite scolaire, professionnelle et entrepreneuriale en les mettant en relation avec des mentors issus de divers domaines professionnels, et en leur offrant des opportunités de formation, d’emploi, de stage, d’alternance, de job étudiant et d’engagement civique dans leur communauté locale et au-delà.', 'We support young people facing difficulties towards academic, professional and entrepreneurial success by connecting them with mentors from many professional fields, and by offering them opportunities for training, jobs, internships, apprenticeships, student jobs and civic engagement in their local community and beyond.')}</p></div>",
        checklist([
            t("<strong>Relier</strong> les jeunes à des mentors engagés", "<strong>Connect</strong> young people with committed mentors"),
            t("<strong>Former</strong> grâce à des parcours en ligne accessibles", "<strong>Train</strong> through accessible online learning paths"),
            t("<strong>Ouvrir</strong> l’accès aux opportunités académiques et professionnelles", "<strong>Open</strong> access to academic and professional opportunities"),
            t("<strong>Rassembler</strong> une communauté de membres, bénévoles et partenaires", "<strong>Bring together</strong> a community of members, volunteers and partners"),
            t("<strong>Mesurer</strong> notre impact en toute transparence", "<strong>Measure</strong> our impact transparently"),
        ])))
    team = section(
        cards([
            dict(ic="spark", title=t("Les jeunes", "Young people"), text=t("Au cœur de tout ce que nous faisons : ils construisent leur parcours, nous les accompagnons.", "At the heart of everything we do: they build their path, we support them.")),
            dict(ic="chat", title=t("Les mentors", "Mentors"), text=t("Des professionnels et bénévoles qui transmettent leur expérience.", "Professionals and volunteers who pass on their experience.")),
            dict(ic="hand", title=t("Les bénévoles et membres", "Volunteers and members"), text=t("Ils font vivre les actions, les événements et la communauté.", "They bring our actions, events and community to life.")),
            dict(ic="building", title=t("Les partenaires", "Partners"), text=t("Entreprises, institutions et associations qui ouvrent des portes.", "Companies, institutions and associations that open doors.")),
        ], cols=4),
        cls="section-soft",
        head=(t("Notre communauté", "Our community"), t("Ensemble, plus loin", "Further, together")))
    cta = section(cta_band(t("Envie d’en savoir plus ?", "Want to know more?"),
                           t("Découvrez notre mission, notre vision et nos valeurs.", "Discover our mission, vision and values."),
                           btn("mission.html", t("Mission et valeurs", "Mission and values"), "light"), teal=True))
    return intro + story + team + cta


@page("mission",
      lambda t: t("Mission, vision et valeurs", "Mission, vision and values"),
      lambda t: t("La mission, la vision et les valeurs de Youthaid Academy : agir pour l’égalité des chances des jeunes.",
                  "Youthaid Academy’s mission, vision and values: acting for equal opportunities for young people."),
      accent="var(--sun)")
def mission(t):
    intro = page_hero(t("Mission, vision et valeurs", "Mission, vision and values"),
                      t("Agir pour l’égalité des chances", "Acting for equal opportunities"),
                      t("Ce qui nous anime, ce vers quoi nous allons et la façon dont nous le faisons.",
                        "What drives us, where we’re heading and how we get there."), accent="var(--sun)")
    mv = section(cards([
        dict(ic="target", title=t("Notre mission", "Our mission"),
             text=t("Accompagner les jeunes issus de milieux défavorisés vers la réussite scolaire, professionnelle et entrepreneuriale, grâce au mentorat, à la formation et à l’accès à des opportunités concrètes.",
                    "Support young people from disadvantaged backgrounds towards academic, professional and entrepreneurial success through mentoring, training and access to real opportunities.")),
        dict(ic="globe", title=t("Notre vision", "Our vision"),
             text=t("Un monde où l’origine sociale ne détermine plus l’avenir : chaque jeune a accès aux mêmes réseaux, aux mêmes savoirs et aux mêmes chances.",
                    "A world where social background no longer determines the future: every young person has access to the same networks, knowledge and chances.")),
        dict(ic="heart", title=t("Notre approche", "Our approach"),
             text=t("Un accompagnement humain, soutenu par une plateforme numérique sécurisée qui relie jeunes, mentors, bénévoles et partenaires.",
                    "Personal support, backed by a secure digital platform connecting young people, mentors, volunteers and partners.")),
    ]))
    vals = [
        ("star", t("Égalité des chances", "Equal opportunities"), t("Nous agissons pour que le talent, et non l’origine, ouvre les portes.", "We act so that talent, not background, opens doors.")),
        ("users", t("Solidarité", "Solidarity"), t("La réussite se construit ensemble, grâce à ceux qui transmettent.", "Success is built together, thanks to those who pass on what they know.")),
        ("shield", t("Confiance", "Trust"), t("Protection des données, mises en relation validées, transparence financière.", "Data protection, approved matches, financial transparency.")),
        ("leaf", t("Engagement", "Commitment"), t("Nous encourageons chaque jeune à s’engager à son tour dans sa communauté.", "We encourage every young person to get involved in their community in turn.")),
    ]
    values = section(cards([dict(ic=i, title=a, text=b) for i, a, b in vals], cols=4), cls="section-soft",
                     head=(t("Nos valeurs", "Our values"), t("Ce en quoi nous croyons", "What we believe in")))
    return intro + mv + values


@page("impact",
      lambda t: t("Impact et témoignages", "Impact and stories"),
      lambda t: t("Comment Youthaid Academy mesure son impact auprès des jeunes, et les témoignages de notre communauté.",
                  "How Youthaid Academy measures its impact on young people, and stories from our community."),
      accent="var(--red)")
def impact(t):
    intro = page_hero(t("Impact et témoignages", "Impact and stories"),
                      t("Mesurer ce qui compte vraiment", "Measuring what really matters"),
                      t("Nous suivons notre action avec rigueur et la partagerons en toute transparence.",
                        "We track our work rigorously and will share it transparently."), accent="var(--red)")
    ind = [
        ("users", t("Mentorat", "Mentoring"), t("Nombre de mentors et de mentorés, taux de mises en relation réussies.", "Number of mentors and mentees, successful match rate.")),
        ("cap", t("Formation", "Learning"), t("Progression pédagogique et taux de complétion des cours.", "Learning progress and course completion rate.")),
        ("briefcase", t("Opportunités", "Opportunities"), t("Nombre d’opportunités publiées, consultées et obtenues.", "Number of opportunities posted, viewed and secured.")),
        ("calendar", t("Événements", "Events"), t("Participation aux ateliers, forums et rencontres.", "Participation in workshops, forums and meet-ups.")),
        ("users", t("Communauté", "Community"), t("Adhérents actifs et utilisateurs engagés sur la plateforme.", "Active members and engaged platform users.")),
        ("heart", t("Soutien", "Support"), t("Volume des dons et cotisations, et leur utilisation.", "Donations and membership fees, and how they are used.")),
    ]
    indicators = section(cards([dict(ic=i, title=a, text=b) for i, a, b in ind], cols=3),
                         head=(t("Nos indicateurs", "Our indicators"), t("Ce que nous suivons", "What we track"),
                               t("Nos premiers résultats seront publiés ici dès le lancement de nos programmes.",
                                 "Our first results will be published here as soon as our programmes launch.")))
    stories = section(empty(t("Vos histoires arrivent bientôt", "Your stories are coming soon"),
                            t("Jeunes, mentors, bénévoles, partenaires : vous avez vécu l’aventure Youthaid ? Partagez votre témoignage.",
                              "Young people, mentors, volunteers, partners: been part of the Youthaid journey? Share your story."),
                            btns(btn("contact.html", t("Partager mon témoignage", "Share my story")))),
                      cls="section-soft", head=(t("Témoignages", "Stories"), t("Ils racontent Youthaid", "In their own words")))
    return intro + indicators + stories


@page("partenaires",
      lambda t: t("Partenaires", "Partners"),
      lambda t: t("Entreprises, institutions, associations : devenez partenaire de Youthaid Academy et ouvrez des portes aux jeunes.",
                  "Companies, institutions, associations: partner with Youthaid Academy and open doors for young people."),
      accent="var(--orange)")
def partners(t):
    intro = page_hero(t("Partenaires", "Partners"),
                      t("Ouvrons des portes, ensemble", "Let’s open doors, together"),
                      t("Entreprises, institutions, collectivités, écoles et associations : votre engagement change concrètement des trajectoires.",
                        "Companies, institutions, local authorities, schools and associations: your commitment makes a real difference to young lives."),
                      accent="var(--orange)", buttons=btns(btn("contact.html", t("Devenir partenaire", "Become a partner"))))
    ways = section(cards([
        dict(ic="briefcase", title=t("Publier des opportunités", "Post opportunities"), text=t("Stages, alternances, emplois, jobs étudiants : touchez des jeunes motivés et accompagnés.", "Internships, apprenticeships, jobs, student jobs: reach motivated, supported young people.")),
        dict(ic="users", title=t("Mobiliser vos collaborateurs", "Engage your employees"), text=t("Proposez à vos équipes de devenir mentors ou d’animer des ateliers.", "Invite your teams to become mentors or run workshops.")),
        dict(ic="calendar", title=t("Co-organiser des événements", "Co-host events"), text=t("Forums, journées d’orientation, visites d’entreprise, conférences.", "Forums, career days, company visits, talks.")),
        dict(ic="heart", title=t("Soutenir financièrement", "Provide funding"), text=t("Mécénat, subventions ou soutien à un programme précis.", "Sponsorship, grants or support for a specific programme.")),
    ], cols=4), head=(t("Comment s’engager", "How to get involved"), t("Plusieurs façons de contribuer", "Many ways to contribute")))
    logos = section(empty(t("Rejoignez nos premiers partenaires", "Join our first partners"),
                          t("Votre logo pourrait figurer ici. Un espace dédié vous permettra bientôt de gérer votre profil, vos représentants et vos offres.",
                            "Your logo could be here. A dedicated space will soon let you manage your profile, representatives and opportunities."),
                          btns(btn("contact.html", t("Nous contacter", "Contact us")))), cls="section-soft")
    return intro + ways + logos


# =====================================================================
# NOS ACTIONS
# =====================================================================
@page("programmes",
      lambda t: t("Nos programmes", "Our programmes"),
      lambda t: t("Réussite scolaire, insertion professionnelle, entrepreneuriat et engagement civique : les programmes de Youthaid Academy.",
                  "Academic success, employability, entrepreneurship and civic engagement: Youthaid Academy’s programmes."))
def programmes(t):
    intro = page_hero(t("Nos programmes", "Our programmes"),
                      t("Des programmes pour chaque étape de ton parcours", "Programmes for every step of your journey"),
                      t("Que tu sois au lycée, à l’université, en recherche d’emploi ou porteur de projet, il y a un programme pour toi.",
                        "Whether you’re in school, at university, job hunting or have a project, there’s a programme for you."))
    progs = section(cards([
        dict(ic="book", title=t("Réussite scolaire", "Academic success"),
             text=t("Orientation, méthodologie, soutien et conseils pour réussir ses études et choisir sa voie.", "Guidance, study skills, support and advice to succeed in your studies and choose your path."),
             link="mentorat.html", link_label=t("Trouver un mentor", "Find a mentor")),
        dict(ic="briefcase", title=t("Insertion professionnelle", "Employability"),
             text=t("CV, entretiens, réseau, premières expériences : tout pour décrocher un stage, une alternance ou un emploi.", "CVs, interviews, networking, first experiences: everything to land an internship, apprenticeship or job."),
             link="opportunites.html", link_label=t("Voir les opportunités", "See opportunities")),
        dict(ic="spark", title=t("Entrepreneuriat", "Entrepreneurship"),
             text=t("Transformer une idée en projet : accompagnement par des entrepreneurs, formations et mise en réseau.", "Turn an idea into a project: support from entrepreneurs, training and networking."),
             link="formations.html", link_label=t("Voir les formations", "See courses")),
        dict(ic="globe", title=t("Engagement civique", "Civic engagement"),
             text=t("Bénévolat, projets locaux et initiatives citoyennes pour agir dans sa communauté.", "Volunteering, local projects and civic initiatives to act in your community."),
             link="evenements.html", link_label=t("Voir les événements", "See events")),
    ], cols=2))
    cta = section(cta_band(t("Prêt à commencer ?", "Ready to start?"),
                           t("Rejoins Youthaid Academy et accède à nos programmes.", "Join Youthaid Academy and access our programmes."),
                           btn("adherer.html", t("Je m’inscris", "Sign up"), "light")))
    return intro + progs + cta


@page("mentorat",
      lambda t: t("Mentorat", "Mentoring"),
      lambda t: t("Le mentorat Youthaid Academy : un professionnel bénévole accompagne un jeune pour l’aider à réussir ses études, son insertion ou son projet.",
                  "Youthaid Academy mentoring: a volunteer professional supports a young person to succeed in their studies, career or project."))
def mentoring(t):
    intro = page_hero(t("Mentorat", "Mentoring"),
                      t("Un mentor, ça change tout", "A mentor changes everything"),
                      t("Le mentorat est au cœur de Youthaid Academy : un professionnel bénévole accompagne un jeune, l’écoute, le conseille et lui ouvre son réseau.",
                        "Mentoring is at the heart of Youthaid Academy: a volunteer professional supports a young person, listens, advises and opens up their network."),
                      buttons=btns(btn("contact.html", t("Demander un mentor", "Request a mentor")), btn("devenir-mentor.html", t("Devenir mentor", "Become a mentor"), "outline")))
    how = section(steps([
        (t("Ta demande", "Your request"), t("Tu décris tes besoins, ton projet et tes disponibilités.", "You describe your needs, your project and your availability.")),
        (t("Le matching", "The match"), t("Nous te proposons un mentor selon des critères précis : domaine, objectifs, langue, lieu.", "We suggest a mentor based on clear criteria: field, goals, language, location.")),
        (t("La validation", "Approval"), t("Chaque binôme est validé par un coordinateur de l’équipe.", "Every pair is approved by a team coordinator.")),
        (t("Le suivi", "Follow-up"), t("Rendez-vous réguliers, journal de suivi et bilan de fin de parcours.", "Regular meetings, a progress log and an end-of-programme review.")),
    ]), head=(t("Comment ça marche", "How it works"), t("Un accompagnement encadré", "Structured support")))
    both = section(cards([
        dict(ic="spark", title=t("Pour les jeunes", "For young people"),
             text=t("Un regard extérieur bienveillant, des conseils concrets, un réseau qui s’ouvre et quelqu’un qui croit en toi.", "A caring outside view, practical advice, a network that opens up and someone who believes in you.")),
        dict(ic="chat", title=t("Pour les mentors", "For mentors"),
             text=t("Transmettre, donner du sens à son expérience et contribuer concrètement à l’égalité des chances.", "Pass on knowledge, give meaning to your experience and make a real contribution to equal opportunities.")),
        dict(ic="shield", title=t("Un cadre sécurisé", "A safe framework"),
             text=t("Mises en relation validées, charte d’engagement et supervision par nos coordinateurs.", "Approved matches, a commitment charter and supervision by our coordinators.")),
    ]), cls="section-soft")
    return intro + how + both


@page("formations",
      lambda t: t("Formations", "Training"),
      lambda t: t("Youthaid Academy’s Compétences : des formations en ligne avec cours, quiz et attestations pour développer ses compétences.",
                  "Youthaid Academy’s Compétences: online courses with lessons, quizzes and certificates to build your skills."),
      accent="var(--sun)")
def training(t):
    intro = page_hero("Youthaid Academy’s Compétences",
                      t("Apprendre à ton rythme, gratuitement ou presque", "Learn at your own pace"),
                      t("Notre plateforme de formation en ligne propose des parcours structurés pour développer les compétences qui comptent pour tes études, ton emploi et tes projets.",
                        "Our online learning platform offers structured paths to build the skills that matter for your studies, job and projects."), accent="var(--sun)")
    feats = section(cards([
        dict(ic="book", title=t("Un catalogue de cours", "A course catalogue"), text=t("Des cours classés par thème, avec des filtres pour trouver rapidement ce qu’il te faut.", "Courses sorted by topic, with filters to quickly find what you need.")),
        dict(ic="cap", title=t("Des parcours structurés", "Structured paths"), text=t("Modules, chapitres et leçons : vidéos, PDF, quiz et exercices pratiques.", "Modules, chapters and lessons: videos, PDFs, quizzes and practical exercises.")),
        dict(ic="target", title=t("Ta progression", "Your progress"), text=t("Un tableau de bord pour suivre ton avancement et reprendre où tu t’es arrêté.", "A dashboard to track your progress and pick up where you left off.")),
        dict(ic="star", title=t("Des attestations", "Certificates"), text=t("Valide tes acquis et valorise-les sur ton CV.", "Validate what you’ve learned and showcase it on your CV.")),
        dict(ic="users", title=t("En groupe", "In groups"), text=t("Des cohortes pour apprendre ensemble et s’entraider.", "Cohorts to learn together and help each other.")),
        dict(ic="chat", title=t("Des formateurs engagés", "Committed trainers"), text=t("Des professionnels conçoivent et animent les contenus.", "Professionals design and deliver the content.")),
    ]), head=(t("La plateforme", "The platform"), t("Une vraie expérience d’apprentissage", "A real learning experience")))
    topics = [t("Orientation", "Career guidance"), t("CV et entretien", "CV and interviews"), t("Prise de parole", "Public speaking"),
              t("Outils numériques", "Digital tools"), t("Entrepreneuriat", "Entrepreneurship"), t("Gestion de projet", "Project management"),
              t("Éducation financière", "Financial literacy"), t("Langues", "Languages"), t("Leadership", "Leadership")]
    cat = section(empty(t("Le catalogue ouvre bientôt", "The catalogue opens soon"),
                        t("Thèmes prévus :", "Planned topics:") + "<br><br>" + "".join(f'<span class="tag">{x}</span>' for x in topics),
                        btns(btn("adherer.html", t("Être prévenu de l’ouverture", "Get notified when it opens")))),
                  cls="section-soft")
    trainer = section(cta_band(t("Vous souhaitez former des jeunes ?", "Want to train young people?"),
                               t("Rejoignez nos formateurs et partagez votre expertise.", "Join our trainers and share your expertise."),
                               btn("contact.html", t("Devenir formateur", "Become a trainer"), "light"), teal=True))
    return intro + feats + cat + trainer


@page("opportunites",
      lambda t: t("Opportunités", "Opportunities"),
      lambda t: t("Offres d’emploi, stages, alternances, jobs étudiants, bourses et bénévolat sélectionnés pour les jeunes de Youthaid Academy.",
                  "Jobs, internships, apprenticeships, student jobs, scholarships and volunteering selected for Youthaid Academy’s young people."),
      accent="var(--red)")
def opportunities(t):
    intro = page_hero(t("Opportunités", "Opportunities"),
                      t("Trouve l’opportunité qui te correspond", "Find the opportunity that fits you"),
                      t("Emplois, stages, alternances, jobs étudiants, bourses, appels à projets et bénévolat : des offres vérifiées, publiées par nos partenaires.",
                        "Jobs, internships, apprenticeships, student jobs, scholarships, calls for projects and volunteering: verified offers posted by our partners."), accent="var(--red)")
    types = [("briefcase", t("Emploi", "Jobs")), ("cap", t("Stage", "Internships")), ("book", t("Alternance", "Apprenticeships")),
             ("spark", t("Job étudiant", "Student jobs")), ("star", t("Bourses", "Scholarships")), ("hand", t("Bénévolat", "Volunteering"))]
    tiles = '<div class="grid grid-3">' + "".join(
        f'<div class="card" style="flex-direction:row;align-items:center;gap:14px;padding:20px"><div class="icon {["c-teal","c-sun","c-red","c-orange"][i % 4]}" style="margin:0">{icon(ic)}</div><h3 style="margin:0">{lbl}</h3></div>'
        for i, (ic, lbl) in enumerate(types)) + "</div>"
    cats = section(tiles, head=(t("Catégories", "Categories"), t("Toutes les opportunités", "All opportunities")))
    listing = section(empty(t("Les premières offres arrivent", "The first offers are coming"),
                            t("Bientôt, tu pourras filtrer les offres, voir les critères d’éligibilité et les dates limites, enregistrer tes favoris, recevoir des alertes et candidater en ligne.",
                              "Soon you’ll be able to filter offers, see eligibility criteria and deadlines, save favourites, get alerts and apply online."),
                            btns(btn("adherer.html", t("M’inscrire pour être alerté", "Sign up for alerts")), btn("partenaires.html", t("Publier une offre", "Post an offer"), "outline"))),
                      cls="section-soft")
    return intro + cats + listing


@page("evenements",
      lambda t: t("Événements", "Events"),
      lambda t: t("Ateliers, journées d’orientation, forums et rencontres communautaires organisés par Youthaid Academy.",
                  "Workshops, career days, forums and community meet-ups organised by Youthaid Academy."),
      accent="var(--orange)")
def events(t):
    intro = page_hero(t("Événements", "Events"),
                      t("Se rencontrer, apprendre, s’inspirer", "Meet, learn, get inspired"),
                      t("Ateliers, journées d’orientation, forums, rencontres communautaires et grands rendez-vous : nos événements créent des liens.",
                        "Workshops, career days, forums, community meet-ups and major gatherings: our events bring people together."), accent="var(--orange)")
    kinds = section(cards([
        dict(ic="book", title=t("Ateliers", "Workshops"), text=t("CV, entretien, prise de parole, outils numériques…", "CVs, interviews, public speaking, digital tools…")),
        dict(ic="target", title=t("Journées d’orientation", "Career days"), text=t("Découvrir des métiers et des parcours avec ceux qui les vivent.", "Discover careers and paths from people who live them.")),
        dict(ic="users", title=t("Forums et rencontres", "Forums and meet-ups"), text=t("Rencontrer entreprises, mentors et autres jeunes.", "Meet companies, mentors and other young people.")),
        dict(ic="star", title=t("Congrès", "Conferences"), text=t("Nos grands rendez-vous annuels autour de l’égalité des chances.", "Our major annual gatherings on equal opportunities.")),
    ], cols=4))
    upcoming = section(empty(t("Aucun événement programmé pour le moment", "No events scheduled yet"),
                             t("Les prochains événements seront annoncés ici, avec inscription en ligne et billets électroniques.",
                               "Upcoming events will be announced here, with online registration and e-tickets."),
                             btns(btn("adherer.html", t("Être informé", "Stay informed")))),
                       cls="section-soft", head=(t("Agenda", "Calendar"), t("Prochains événements", "Upcoming events")))
    return intro + kinds + upcoming


# =====================================================================
# S'ENGAGER
# =====================================================================
@page("don",
      lambda t: t("Faire un don", "Donate"),
      lambda t: t("Soutenez Youthaid Academy : chaque don finance le mentorat, la formation et l’accès aux opportunités des jeunes.",
                  "Support Youthaid Academy: every donation funds mentoring, training and access to opportunities for young people."),
      accent="var(--orange)")
def donate(t):
    intro = page_hero(t("Faire un don", "Donate"),
                      t("Votre don ouvre des portes", "Your donation opens doors"),
                      t("Chaque contribution finance directement l’accompagnement des jeunes : mentorat, formations, événements et accès aux opportunités.",
                        "Every contribution directly funds support for young people: mentoring, training, events and access to opportunities."), accent="var(--orange)")
    uses = section(cards([
        dict(ic="users", title=t("Le mentorat", "Mentoring"), text=t("Recruter, former et accompagner les binômes mentor / jeune.", "Recruiting, training and supporting mentor / mentee pairs.")),
        dict(ic="cap", title=t("Les formations", "Training"), text=t("Créer des cours en ligne accessibles à tous.", "Creating online courses accessible to all.")),
        dict(ic="calendar", title=t("Les événements", "Events"), text=t("Organiser ateliers, forums et journées d’orientation.", "Running workshops, forums and career days.")),
    ]), head=(t("À quoi sert votre don", "What your donation funds"), t("Un impact concret", "Real impact")))
    how = section(two_col(
        f"<div><h2>{t('Comment donner', 'How to give')}</h2>"
        f"<p>{t('Le don en ligne sécurisé (ponctuel ou mensuel) arrive très prochainement, avec un reçu envoyé automatiquement.', 'Secure online giving (one-off or monthly) is coming very soon, with a receipt sent automatically.')}</p>"
        f"<p>{t('En attendant, contactez-nous pour faire un don ou soutenir un programme précis : nous vous répondrons rapidement.', 'In the meantime, contact us to make a donation or support a specific programme: we’ll get back to you quickly.')}</p>"
        + btns(btn("contact.html", t("Nous contacter pour donner", "Contact us to give"))) + "</div>",
        '<div class="notice">' + t("<strong>Transparence.</strong> Nous publierons chaque année l’utilisation des fonds reçus dans notre rapport d’impact.",
                                   "<strong>Transparency.</strong> Each year we’ll publish how the funds we receive are used in our impact report.") + "</div>"
        + '<div class="notice">' + t("<strong>Entreprises et fondations.</strong> Mécénat, subventions, soutien à un programme : parlons-en ensemble.",
                                     "<strong>Companies and foundations.</strong> Sponsorship, grants, programme support: let’s talk.") + "</div>"),
        cls="section-soft")
    return intro + uses + how


def _signup_page(t, kind):
    """Formulaire commun pour adhérer / mentor / bénévole."""
    common = (row(field("prenom", t("Prénom", "First name")), field("nom", t("Nom", "Last name")))
              + row(field("email", "Email", "email"), field("ville", t("Ville", "City"))))
    if kind == "adherer":
        extra = (field("profil", t("Je suis", "I am"), "select", options=[
            t("Un jeune (16-30 ans)", "A young person (16-30)"), t("Un parent / représentant légal", "A parent / legal guardian"),
            t("Un membre adhérent", "A supporting member"), t("Une organisation", "An organisation")])
            + field("message", t("Ce que tu attends de Youthaid", "What you expect from Youthaid"), "textarea", required=False))
        return form(t, t("Adhésion à Youthaid Academy", "Joining Youthaid Academy"), common + extra, t("Envoyer ma demande d’adhésion", "Send my membership request"))
    if kind == "mentor":
        extra = (row(field("metier", t("Métier / secteur", "Job / sector")), field("dispo", t("Disponibilité", "Availability"), "select", options=[
            t("1 h par mois", "1 hour a month"), t("2 h par mois", "2 hours a month"), t("Plus de 2 h par mois", "More than 2 hours a month")]))
            + field("domaines", t("Domaines où tu peux accompagner", "Areas where you can help"), placeholder=t("Ex. : orientation, CV, entrepreneuriat…", "E.g. career guidance, CVs, entrepreneurship…"))
            + field("message", t("Pourquoi souhaites-tu devenir mentor ?", "Why do you want to become a mentor?"), "textarea"))
        return form(t, t("Candidature mentor", "Mentor application"), common + extra, t("Envoyer ma candidature", "Send my application"))
    extra = (field("missions", t("Missions qui t’intéressent", "Roles you’re interested in"), "select", options=[
        t("Événements", "Events"), t("Ateliers", "Workshops"), t("Communication", "Communications"), t("Administratif", "Admin"), t("Autre", "Other")])
        + field("message", t("Parle-nous de toi", "Tell us about yourself"), "textarea", required=False))
    return form(t, t("Candidature bénévole", "Volunteer application"), common + extra, t("Envoyer ma candidature", "Send my application"))


@page("adherer",
      lambda t: t("Adhérer", "Join"),
      lambda t: t("Adhérez à Youthaid Academy : jeunes, parents, membres et organisations, rejoignez la communauté.",
                  "Join Youthaid Academy: young people, parents, members and organisations, join the community."))
def join(t):
    intro = page_hero(t("Adhérer", "Join"), t("Rejoins la communauté Youthaid", "Join the Youthaid community"),
                      t("Adhésion individuelle, familiale, institutionnelle ou bénévole : choisis la formule qui te correspond.",
                        "Individual, family, institutional or volunteer membership: choose what suits you."))
    types = section(cards([
        dict(ic="spark", title=t("Jeune", "Young person"), text=t("Accès au mentorat, aux formations, aux opportunités et aux événements.", "Access to mentoring, courses, opportunities and events.")),
        dict(ic="heart", title=t("Famille", "Family"), text=t("Plusieurs profils rattachés à une même adhésion, avec suivi par le parent.", "Several profiles under one membership, with parent follow-up.")),
        dict(ic="users", title=t("Membre adhérent", "Supporting member"), text=t("Soutenez l’association et participez à sa vie et à ses décisions.", "Support the association and take part in its life and decisions.")),
        dict(ic="building", title=t("Organisation", "Organisation"), text=t("Pour les structures qui veulent s’engager durablement à nos côtés.", "For organisations wishing to commit long-term alongside us.")),
    ], cols=4), head=(t("Les formules", "Membership types"), t("Une adhésion pour chacun", "Membership for everyone")))
    body = section(two_col(
        f"<div><h2>{t('Ce que tu reçois', 'What you get')}</h2>" + checklist([
            t("Ta carte de membre", "Your membership card"), t("Un accès à ton espace personnel", "Access to your personal space"),
            t("Les invitations à nos événements", "Invitations to our events"), t("Les communications réservées aux membres", "Members-only updates"),
        ]) + '<div class="notice">' + t("<strong>Bon à savoir :</strong> l’adhésion et le paiement en ligne arrivent bientôt. En attendant, envoie-nous ta demande avec ce formulaire.",
                                         "<strong>Good to know:</strong> online membership and payment are coming soon. In the meantime, send us your request using this form.") + "</div></div>",
        _signup_page(t, "adherer")), cls="section-soft")
    return intro + types + body


@page("devenir-mentor",
      lambda t: t("Devenir mentor", "Become a mentor"),
      lambda t: t("Devenez mentor chez Youthaid Academy : partagez votre expérience et accompagnez un jeune vers la réussite.",
                  "Become a Youthaid Academy mentor: share your experience and help a young person succeed."))
def become_mentor(t):
    intro = page_hero(t("Devenir mentor", "Become a mentor"), t("Transmettez, inspirez, ouvrez des portes", "Share, inspire, open doors"),
                      t("Quelques heures par mois suffisent pour changer la trajectoire d’un jeune.", "A few hours a month is enough to change a young person’s path."))
    body = section(two_col(
        f"<div><h2>{t('Le rôle du mentor', 'The mentor’s role')}</h2>" + checklist([
            t("Écouter le jeune et l’aider à clarifier son projet", "Listen and help the young person clarify their project"),
            t("Partager son expérience et ses conseils", "Share experience and advice"),
            t("Ouvrir son réseau quand c’est utile", "Open up your network when helpful"),
            t("Planifier des échanges réguliers et suivre la relation", "Plan regular meetings and follow the relationship"),
        ]) + f"<h3>{t('Ce que nous vous apportons', 'What we provide')}</h3>" + checklist([
            t("Un binôme choisi selon vos compétences et vos disponibilités", "A mentee matched to your skills and availability"),
            t("Des ressources et un accompagnement par nos coordinateurs", "Resources and support from our coordinators"),
            t("Une communauté de mentors engagés", "A community of committed mentors"),
        ]) + "</div>", _signup_page(t, "mentor")), cls="section-soft")
    return intro + body


@page("devenir-benevole",
      lambda t: t("Devenir bénévole", "Volunteer"),
      lambda t: t("Devenez bénévole chez Youthaid Academy : événements, ateliers, communication… mettez votre énergie au service des jeunes.",
                  "Volunteer with Youthaid Academy: events, workshops, communications… put your energy to work for young people."),
      accent="var(--sun)")
def become_volunteer(t):
    intro = page_hero(t("Devenir bénévole", "Volunteer"), t("Votre énergie compte", "Your energy matters"),
                      t("Rejoignez l’équipe de bénévoles qui fait vivre Youthaid Academy au quotidien.", "Join the volunteer team that brings Youthaid Academy to life every day."), accent="var(--sun)")
    body = section(two_col(
        f"<div><h2>{t('Les missions', 'Roles')}</h2>" + checklist([
            t("Organiser et animer des événements", "Organise and run events"),
            t("Animer des ateliers pour les jeunes", "Lead workshops for young people"),
            t("Aider à la communication et aux réseaux sociaux", "Help with communications and social media"),
            t("Soutenir l’équipe dans l’accueil et l’administratif", "Support the team with welcome and admin tasks"),
        ]) + f"<p>{t('Vous choisissez vos missions et votre rythme. Chaque heure donnée compte.', 'You choose your roles and your pace. Every hour given counts.')}</p></div>",
        _signup_page(t, "benevole")), cls="section-soft")
    return intro + body


# =====================================================================
# ACTUALITÉS, FAQ, CONTACT
# =====================================================================
@page("actualites",
      lambda t: t("Actualités", "News"),
      lambda t: t("Les actualités de Youthaid Academy : lancements, programmes, événements et vie de la fondation.",
                  "Youthaid Academy news: launches, programmes, events and foundation life."))
def news(t):
    intro = page_hero(t("Blog / Actualités", "Blog / News"), t("Les nouvelles de Youthaid", "News from Youthaid"),
                      t("Lancements, programmes, événements et histoires de notre communauté.", "Launches, programmes, events and stories from our community."))
    article = section(f"""<article class="prose" id="lancement">
  <p class="meta" style="color:var(--muted)">19/11/2026 · {t("Vie de la fondation", "Foundation news")}</p>
  <h2 style="margin-top:0">{t("Youthaid Academy lance son site internet", "Youthaid Academy launches its website")}</h2>
  <p>{t("Nous sommes heureux de vous présenter le site de Youthaid Academy. Vous y découvrirez notre mission, nos programmes et toutes les façons de rejoindre l’aventure : adhérer, devenir mentor ou bénévole, devenir partenaire ou faire un don.",
        "We’re delighted to introduce the Youthaid Academy website. Here you’ll discover our mission, our programmes and all the ways to join the adventure: become a member, mentor or volunteer, partner with us or donate.")}</p>
  <p>{t("Ce site est la première étape d’une plateforme plus complète : espace membre, mise en relation avec des mentors, formations en ligne, opportunités et événements arriveront progressivement.",
        "This website is the first step towards a more complete platform: member area, mentor matching, online courses, opportunities and events will arrive step by step.")}</p>
  <p>{t("Restez connectés, et n’hésitez pas à nous écrire !", "Stay tuned, and feel free to get in touch!")}</p>
  {btns(btn("contact.html", t("Nous écrire", "Write to us"), "outline"))}
</article>""")
    follow = section(f"""<div class="follow-band">
  <div><h2>{t("Suivez Youthaid Academy", "Follow Youthaid Academy")}</h2>
  <p>{t("Nos dernières actualités, programmes et opportunités sont aussi partagés sur nos réseaux officiels.",
        "Our latest news, programmes and opportunities are also shared on our official channels.")}</p></div>
  {social_links(t, "socials socials-lg")}
</div>""", cls="section-soft")
    return intro + article + follow


@page("faq",
      lambda t: "FAQ",
      lambda t: t("Questions fréquentes sur Youthaid Academy : mentorat, adhésion, formations, dons et données personnelles.",
                  "Frequently asked questions about Youthaid Academy: mentoring, membership, training, donations and personal data."),
      nav=lambda t: t("FAQ", "FAQ"))
def faq_page(t):
    intro = page_hero("FAQ", t("Questions fréquentes", "Frequently asked questions"),
                      t("Vous ne trouvez pas votre réponse ? Écrivez-nous.", "Can’t find your answer? Write to us."))
    qs = [
        (t("Qui peut bénéficier de Youthaid Academy ?", "Who can benefit from Youthaid Academy?"),
         t("Les jeunes, en priorité issus de milieux défavorisés, qui souhaitent être accompagnés dans leur réussite scolaire, professionnelle ou entrepreneuriale.",
           "Young people, especially from disadvantaged backgrounds, who want support towards academic, professional or entrepreneurial success.")),
        (t("Le mentorat est-il payant pour les jeunes ?", "Is mentoring paid for young people?"),
         t("Nos mentors sont des bénévoles. Les conditions d’accès à chaque programme sont précisées lors de l’inscription.",
           "Our mentors are volunteers. Access conditions for each programme are set out when you sign up.")),
        (t("Comment est choisi mon mentor ?", "How is my mentor chosen?"),
         t("Selon tes besoins, ton projet, tes disponibilités et les compétences du mentor. Chaque mise en relation est validée par un coordinateur.",
           "Based on your needs, project, availability and the mentor’s skills. Every match is approved by a coordinator.")),
        (t("Faut-il des compétences particulières pour devenir mentor ?", "Do I need special skills to be a mentor?"),
         t("Il faut surtout de l’écoute, de la bienveillance et un peu de temps. Votre expérience professionnelle, quelle qu’elle soit, a de la valeur.",
           "Mostly listening, kindness and a little time. Your professional experience, whatever it is, is valuable.")),
        (t("Quand ouvrent les formations en ligne ?", "When do the online courses open?"),
         t("Le catalogue Youthaid Academy’s Compétences ouvrira progressivement. Inscris-toi pour être prévenu.",
           "The Youthaid Academy’s Compétences catalogue will open step by step. Sign up to be notified.")),
        (t("Comment faire un don ?", "How can I donate?"),
         t("Le don en ligne arrive bientôt. En attendant, contactez-nous via la page Contact.", "Online giving is coming soon. In the meantime, contact us via the Contact page.")),
        (t("Comment sont protégées mes données ?", "How is my data protected?"),
         t("Nous ne collectons que les données nécessaires et ne les vendons jamais. Consultez notre politique de confidentialité pour en savoir plus.",
           "We only collect the data we need and never sell it. See our privacy policy for details.")),
        (t("Le site est-il disponible en anglais ?", "Is the site available in English?"),
         t("Oui ! Utilisez le bouton EN / FR en haut de chaque page.", "Yes! Use the EN / FR button at the top of every page.")),
    ]
    return intro + section(faq(qs) + btns(btn("contact.html", t("Poser une question", "Ask a question"))))


@page("contact",
      lambda t: t("Contact", "Contact"),
      lambda t: t("Contactez Youthaid Academy : questions, partenariats, dons, témoignages.",
                  "Contact Youthaid Academy: questions, partnerships, donations, stories."))
def contact(t):
    intro = page_hero(t("Contact", "Contact"), t("Parlons-en", "Let’s talk"),
                      t("Une question, une idée de partenariat, envie de donner ou de témoigner ? Écrivez-nous.",
                        "A question, a partnership idea, want to donate or share your story? Write to us."))
    f = form(t, t("Message depuis le site Youthaid Academy", "Message from the Youthaid Academy website"),
             row(field("prenom", t("Prénom", "First name")), field("nom", t("Nom", "Last name")))
             + row(field("email", "Email", "email"), field("sujet", t("Sujet", "Subject"), "select", options=[
                 t("Question générale", "General question"), t("Mentorat", "Mentoring"), t("Partenariat", "Partnership"),
                 t("Don", "Donation"), t("Témoignage", "Story"), t("Presse", "Press"), t("Autre", "Other")]))
             + field("message", "Message", "textarea"),
             t("Envoyer", "Send"))
    phone = (f'<li><span class="ci-icon">{icon("chat", 20)}</span><div><span class="ci-label">{t("Téléphone", "Phone")}</span>'
             f'<a href="{phone_href(ORG_PHONE)}">{ORG_PHONE}</a></div></li>' if ORG_PHONE else "")
    offices = "".join(
        f'<li><span class="ci-icon">{icon("globe", 20)}</span><div><span class="ci-label">{t("Bureau", "Office")} · {o["city"]}</span>'
        f'<span>{office_line(o, t)}</span></div></li>' for o in OFFICES)
    side = f"""<div class="contact-side">
  <h2>{t("Nos coordonnées", "Our details")}</h2>
  <p>{t("Une question, un projet de partenariat, une demande presse ? Notre équipe vous répond en français et en anglais, dans les meilleurs délais.",
        "A question, a partnership project, a press request? Our team replies in French and English as soon as possible.")}</p>
  <ul class="contact-info card">
    <li><span class="ci-icon">{icon("mail", 20)}</span><div><span class="ci-label">Email</span><a href="mailto:{ORG_EMAIL}">{ORG_EMAIL}</a></div></li>
    {phone}
    {offices}
  </ul>
  <h3>{t("Suivez-nous", "Follow us")}</h3>
  <p class="muted">{t("Actualités, programmes et opportunités : rejoignez la communauté sur nos réseaux officiels.",
                      "News, programmes and opportunities: join the community on our official channels.")}</p>
  {social_links(t, "socials socials-lg")}
</div>"""
    return intro + section(two_col(side, f), cls="section-soft")


# =====================================================================
# ESPACE MEMBRE (à venir)
# =====================================================================
@page("espace-membre",
      lambda t: t("Espace membre", "Member area"),
      lambda t: t("L’espace membre Youthaid Academy : profil, adhésion, formations, mentorat, opportunités et événements.",
                  "The Youthaid Academy member area: profile, membership, courses, mentoring, opportunities and events."))
def member(t):
    intro = page_hero(t("Espace membre", "Member area"), t("Ton espace personnel arrive bientôt", "Your personal space is coming soon"),
                      t("Un tableau de bord sécurisé, adapté à ton rôle : jeune, mentor, bénévole, parent, partenaire ou formateur.",
                        "A secure dashboard tailored to your role: young person, mentor, volunteer, parent, partner or trainer."),
                      buttons=btns(btn("adherer.html", t("Être prévenu de l’ouverture", "Get notified at launch"))))
    mods = [("users", t("Mon profil", "My profile")), ("target", t("Mon tableau de bord", "My dashboard")), ("star", t("Mon adhésion", "My membership")),
            ("book", t("Mes documents", "My documents")), ("heart", t("Mes paiements", "My payments")), ("cap", t("Mes formations", "My courses")),
            ("chat", t("Mon mentorat", "My mentoring")), ("briefcase", t("Mes opportunités", "My opportunities")), ("calendar", t("Mes événements", "My events")),
            ("mail", t("Mes messages", "My messages")), ("building", t("Mon organisation / famille", "My organisation / family")), ("shield", t("Assistance", "Support"))]
    tiles = '<div class="grid grid-4">' + "".join(
        f'<div class="card" style="flex-direction:row;align-items:center;gap:12px;padding:18px"><div class="icon {["c-teal","c-sun","c-red","c-orange"][i % 4]}" style="margin:0;width:44px;height:44px">{icon(ic)}</div><strong style="color:var(--ink)">{lbl}</strong></div>'
        for i, (ic, lbl) in enumerate(mods)) + "</div>"
    return intro + section(tiles, head=(t("Au programme", "What’s inside"), t("Tout ton parcours, au même endroit", "Your whole journey, in one place")))


# =====================================================================
# PAGES LÉGALES
# =====================================================================
def legal(t, eyebrow, title, html_fr, html_en):
    return page_hero(eyebrow, title, t("Dernière mise à jour : 19 novembre 2026", "Last updated: 19 November 2026")) + \
        section(f'<div class="prose">{t(html_fr, html_en)}</div>')


@page("mentions-legales",
      lambda t: t("Mentions légales", "Legal notice"),
      lambda t: t("Mentions légales du site youthaidacademy.org.", "Legal notice for youthaidacademy.org."))
def legal_notice(t):
    td = todo(t("à compléter", "to be completed"))
    tel_fr = f'<br>Téléphone : <a href="{phone_href(ORG_PHONE)}">{ORG_PHONE}</a>' if ORG_PHONE else ""
    tel_en = f'<br>Phone: <a href="{phone_href(ORG_PHONE)}">{ORG_PHONE}</a>' if ORG_PHONE else ""
    offices_fr = " · ".join(office_line(o, lambda fr, en: fr) for o in OFFICES)
    offices_en = " · ".join(office_line(o, lambda fr, en: en) for o in OFFICES)
    return legal(t, t("Informations légales", "Legal"), t("Mentions légales", "Legal notice"),
                 f"""<h2>Éditeur du site</h2>
<p>Youthaid Academy — {td}<br>Forme juridique : {td}<br>Siège social : {td}<br>Numéro RNA / SIREN : {td}<br>Directeur de la publication : {td}<br>Email : <a href="mailto:{ORG_EMAIL}">{ORG_EMAIL}</a>{tel_fr}<br>Implantations : {offices_fr}</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — github.com.<br>Le nom de domaine est géré par Hostinger International Ltd.</p>
<h2>Propriété intellectuelle</h2>
<p>L’ensemble des contenus de ce site (textes, logo, éléments graphiques) est la propriété de Youthaid Academy, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2>Responsabilité</h2>
<p>Youthaid Academy s’efforce de fournir des informations exactes et à jour, sans pouvoir garantir l’absence d’erreurs. Les liens vers d’autres sites n’engagent pas sa responsabilité.</p>""",
                 f"""<h2>Publisher</h2>
<p>Youthaid Academy — {td}<br>Legal form: {td}<br>Registered office: {td}<br>Registration number: {td}<br>Publication director: {td}<br>Email: <a href="mailto:{ORG_EMAIL}">{ORG_EMAIL}</a>{tel_en}<br>Offices: {offices_en}</p>
<h2>Hosting</h2>
<p>The site is hosted by GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA — github.com.<br>The domain name is managed by Hostinger International Ltd.</p>
<h2>Intellectual property</h2>
<p>All content on this site (text, logo, graphics) belongs to Youthaid Academy unless otherwise stated. Reproduction without permission is prohibited.</p>
<h2>Liability</h2>
<p>Youthaid Academy strives to provide accurate, up-to-date information but cannot guarantee it is error-free. Links to other sites are not its responsibility.</p>""")


@page("confidentialite",
      lambda t: t("Politique de confidentialité", "Privacy policy"),
      lambda t: t("Comment Youthaid Academy collecte, utilise et protège vos données personnelles.", "How Youthaid Academy collects, uses and protects your personal data."))
def privacy(t):
    return legal(t, t("Données personnelles", "Personal data"), t("Politique de confidentialité", "Privacy policy"),
                 """<p>Youthaid Academy accorde une grande importance à la protection de vos données personnelles, en particulier celles des jeunes que nous accompagnons. Cette politique explique quelles données nous collectons, pourquoi et quels sont vos droits, conformément au Règlement général sur la protection des données (RGPD).</p>
<h2>Données collectées</h2>
<p>Via les formulaires du site (contact, adhésion, mentor, bénévole) : nom, prénom, email, ville et les informations que vous choisissez de nous transmettre. Les formulaires ouvrent votre messagerie : les données nous parviennent uniquement par l’email que vous envoyez.</p>
<h2>Finalités</h2>
<ul><li>Répondre à vos demandes ;</li><li>Traiter les adhésions et candidatures (mentors, bénévoles) ;</li><li>Organiser l’accompagnement et les mises en relation ;</li><li>Vous informer de nos actions, si vous l’avez accepté.</li></ul>
<h2>Base légale</h2>
<p>Votre consentement et, pour les adhésions, l’exécution de la relation avec l’association.</p>
<h2>Destinataires et durée</h2>
<p>Vos données sont réservées à l’équipe de Youthaid Academy et ne sont jamais vendues. Elles sont conservées le temps nécessaire au traitement de votre demande, puis au maximum 3 ans après notre dernier échange.</p>
<h2>Mineurs</h2>
<p>Pour les jeunes de moins de 15 ans, l’accord d’un parent ou représentant légal est nécessaire.</p>
<h2>Vos droits</h2>
<p>Vous disposez d’un droit d’accès, de rectification, d’effacement, de limitation, d’opposition et de portabilité. Pour les exercer, écrivez-nous à <a href="mailto:contact@youthaidacademy.org">contact@youthaidacademy.org</a> ou via la <a href="contact.html">page Contact</a>. Vous pouvez aussi saisir la CNIL (cnil.fr).</p>
<h2>Cookies</h2>
<p>Voir notre <a href="cookies.html">politique de cookies</a>.</p>""",
                 """<p>Youthaid Academy cares deeply about protecting your personal data, especially that of the young people we support. This policy explains what data we collect, why, and your rights under the General Data Protection Regulation (GDPR).</p>
<h2>Data collected</h2>
<p>Through the site’s forms (contact, membership, mentor, volunteer): name, email, city and any information you choose to share. Forms open your email app: data reaches us only through the email you send.</p>
<h2>Purposes</h2>
<ul><li>Answering your requests;</li><li>Processing memberships and applications (mentors, volunteers);</li><li>Organising support and matches;</li><li>Keeping you informed of our work, if you agreed.</li></ul>
<h2>Legal basis</h2>
<p>Your consent and, for memberships, the performance of your relationship with the association.</p>
<h2>Recipients and retention</h2>
<p>Your data is only used by the Youthaid Academy team and is never sold. It is kept as long as needed to handle your request, then for at most 3 years after our last exchange.</p>
<h2>Minors</h2>
<p>For young people under 15, consent from a parent or legal guardian is required.</p>
<h2>Your rights</h2>
<p>You have the right to access, rectify, erase, restrict, object and port your data. To exercise them, email <a href="mailto:contact@youthaidacademy.org">contact@youthaidacademy.org</a> or use the <a href="contact.html">Contact page</a>. You may also contact the CNIL (cnil.fr).</p>
<h2>Cookies</h2>
<p>See our <a href="cookies.html">cookie policy</a>.</p>""")


@page("cgu",
      lambda t: t("Conditions générales d’utilisation", "Terms of use"),
      lambda t: t("Conditions générales d’utilisation du site Youthaid Academy.", "Terms of use of the Youthaid Academy website."),
      nav=lambda t: t("CGU", "Terms of use"))
def terms(t):
    return legal(t, t("Informations légales", "Legal"), t("Conditions générales d’utilisation", "Terms of use"),
                 """<h2>Objet</h2><p>Les présentes conditions encadrent l’utilisation du site youthaidacademy.org. En naviguant sur le site, vous les acceptez.</p>
<h2>Accès au site</h2><p>Le site est accessible gratuitement. Youthaid Academy peut en suspendre l’accès pour maintenance ou mise à jour.</p>
<h2>Utilisation</h2><p>Vous vous engagez à utiliser le site de façon loyale, à fournir des informations exactes dans les formulaires et à respecter les autres membres de la communauté.</p>
<h2>Espace membre</h2><p>Les conditions propres à l’espace membre (comptes, adhésions, paiements, formations) seront précisées lors de son ouverture.</p>
<h2>Propriété intellectuelle</h2><p>Les contenus du site sont protégés. Voir les <a href="mentions-legales.html">mentions légales</a>.</p>
<h2>Modification</h2><p>Youthaid Academy peut modifier ces conditions à tout moment ; la version en ligne fait foi.</p>
<h2>Droit applicable</h2><p>Les présentes conditions sont soumises au droit français.</p>""",
                 """<h2>Purpose</h2><p>These terms govern use of youthaidacademy.org. By browsing the site, you accept them.</p>
<h2>Access</h2><p>The site is free to access. Youthaid Academy may suspend access for maintenance or updates.</p>
<h2>Use</h2><p>You agree to use the site fairly, provide accurate information in forms and respect other community members.</p>
<h2>Member area</h2><p>Terms specific to the member area (accounts, memberships, payments, courses) will be set out when it opens.</p>
<h2>Intellectual property</h2><p>Site content is protected. See the <a href="mentions-legales.html">legal notice</a>.</p>
<h2>Changes</h2><p>Youthaid Academy may change these terms at any time; the online version prevails.</p>
<h2>Governing law</h2><p>These terms are governed by French law.</p>""")


@page("cookies",
      lambda t: t("Politique de cookies", "Cookie policy"),
      lambda t: t("Politique de cookies du site Youthaid Academy.", "Cookie policy of the Youthaid Academy website."),
      nav=lambda t: t("Cookies", "Cookies"))
def cookies(t):
    return legal(t, t("Données personnelles", "Personal data"), t("Politique de cookies", "Cookie policy"),
                 """<h2>Aucun cookie de suivi</h2><p>Le site youthaidacademy.org n’utilise aucun cookie publicitaire ni de mesure d’audience, et ne charge aucune police ou ressource depuis des services tiers. Aucun bandeau de consentement n’est donc nécessaire.</p>
<h2>Évolutions</h2><p>Si l’espace membre ou un outil de mesure d’audience venait à utiliser des cookies, cette page serait mise à jour et votre consentement vous serait demandé lorsque la loi l’exige.</p>""",
                 """<h2>No tracking cookies</h2><p>youthaidacademy.org uses no advertising or analytics cookies and loads no fonts or resources from third-party services. No consent banner is therefore needed.</p>
<h2>Changes</h2><p>If the member area or an analytics tool were to use cookies, this page would be updated and your consent requested where the law requires it.</p>""")


@page("404",
      lambda t: t("Page introuvable", "Page not found"),
      lambda t: t("Cette page n’existe pas.", "This page doesn’t exist."))
def not_found(t):
    return page_hero("404", t("Oups, cette page n’existe pas", "Oops, this page doesn’t exist"),
                     t("Elle a peut-être été déplacée. Utilisez la loupe ou revenez à l’accueil.", "It may have moved. Use the search or go back home."),
                     buttons=btns(btn("./", t("Retour à l’accueil", "Back to home"))))
