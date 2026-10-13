"""Build certificates.html and hu/certificates.html from the list below.

Header and footer are copied from index.html and hu/index.html, so the
certificate pages always match the rest of the site. Certificate images live
in assets/img/certs/<img>.jpg, issuer logos in assets/img/logos/.

    python assets/make_certificates.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS_V = re.search(r"style\.css\?v=(\d+)", (ROOT / "index.html").read_text(encoding="utf-8")).group(1)
LINKEDIN = "https://www.linkedin.com/in/rolandkeszi/details/certifications/"
V = "https://coursera.org/verify/"

# Issuers in display order. A "programme" has a final certificate and its
# courses; anything else is a single certificate. Dates are ISO strings.
ISSUERS = [
    {
        "id": "google", "name": "Google", "logo": "google-wordmark.png",
        "items": [
            {
                "kind": "Professional Certificate", "title": "Google AI",
                "date": "2026-03-09", "img": "google-ai", "url": V + "professional-cert/FMXVYCSDFP76",
                "courses": [
                    ("AI Fundamentals", "2026-03-07", "google-ai-1", V + "DLLO454JEISM"),
                    ("AI for Brainstorming and Planning", "2026-03-08", "google-ai-2", V + "7SJSB12WP67Q"),
                    ("AI for Research and Insights", "2026-03-08", "google-ai-3", V + "ZWQSZMJ0EOZ2"),
                    ("AI for Writing and Communicating", "2026-03-08", "google-ai-4", V + "SGECLH1HD9XT"),
                    ("AI for Content Creation", "2026-03-08", "google-ai-5", V + "J1QJ36QDL2YV"),
                    ("AI for Data Analysis", "2026-03-09", "google-ai-6", V + "RIAMQVLHUGGZ"),
                    ("AI for App Building", "2026-03-09", "google-ai-7", V + "JOT8Z0POVX3I"),
                ],
            },
            {
                "kind": "Professional Certificate", "title": "Google Advanced Data Analytics",
                "date": "2023-12-20", "img": "google-advanced-data-analytics", "url": V + "professional-cert/38GDRKM2JHWF",
                "courses": [
                    ("Foundations of Data Science", "2023-12-18", "google-ada-1", V + "RW326JCRJ5EP"),
                    ("Get Started with Python", "2023-12-20", "google-ada-2", V + "7MY87X6RRTSE"),
                    ("Go Beyond the Numbers: Translate Data into Insights", "2023-12-18", "google-ada-3", V + "LNKPZ3TB4PCT"),
                    ("The Power of Statistics", "2023-12-18", "google-ada-4", V + "9ZUWWYH3JMF2"),
                    ("Regression Analysis: Simplify Complex Data Relationships", "2023-12-18", "google-ada-5", V + "9QDYF36WUBBA"),
                    ("The Nuts and Bolts of Machine Learning", "2023-12-18", "google-ada-6", V + "LLBYU7SN5WDD"),
                    ("Google Advanced Data Analytics Capstone", "2023-12-20", "google-ada-7", V + "P2S4UGP8GDPJ"),
                ],
            },
            {
                "kind": "Professional Certificate", "title": "Google Data Analytics",
                "date": "2023-07-21", "img": "google-data-analytics", "url": V + "professional-cert/A4CBEGZBMB9S",
                "courses": [
                    ("Foundations: Data, Data, Everywhere", "2023-06-02", "google-da-1", V + "VT83PRTKZLZB"),
                    ("Ask Questions to Make Data-Driven Decisions", "2023-07-18", "google-da-2", V + "RUBFJ2RKG4HF"),
                    ("Prepare Data for Exploration", "2023-07-18", "google-da-3", V + "JGP4V7L2X64C"),
                    ("Process Data from Dirty to Clean", "2023-07-20", "google-da-4", V + "29TCB4K4THNT"),
                    ("Analyze Data to Answer Questions", "2023-07-20", "google-da-5", V + "D9N6LMUV72B9"),
                    ("Share Data Through the Art of Visualization", "2023-07-21", "google-da-6", V + "ZDUUZ6DEGPK2"),
                    ("Data Analysis with R Programming", "2023-05-26", "google-da-7", V + "3V4S43JHJCA8"),
                    ("Google Data Analytics Capstone: Complete a Case Study", "2023-07-19", "google-da-8", V + "H3ZXLATX7B83"),
                ],
            },
            {"title": "Deploy a BigQuery ML Customer Churn Classifier to Vertex AI for Online Predictions",
             "by": "Google Cloud", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2023-08-15", "img": "google-cloud-bigquery-ml", "url": V + "ULBWUHGDU4Q5"},
            {"title": "Fundamentals of Digital Marketing",
             "by": "Google Digital Workshop", "platform": "IAB Europe · The Open University",
             "date": "2022-11-05", "img": "google-digital-marketing", "url": "https://learndigital.withgoogle.com/link/1gz8b5ztmv4"},
        ],
    },
    {
        "id": "ibm", "name": "IBM", "logo": "ibm.png",
        "items": [
            {
                "kind": "Professional Certificate", "title": "IBM Generative AI Engineering",
                "date": "2025-07-31", "img": "ibm-genai", "url": V + "professional-cert/J3HA302KSVZ9",
                "courses": [
                    ("Introduction to Artificial Intelligence (AI)", "2025-07-25", "ibm-genai-1", V + "AYG504LMG6J7"),
                    ("Generative AI: Introduction and Applications", "2025-07-25", "ibm-genai-2", V + "Z68ML1LFTVI5"),
                    ("Generative AI: Prompt Engineering Basics", "2025-07-25", "ibm-genai-3", V + "AC5DF5S9SR3G"),
                    ("Python for Data Science, AI & Development", "2025-07-26", "ibm-genai-4", V + "2GIAEBIYD4CT"),
                    ("Developing AI Applications with Python and Flask", "2025-07-31", "ibm-genai-5", V + "TPBT08SEK3EP"),
                    ("Building Generative AI-Powered Applications with Python", "2025-07-27", "ibm-genai-6", V + "3C91KIF8L7KJ"),
                    ("Data Analysis with Python", "2025-07-28", "ibm-genai-7", V + "FBUTKYILT4AA"),
                    ("Machine Learning with Python", "2025-07-27", "ibm-genai-8", V + "PEJW3GFS6OR9"),
                    ("Introduction to Deep Learning & Neural Networks with Keras", "2025-07-27", "ibm-genai-9", V + "OKZK4I0NOGZ0"),
                    ("Generative AI and LLMs: Architecture and Data Preparation", "2025-07-28", "ibm-genai-10", V + "5ZV6IIPBSLKM"),
                    ("Gen AI Foundational Models for NLP & Language Understanding", "2025-07-27", "ibm-genai-11", V + "ZPVRA6OS43ZB"),
                    ("Generative AI Language Modeling with Transformers", "2025-07-28", "ibm-genai-12", V + "3HX8L83J6JIW"),
                    ("Generative AI Engineering and Fine-Tuning Transformers", "2025-07-28", "ibm-genai-13", V + "X6JZ0RMKIZ6P"),
                    ("Generative AI Advanced Fine-Tuning for LLMs", "2025-07-28", "ibm-genai-14", V + "OQP9BZBYY4ZM"),
                    ("Fundamentals of AI Agents Using RAG and LangChain", "2025-07-29", "ibm-genai-15", V + "X77MZ3B1F222"),
                    ("Project: Generative AI Applications with RAG and LangChain", "2025-07-30", "ibm-genai-16", V + "3QV23I9Q8MYM"),
                ],
            },
            {"title": "Databases and SQL for Data Science with Python", "note": ("With honors", "Kitüntetéssel"),
             "platform": "Coursera", "date": "2023-03-05", "img": "ibm-databases-sql", "url": V + "KM9UCAAXDSGE"},
        ],
    },
    {
        "id": "microsoft", "name": "Microsoft", "logo": "microsoft.png",
        "items": [
            {
                "kind": "Professional Certificate", "title": "Microsoft Power BI Data Analyst",
                "date": "2025-07-13", "img": "microsoft-powerbi", "url": V + "professional-cert/H0NRM7U1YV7V",
                "courses": [
                    ("Preparing Data for Analysis with Microsoft Excel", "2025-07-11", "microsoft-powerbi-1", V + "PO41NTPS54A5"),
                    ("Harnessing the Power of Data with Power BI", "2025-07-11", "microsoft-powerbi-2", V + "KY3J0X5XN9HI"),
                    ("Extract, Transform and Load Data in Power BI", "2025-07-11", "microsoft-powerbi-3", V + "3HEVBCX5N7W6"),
                    ("Data Modeling in Power BI", "2025-07-11", "microsoft-powerbi-4", V + "BKMVLHPRE689"),
                    ("Data Analysis and Visualization with Power BI", "2025-07-11", "microsoft-powerbi-5", V + "SBQ4US50GL7Q"),
                    ("Creative Designing in Power BI", "2025-07-11", "microsoft-powerbi-6", V + "E7HMLKEI0MPM"),
                    ("Deploy and Maintain Power BI Assets and Capstone project", "2025-07-11", "microsoft-powerbi-7", V + "464IJS7P8SLE"),
                    ("Microsoft PL-300 Exam Preparation and Practice", "2025-07-13", "microsoft-powerbi-8", V + "IK8ESN9Z9ICL"),
                ],
            },
        ],
    },
    {
        "id": "stanford", "name": "Stanford University · DeepLearning.AI", "logo": "deeplearning-stanford.png",
        "items": [
            {
                "kind": "Specialization", "title": "Machine Learning",
                "date": "2024-01-23", "img": "stanford-machine-learning", "url": V + "specialization/G9RM6NED4VGU",
                "courses": [
                    ("Supervised Machine Learning: Regression and Classification", "2024-01-22", "stanford-ml-1", V + "W3AWCTQXEJBK"),
                    ("Advanced Learning Algorithms", "2024-01-23", "stanford-ml-2", V + "W3XD6D7BMN6G"),
                    ("Unsupervised Learning, Recommenders, Reinforcement Learning", "2024-01-23", "stanford-ml-3", V + "RFE2A2QAMB9R"),
                ],
            },
        ],
    },
    {
        "id": "deeplearning-ai", "name": "DeepLearning.AI", "logo": "deeplearning-ai.png",
        "items": [
            {
                "kind": "Specialization", "title": "Natural Language Processing",
                "date": "2025-07-20", "img": "dlai-nlp", "url": V + "specialization/5SJX32L99X19",
                "courses": [
                    ("Natural Language Processing with Classification and Vector Spaces", "2025-07-14", "dlai-nlp-1", V + "LRIK544GX36Q"),
                    ("Natural Language Processing with Probabilistic Models", "2025-07-17", "dlai-nlp-2", V + "LH57NJMXWH9S"),
                    ("Natural Language Processing with Sequence Models", "2025-07-18", "dlai-nlp-3", V + "CXGET8VYJO55"),
                    ("Natural Language Processing with Attention Models", "2025-07-20", "dlai-nlp-4", V + "WTZP7JYIXYBK"),
                ],
            },
        ],
    },
    {
        "id": "packt", "name": "Packt", "logo": "packt.png",
        "items": [
            {"title": "Applied Generative AI & NLP with Python", "platform": "Coursera",
             "date": "2025-05-22", "img": "packt-generative-ai-nlp", "url": V + "03WEQTRZRNF6"},
        ],
    },
    {
        "id": "skillsbooster", "name": "SkillsBooster Academy", "logo": "skillsbooster.png",
        "items": [
            {"title": "Claude Skills: Automating Business Workflows", "platform": "Coursera",
             "date": "2026-08-08", "img": "skillsbooster-claude-skills", "url": V + "LBV64ZF83FWE"},
        ],
    },
    {
        "id": "coursera-projects", "name": "Coursera Project Network", "logo": "coursera-project-network.png", "square": True,
        "items": [
            {"title": "ChatGPT for Beginners: Using AI for Market Research", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2025-07-10", "img": "coursera-ai-market-research", "url": V + "UE8YUOMHR6TF"},
            {"title": "NLP: Twitter Sentiment Analysis", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2025-06-18", "img": "coursera-twitter-sentiment", "url": V + "OOUBZ696CACX"},
            {"title": "Using Google Forms to Analyze User Research Data", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2025-06-12", "img": "coursera-google-forms", "url": V + "SGFJ6V0ZOJQP"},
            {"title": "Create an Employee Feedback Survey with TypeForm", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2025-06-10", "img": "coursera-typeform-survey", "url": V + "TAQVRU9HSIVK"},
            {"title": "Create surveys with Qualtrics", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2025-06-09", "img": "coursera-qualtrics-surveys", "url": V + "8LQXB1A9FYLI"},
            {"title": "Sentiment Analysis with Deep Learning using BERT", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2024-12-25", "img": "coursera-bert-sentiment", "url": V + "H0G6FQ1VXD82"},
            {"title": "Create Interactive Dashboards with Streamlit and Python", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2024-09-24", "img": "coursera-streamlit-dashboards", "url": V + "QYW6M7QXOALU"},
            {"title": "Facebook Network Analysis using Python and NetworkX", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2024-05-10", "img": "coursera-facebook-networkx", "url": V + "YZ3E348VVUXP"},
            {"title": "Basic Sentiment Analysis with TensorFlow", "type": ("Project", "Projekt"), "platform": "Coursera",
             "date": "2024-02-28", "img": "coursera-tensorflow-sentiment", "url": V + "8553VJ6HFHMU"},
        ],
    },
    {
        "id": "coursera-instructors", "name": "Coursera Instructor Network", "logo": "coursera-instructor-network.png",
        "items": [
            {"title": "Social Listening", "platform": "Coursera",
             "date": "2025-05-24", "img": "coursera-social-listening", "url": V + "BC6LSX0925E8"},
        ],
    },
]

MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "hu": ["január", "február", "március", "április", "május", "június", "július", "augusztus", "szeptember", "október", "november", "december"],
}

TEXT = {
    "en": {
        "src": "index.html", "out": "certificates.html",
        "title": "Certificates · Roland Keszi",
        "description": "Professional certificates of Roland Keszi in data analytics, machine learning and AI from Google, IBM, Microsoft, Stanford University, DeepLearning.AI and others.",
        "h1": "Certificates",
        "intro": [
            "I regard <strong>learning</strong>, and a lasting commitment to self-development, as a priority in every area of my life. In technology, and in AI in particular, I consider it indispensable.",
            "Below are some of my most important training programmes in artificial intelligence and data science.",
        ],
        "hint": "Click a certificate to enlarge it; the title links to the issuer's verification page.",
        "linkedin": "All certificates on LinkedIn",
        "courses": "courses", "course": "Course", "included": "Courses in this programme",
        "count": ("certificate", "certificates"),
        "enlarge": "Enlarge certificate", "close": "Close",
        "en_href": "certificates.html", "hu_href": "hu/certificates.html",
    },
    "hu": {
        "src": "hu/index.html", "out": "hu/certificates.html",
        "title": "Tanúsítványok · Keszi Roland",
        "description": "Keszi Roland adatelemzési, gépi tanulási és MI-tanúsítványai a Google-tól, az IBM-től, a Microsofttól, a Stanford Egyetemtől, a DeepLearning.AI-tól és másoktól.",
        "h1": "Tanúsítványok",
        "intro": [
            "Életem minden területén kiemelt jelentőségűként tekintek a <strong>tanulás</strong>, az állandó önképzés fenntartására, melyet a technológiai, illetve AI vonatkozású tevékenységekben elengedhetetlennek gondolok.",
            "Az alábbiakban a mesterséges intelligencia, illetve data science vonatkozású néhány fontosabb továbbképzésemet tüntetem fel.",
        ],
        "hint": "A képre kattintva a tanúsítvány nagyobb méretben nyílik meg, a cím a kiállító hitelesítő oldalára mutat.",
        "linkedin": "Összes tanúsítvány a LinkedIn-en",
        "courses": "kurzus", "course": "Kurzus", "included": "A program kurzusai",
        "count": ("tanúsítvány", "tanúsítvány"),
        "enlarge": "Tanúsítvány nagyítása", "close": "Bezárás",
        "en_href": "../certificates.html", "hu_href": "certificates.html",
    },
}


def month(iso: str, lang: str) -> str:
    y, m, _ = iso.split("-")
    name = MONTHS[lang][int(m) - 1]
    return f"{name} {y}" if lang == "en" else f"{y}. {name}"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def image_link(img: str, title: str, t: dict, prefix: str) -> str:
    src = f"{prefix}assets/img/certs/{img}.jpg"
    return (f'<a class="cert-img" href="{src}" aria-label="{esc(t["enlarge"])}: {esc(title)}">'
            f'<img src="{src}" alt="{esc(title)}" width="1000" height="773" loading="lazy"></a>')


def programme(p: dict, t: dict, lang: str, prefix: str) -> str:
    n = len(p["courses"])
    full = f'{p["title"]} {p["kind"]}'
    courses = []
    for k, (title, date, img, url) in enumerate(p["courses"], 1):
        courses.append(
            f'          <figure class="cert course">{image_link(img, title, t, prefix)}'
            f'<figcaption><span class="cert-meta">{t["course"]} {k} · {month(date, lang)}</span>'
            f'<a class="cert-title" href="{url}">{esc(title)}</a></figcaption></figure>'
        )
    return (
        f'      <article class="programme">\n'
        f'        <div class="programme-main">\n'
        f'          {image_link(p["img"], full, t, prefix)}\n'
        f'          <div class="programme-text"><span class="badge">{esc(p["kind"])}</span>'
        f'<h3><a href="{p["url"]}">{esc(full)}</a></h3>'
        f'<p class="cert-meta">{n} {t["courses"]} · Coursera · {month(p["date"], lang)}</p></div>\n'
        f'        </div>\n'
        f'        <p class="courses-label">{t["included"]}</p>\n'
        f'        <div class="course-grid">\n' + "\n".join(courses) + "\n        </div>\n"
        f'      </article>'
    )


def single(c: dict, t: dict, lang: str, prefix: str) -> str:
    i = 0 if lang == "en" else 1
    meta = [x for x in (c.get("by"), c["type"][i] if "type" in c else None, c.get("platform"),
                        c["note"][i] if "note" in c else None, month(c["date"], lang)) if x]
    return (
        f'        <figure class="cert">{image_link(c["img"], c["title"], t, prefix)}'
        f'<figcaption><a class="cert-title" href="{c["url"]}">{esc(c["title"])}</a>'
        f'<span class="cert-meta">{esc(" · ".join(meta))}</span></figcaption></figure>'
    )


def count(iss: dict) -> int:
    return sum(1 + len(x.get("courses", [])) for x in iss["items"])


def build(lang: str) -> None:
    t = TEXT[lang]
    page = (ROOT / t["src"]).read_text(encoding="utf-8")
    prefix = "" if lang == "en" else "../"

    header = re.search(r"<header class=\"top\">.*?</header>", page, re.S).group(0)
    header = header.replace('href="#projects"', 'href="./#projects"')
    header = header.replace('<a href="certificates.html">', '<a href="certificates.html" aria-current="page">')
    header = re.sub(r'(<a[^>]*?href=")[^"]*(" hreflang="en")', rf'\g<1>{t["en_href"]}\2', header)
    header = re.sub(r'(<a[^>]*?href=")[^"]*(" hreflang="hu")', rf'\g<1>{t["hu_href"]}\2', header)
    popovers = re.search(r'<div id="photo-large".*?</div>\s*<div id="about-info".*?</div>', page, re.S).group(0)
    footer = re.search(r"<footer>.*?</footer>", page, re.S).group(0)

    groups = []
    for iss in ISSUERS:
        progs = [programme(x, t, lang, prefix) for x in iss["items"] if "courses" in x]
        singles = [single(x, t, lang, prefix) for x in iss["items"] if "courses" not in x]
        n = count(iss)
        body = "\n".join(progs)
        if singles:
            body += ("\n" if body else "") + '      <div class="cert-grid">\n' + "\n".join(singles) + "\n      </div>"
        groups.append(
            f'    <section class="cert-group" id="{iss["id"]}">\n'
            f'      <div class="cert-issuer"><span class="logo-tile{' square' if iss.get('square') else ''}"><img src="{prefix}assets/img/logos/{iss["logo"]}" alt="{esc(iss["name"])} logo"></span>'
            f'<div><h2>{esc(iss["name"])}</h2><span class="cert-meta">{n} {t["count"][0 if n == 1 else 1]}</span></div></div>\n'
            f'{body}\n'
            f'    </section>'
        )

    intro = "\n".join(f'      <p class="lede">{para}</p>' for para in t["intro"])

    out = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t["title"]}</title>
  <meta name="description" content="{t["description"]}">
  <meta property="og:title" content="{t["title"]}">
  <meta property="og:description" content="{t["description"]}">
  <meta property="og:image" content="https://rolandkeszi.github.io/assets/img/certs/google-data-analytics.jpg">
  <link rel="alternate" hreflang="en" href="https://rolandkeszi.github.io/certificates.html">
  <link rel="alternate" hreflang="hu" href="https://rolandkeszi.github.io/hu/certificates.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/style.css?v={CSS_V}">
</head>
<body>
  {header}
  {popovers}
  <div id="cert-large" class="cert-pop" popover><button type="button" popovertarget="cert-large" popovertargetaction="hide" aria-label="{t["close"]}"><img alt=""></button></div>
  <div class="wrap">

    <section class="case-head cert-head">
      <h1>{t["h1"]}</h1>
{intro}
      <p class="cert-hint">{t["hint"]}</p>
      <a class="linkedin-all" href="{LINKEDIN}" target="_blank" rel="noopener">{t["linkedin"]} ↗</a>
    </section>

{chr(10).join(groups)}

    {footer}
  </div>
  <script>
    // Open a certificate image in the popover instead of leaving the page.
    const pop = document.getElementById("cert-large"), big = pop.querySelector("img");
    document.querySelectorAll(".cert-img").forEach(a => a.addEventListener("click", e => {{
      if (!pop.showPopover) return;
      e.preventDefault();
      big.src = a.getAttribute("href");
      big.alt = a.querySelector("img").alt;
      pop.showPopover();
    }}));
  </script>
</body>
</html>
"""
    (ROOT / t["out"]).write_text(out, encoding="utf-8", newline="\n")
    print("wrote", t["out"])


if __name__ == "__main__":
    for lang in TEXT:
        build(lang)
