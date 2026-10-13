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
        "school": ("University of Pannonia - Faculty of Engineering", "Pannon Egyetem - Mérnöki Kar"),
        "degree": ("Data and Systems Scientist and Artificial Intelligence Solution Development Specialist",
                   "Mesterséges intelligencia megoldásokat fejlesztő adat- és rendszertudományi szakember"),
        "detail": ("Postgraduate artificial intelligence specialist engineer programme", "Mesterséges intelligencia szakmérnök képzés"),
    },
    {
        "year": "2006", "logo": "elte.png",
        "school": ("Eötvös Loránd University", "Eötvös Loránd Tudományegyetem"),
        "degree": ("PhD in Sociology", "Doktori (PhD) fokozat, szociológia"),
        "detail": ("Sociological sciences, quantitative empirical sociology",
                   "Szociológiai tudományok, kvantitatív empirikus szociológia"),
    },
    {
        "year": "2003", "logo": "corvinus.svg",
        "school": ("Corvinus University - Corvinus Business School", "Budapesti Corvinus Egyetem - Corvinus Business School"),
        "degree": ("Master of Business Administration (MBA)", "Master of Business Administration (MBA)"),
        "detail": ("Awarded by the Budapest University of Economic Sciences and Public Administration, now Corvinus University of Budapest",
                   "Kiállító: Budapesti Közgazdaságtudományi és Államigazgatási Egyetem, ma Budapesti Corvinus Egyetem"),
    },
    {
        "year": "1998", "logo": "elte.png",
        "school": ("ELTE - Faculty of Social Sciences", "ELTE - Társadalomtudományi Kar"),
        "degree": ("Master's degree in Sociology", "Egyetemi mesterdiploma, szociológia"),
        "detail": ("Specialisations: research sociology; change management",
                   "Szakirányok: kutató szociológus; változásmenedzsment"),
    },
]

TEXT = {
    "en": {
        "title": "Education · Roland Keszi",
        "description": "University degrees of Roland Keszi: artificial intelligence specialist engineer programme (University of Pannonia - Faculty of Engineering), PhD in sociology (Eötvös Loránd University), master's degree in sociology (ELTE - Faculty of Social Sciences), MBA (Corvinus University - Corvinus Business School).",
        "h1": "Education",
    },
    "hu": {
        "title": "Végzettség · Keszi Roland",
        "description": "Keszi Roland egyetemi végzettségei: mesterséges intelligencia szakmérnök képzés (Pannon Egyetem - Mérnöki Kar), szociológia PhD (Eötvös Loránd Tudományegyetem) és egyetemi mesterdiploma (ELTE - Társadalomtudományi Kar), MBA (Budapesti Corvinus Egyetem - Corvinus Business School).",
        "h1": "Végzettség",
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
