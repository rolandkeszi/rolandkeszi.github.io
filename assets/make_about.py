"""Build about.html and hu/about.html.

    python assets/make_about.py
"""
from site_shell import write_page

# Photos at the end of the page, left to right: (file, width, height, English alt, Hungarian alt).
# Copies in assets/img/about/ are re-saved without any metadata.
PHOTOS = [
    ("zoe-1.jpg", 443, 590, "Roland holding Zoé, his Labrador, as a puppy", "Roland a kölyökkutya Zoéval, a labradorjával"),
    ("zoe-3.jpg", 684, 912, "Zoé smiling into the camera", "Zoé mosolyog a kamerába"),
    ("zoe-2.jpg", 443, 590, "Roland carrying Zoé, now fully grown", "Roland a már felnőtt Zoéval a karjában"),
]

TEXT = {
    "en": {
        "title": "About · Roland Keszi",
        "description": "Roland Keszi explains, interprets and forecasts real-world phenomena, drawing on artificial intelligence engineering, MBA business and leadership studies, empirical research sociology and change management, and decades of professional experience.",
        "h1": "About",
        "name": "Roland Keszi",
        "role": "AI &amp; Data Science",
        "lead": "I seek to explain, understand and predict the phenomena of the world around us. My work builds on the expert knowledge I gained in a postgraduate <a href='education.html'><strong>artificial intelligence specialist engineer</strong></a> programme at a faculty of engineering, the business and leadership knowledge of a <a href='education.html'><strong>Master of Business Administration</strong></a> programme at a university of economics, and further specialised studies at a faculty of social sciences in <a href='education.html'><strong>empirical research sociology</strong></a> and <a href='education.html'><strong>change management</strong></a>, and it is backed by decades of professional experience. I keep my knowledge up to date through regular <a href='certificates.html'><strong>further training</strong></a>.",
        "body": "On these pages I share selected excerpts from some of my projects in artificial intelligence and data science.",
        "photos_caption": "My furry child taught me to understand the most important law of the world, the law of change, as illustrated by the visualisation (a fleeting group of phenomena) of unstructured data sets (pixels) below. 😊",
        "enlarge": "Enlarge",
        "close": "Close",
        "links": [("./#projects", "Projects"), ("education.html", "Education"), ("certificates.html", "Certificates"),
                  ("https://keszi.krolify.hu/", "Pages for higher education ↗")],
    },
    "hu": {
        "title": "Rólam · Keszi Roland",
        "description": "Keszi Roland a minket körülvevő világ jelenségeit igyekszik magyarázni, megérteni és előre jelezni mesterséges intelligencia szakmérnöki, MBA, empirikus kutató szociológus és változásmenedzser tanulmányaira és több évtizedes szakmai tapasztalatára építve.",
        "h1": "Rólam",
        "name": "Keszi Roland",
        "role": "Mesterséges intelligencia és adattudomány",
        "lead": "A minket körülvevő világ jelenségeit igyekszem magyarázni, megérteni és előre jelezni mérnöki kar, <a href='education.html'><strong>mesterséges intelligencia szakmérnöki</strong></a> képzésén szerzett szakértői, közgazdaságtudományi egyetem <a href='education.html'><strong>Master of Business Administration</strong></a> képzésen szerzett üzleti és vezetői, társadalomtudományi kar, <a href='education.html'><strong>empirikus kutató szociológus</strong></a>, valamint <a href='education.html'><strong>változásmenedzser</strong></a> szakirányain szerzett szakirányú többlet tanulmányaimmal megalapozva és több évtizedes szakmai tapasztalataimmal alátámasztva. Ismereteimet rendszeres <a href='certificates.html'><strong>továbbképzésekkel</strong></a> igyekszem naprakészen tartani.",
        "body": "Ezeken az oldalakon a mesterséges intelligencia és data science területeiről közlök néhány projektemből szemelvényeket.",
        "photos_caption": "A legjelentősebb világtörvénynek, a változás törvényének megértésére szőrös gyermekem tanított meg, melyet az alábbi strukturálatlan adathalmazokat (pixel) tartalmazó vizualizáció (tünékeny jelenségcsoport) szemléltet. 😊",
        "enlarge": "Nagyítás",
        "close": "Bezárás",
        "links": [("./#projects", "Projektek"), ("education.html", "Végzettség"), ("certificates.html", "Tanúsítványok"),
                  ("https://keszi.krolify.hu/", "Felsőoktatási oldalaim ↗")],
    },
}


def build(lang: str) -> None:
    t = TEXT[lang]
    i = 0 if lang == "en" else 1
    img = ("" if lang == "en" else "../") + "assets/img/about/"
    photos = "\n".join(
        f'        <a class="photo-link" href="{img}{f}" aria-label="{t["enlarge"]}: {alts[i]}">'
        f'<img src="{img}{f}" alt="{alts[i]}" width="{w}" height="{h}" loading="lazy"></a>'
        for f, w, h, *alts in PHOTOS)
    links = "".join(f'<a href="{href}">{label}</a>' for href, label in t["links"])
    body = f"""    <section class="case-head about-head">
      <h1>{t["h1"]}</h1>
      <p class="about-name">{t["name"]} <span>· {t["role"]}</span></p>
    </section>

    <article class="about-text">
      <p class="about-lead">{t["lead"]}</p>
      <p>{t["body"]}</p>
      <p class="about-photos-caption">{t["photos_caption"]}</p>
      <div class="about-photos">
{photos}
      </div>
      <nav class="about-links">{links}</nav>
    </article>"""
    popover = f"""
  <div id="cert-large" class="cert-pop about-pop" popover><button type="button" popovertarget="cert-large" popovertargetaction="hide" aria-label="{t["close"]}"><img alt=""></button></div>"""
    script = """
  <script>
    // Open a photo in the popover instead of leaving the page.
    const pop = document.getElementById("cert-large"), big = pop.querySelector("img");
    document.querySelectorAll(".photo-link").forEach(a => a.addEventListener("click", e => {
      if (!pop.showPopover) return;
      e.preventDefault();
      big.src = a.getAttribute("href");
      big.alt = a.querySelector("img").alt;
      pop.showPopover();
    }));
  </script>"""
    write_page(lang, "about.html", t["title"], t["description"], "assets/img/avatar-large.jpg", body,
               extra_popovers=popover, script=script)


if __name__ == "__main__":
    for lang in TEXT:
        build(lang)
