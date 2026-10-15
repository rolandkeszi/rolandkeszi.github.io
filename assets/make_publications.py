"""Build publications.html and hu/publications.html.

The page links out to the two databases that hold the full, up-to-date
publication list (Google Scholar and MTMT) instead of copying the list here.

    python assets/make_publications.py
"""
from site_shell import write_page

SCHOLAR_ID = "gKmgHogAAAAJ"
MTMT_ID = "10012594"

TEXT = {
    "en": {
        "title": "Publications · Roland Keszi",
        "description": "Publications of Roland Keszi: the full, up-to-date list on Google Scholar and in MTMT, the Hungarian Scientific Bibliography.",
        "h1": "Publications",
        "lede": "My publications are listed in two databases. Click a banner to open the full, up-to-date list in a new window.",
        "cta": "Open the list",
        "scholar_name": "Scholar",
        "scholar": "Publications, citations and h-index",
        "mtmt_name": "Magyar Tudományos Művek Tára (MTMT)",
        "mtmt": "Data verified by the Hungarian Academy of Sciences",
        "new_window": "opens in a new window",
    },
    "hu": {
        "title": "Publikációk · Keszi Roland",
        "description": "Keszi Roland publikációi: a teljes, naprakész lista a Google Tudós (Google Scholar) oldalán és a Magyar Tudományos Művek Tárában (MTMT).",
        "h1": "Publikációk",
        "lede": "Publikációim két adatbázisban érhetők el. A bannerre kattintva új ablakban nyílik meg a teljes, naprakész lista.",
        "cta": "A lista megnyitása",
        "scholar_name": "Tudós",
        "scholar": "Publikációk, hivatkozások és h-index",
        "mtmt_name": "Magyar Tudományos Művek Tára (MTMT)",
        "mtmt": "A Magyar Tudományos Akadémia által hitelesített adatok",
        "new_window": "új ablakban nyílik meg",
    },
}


def banner(kind: str, href: str, logo: str, name: str, desc: str, t: dict, deco: str = "", name_html: str = "") -> str:
    return (
        f'      <a class="pub-banner pub-{kind}" href="{href}" target="_blank" rel="noopener" '
        f'aria-label="{name}: {desc} ({t["new_window"]})">\n'
        f'        <span class="pub-logo"><img src="{logo}" alt="" width="72" height="72"></span>\n'
        f'        <span class="pub-text"><span class="pub-name">{name_html or name}</span>'
        f'<span class="pub-desc">{desc}</span>'
        f'<span class="pub-cta">{t["cta"]} ↗</span></span>\n'
        f'{deco}'
        f'      </a>'
    )


def build(lang: str) -> None:
    t = TEXT[lang]
    prefix = "" if lang == "en" else "../"
    scholar_logo = f"{prefix}assets/img/logos/google-scholar.svg"
    scholar = banner(
        "scholar", f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl={lang}",
        scholar_logo, f"Google {t['scholar_name']}", t["scholar"], t,
        f'        <img class="pub-deco" src="{scholar_logo}" alt="" aria-hidden="true">\n',
        f'<span class="pub-wordmark"><img src="{prefix}assets/img/logos/google.svg" alt="Google" width="118" height="40">'
        f'<span>{t["scholar_name"]}</span></span>',
    )
    mtmt = banner(
        "mtmt", f"https://m2.mtmt.hu/gui2/?type=authors&mode=browse&sel={MTMT_ID}&view=simpleList",
        f"{prefix}assets/img/logos/mtmt.svg", t["mtmt_name"], t["mtmt"], t,
        '        <span class="pub-deco pub-deco-text" aria-hidden="true">mt<br>mt</span>\n',
        '<span class="pub-mtmt-word" lang="hu">Magyar Tudományos<br>Művek Tára</span>',
    )
    body = f"""    <section class="case-head cert-head">
      <h1>{t["h1"]}</h1>
      <p class="lede">{t["lede"]}</p>
    </section>

    <section class="pub-banners">
{scholar}
{mtmt}
    </section>"""
    write_page(lang, "publications.html", t["title"], t["description"], "assets/img/avatar-large.jpg", body)


if __name__ == "__main__":
    for lang in TEXT:
        build(lang)
