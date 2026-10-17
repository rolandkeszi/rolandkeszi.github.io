"""Build about.html and hu/about.html.

    python assets/make_about.py
"""
from site_shell import write_page

TEXT = {
    "en": {
        "title": "About · Roland Keszi",
        "description": "Roland Keszi explains, interprets and forecasts real-world phenomena, drawing on artificial intelligence engineering, MBA business and leadership studies, empirical research sociology and change management, and decades of professional experience.",
        "h1": "About",
        "name": "Roland Keszi",
        "role": "AI &amp; Data Science",
        "lead": "I seek to explain, understand and predict the phenomena of the world around us. My work builds on the expert knowledge I gained in a postgraduate <strong>artificial intelligence specialist engineer</strong> programme at a faculty of engineering, the business and leadership knowledge of a <strong>Master of Business Administration</strong> programme at a university of economics, and further specialised studies at a faculty of social sciences in <strong>empirical research sociology</strong> and <strong>change management</strong>, and it is backed by decades of professional experience.",
        "body": "On these pages I share selected excerpts from some of my projects in artificial intelligence and data science.",
        "links": [("./#projects", "Projects"), ("education.html", "Education"), ("certificates.html", "Certificates"),
                  ("https://keszi.krolify.hu/", "Pages for higher education ↗")],
    },
    "hu": {
        "title": "Rólam · Keszi Roland",
        "description": "Keszi Roland a minket körülvevő világ jelenségeit igyekszik magyarázni, megérteni és előre jelezni mesterséges intelligencia szakmérnöki, MBA, empirikus kutató szociológus és változásmenedzser tanulmányaira és több évtizedes szakmai tapasztalatára építve.",
        "h1": "Rólam",
        "name": "Keszi Roland",
        "role": "Mesterséges intelligencia és adattudomány",
        "lead": "A minket körülvevő világ jelenségeit igyekszem magyarázni, megérteni és előre jelezni mérnöki kar, <strong>mesterséges intelligencia szakmérnöki</strong> képzésén szerzett szakértői, közgazdaságtudományi egyetem <strong>Master of Business Administration</strong> képzésen szerzett üzleti és vezetői, valamint társadalomtudományi kar, <strong>empirikus kutató szociológus</strong>, valamint <strong>változásmenedzser</strong> szakirányain szerzett szakirányú többlet tanulmányaimmal megalapozva és több évtizedes szakmai tapasztalataimmal alátámasztva.",
        "body": "Ezeken az oldalakon a mesterséges intelligencia és data science területeiről közlök néhány projektemből szemelvényeket.",
        "links": [("./#projects", "Projektek"), ("education.html", "Végzettség"), ("certificates.html", "Tanúsítványok"),
                  ("https://keszi.krolify.hu/", "Felsőoktatási oldalaim ↗")],
    },
}


def build(lang: str) -> None:
    t = TEXT[lang]
    links = "".join(f'<a href="{href}">{label}</a>' for href, label in t["links"])
    body = f"""    <section class="case-head about-head">
      <h1>{t["h1"]}</h1>
      <p class="about-name">{t["name"]} <span>· {t["role"]}</span></p>
    </section>

    <article class="about-text">
      <p class="about-lead">{t["lead"]}</p>
      <p>{t["body"]}</p>
      <nav class="about-links">{links}</nav>
    </article>"""
    write_page(lang, "about.html", t["title"], t["description"], "assets/img/avatar-large.jpg", body)


if __name__ == "__main__":
    for lang in TEXT:
        build(lang)
