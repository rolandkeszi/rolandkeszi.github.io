"""Build education.html and hu/education.html from the list below.

Degrees are shown as text with the university's logo; the diplomas themselves
are not published because they carry personal data.

    python assets/make_education.py
"""
import html

from site_shell import write_page

# Newest first. Text pairs are (English, Hungarian).
DEGREES = [
    {
        "year": "2026", "logo": "pannon.png",
        "school": ("University of Pannonia, Faculty of Engineering", "Pannon Egyetem, Mérnöki Kar"),
        "degree": ("Data and Systems Scientist and Artificial Intelligence Solution Development Specialist",
                   "Mesterséges intelligencia megoldásokat fejlesztő adat- és rendszertudományi szakember"),
        "detail": ("Postgraduate specialist training programme · 2 semesters", "Szakirányú továbbképzés · 2 félév"),
    },
    {
        "year": "2006", "logo": "elte.png",
        "school": ("Eötvös Loránd University (ELTE)", "Eötvös Loránd Tudományegyetem (ELTE)"),
        "degree": ("PhD in Sociology", "Doktori (PhD) fokozat, szociológia"),
        "detail": ("Doctoral degree in the sociological sciences, awarded <em>cum laude</em>",
                   "Szociológiai tudományok, <em>cum laude</em> minősítéssel"),
    },
    {
        "year": "2003", "logo": "corvinus.svg",
        "school": ("Corvinus University of Budapest", "Budapesti Corvinus Egyetem"),
        "degree": ("Master of Business Administration (MBA)", "Master of Business Administration (MBA)"),
        "detail": ("Awarded by the Budapest University of Economic Sciences and Public Administration, now Corvinus University of Budapest",
                   "Kiállító: Budapesti Közgazdaságtudományi és Államigazgatási Egyetem, ma Budapesti Corvinus Egyetem"),
    },
    {
        "year": "1998", "logo": "elte.png",
        "school": ("Eötvös Loránd University (ELTE)", "Eötvös Loránd Tudományegyetem (ELTE)"),
        "degree": ("Master's degree in Sociology", "Egyetemi oklevél, szociológia"),
        "detail": ("Specialisations: research sociology; change management",
                   "Szakirányok: kutató szociológus; változásmenedzsment"),
    },
]

TEXT = {
    "en": {
        "title": "Education · Roland Keszi",
        "description": "University degrees of Roland Keszi: AI and data science specialist training (University of Pannonia), PhD and master's degree in sociology (ELTE), MBA (Corvinus University of Budapest).",
        "h1": "Education",
    },
    "hu": {
        "title": "Egyetemi tanulmányok · Keszi Roland",
        "description": "Keszi Roland egyetemi végzettségei: MI- és adattudományi szakirányú továbbképzés (Pannon Egyetem), szociológia PhD és egyetemi oklevél (ELTE), MBA (Budapesti Corvinus Egyetem).",
        "h1": "Egyetemi tanulmányok",
    },
}


def build(lang: str) -> None:
    t = TEXT[lang]
    i = 0 if lang == "en" else 1
    prefix = "" if lang == "en" else "../"
    items = []
    for d in DEGREES:
        items.append(
            f'      <article class="edu-item">\n'
            f'        <span class="logo-tile"><img src="{prefix}assets/img/logos/{d["logo"]}" alt="{html.escape(d["school"][i])} logo"></span>\n'
            f'        <div class="edu-text"><span class="badge">{d["year"]}</span>'
            f'<h2>{html.escape(d["degree"][i])}</h2>'
            f'<p class="edu-school">{html.escape(d["school"][i])}</p>'
            f'<p class="cert-meta">{d["detail"][i]}</p></div>\n'
            f'      </article>'
        )
    body = f"""    <section class="case-head cert-head">
      <h1>{t["h1"]}</h1>
    </section>

    <section class="edu-list">
{chr(10).join(items)}
    </section>"""
    write_page(lang, "education.html", t["title"], t["description"], "assets/img/logos/elte.png", body)


if __name__ == "__main__":
    for lang in TEXT:
        build(lang)
