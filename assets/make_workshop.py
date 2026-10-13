"""Build the ELTE Innofair 2026 workshop page (innofair-workshop.html, EN and HU)
and its registration chart (assets/img/workshop/registrations-{en,hu}.svg).

    python assets/make_workshop.py
"""
from pathlib import Path

from site_shell import ROOT, write_page

REG_URL = "https://keszi.krolify.hu/hu/kutatas/elte-innofair/"
PHOTOS_URL = "https://drive.google.com/drive/folders/1SNw69G51sgFOmnAuI-xXAqEu1McVmtoh"

# Cumulative registrations on the workshop's own page at the end of each day,
# 8-30 September 2026, read from the labelled values of the original chart.
CUMULATIVE = [0, 11, 15, 16, 16, 22, 32, 41, 43, 55, 64, 66, 69, 71, 74, 74, 74, 75, 76, 77, 87, 91, 97]

# (file stem, English caption, Hungarian caption) in display order.
PHOTOS = [
    ("hall", "The Harmónia Hall before the workshop", "A Harmónia terem a workshop előtt"),
    ("opening-talk", "Opening talk", "Nyitóelőadás"),
    ("speech-recognition", "Speech recognition: overview and industrial outlook", "Beszédfelismerés: általános áttekintés és ipari kitekintés"),
    ("talk", "During the talks", "Előadás közben"),
    ("robot-interviewer-slide", "The robot interviewer", "A robot kérdezőbiztos"),
    ("robot-interviewer", "The robot interviewer", "A robot kérdezőbiztos"),
    ("talkie-aac", "Live demonstration of the Talkie AAC app", "A Talkie AAC-alkalmazás élő bemutatója"),
    ("audience", "The audience", "A közönség"),
]

TEXT = {
    "en": {
        "title": "Voice for everyone! A workshop at ELTE Innofair 2026 · Roland Keszi",
        "description": "Workshop report: language technology, speech recognition and AAC in practice, organised and moderated by Roland Keszi at ELTE Innofair 2026.",
        "h1": "Voice for everyone! Language technology, speech recognition and AAC in practice",
        "lede": "A workshop I initiated, organised and moderated at ELTE Innofair 2026, with an opening talk of my own. It showed, through concrete, practical projects, how language technology and automatic speech recognition can help people whose speech is impaired.",
        "facts": [
            ("Event", "ELTE Innofair 2026 · 30 September 2026 · Harmónia Hall, ELTE Lágymányos Campus"),
            ("My role", "Initiator, organiser, moderator and opening speaker"),
            ("Audience", "129 registrations: special needs teachers, researchers, industry experts"),
        ],
        "sections": [
            ("The event", [
                "ELTE Innofair is the flagship event that showcases the innovation and industry partnerships of Eötvös Loránd University. Our workshop set out to demonstrate, through <strong>concrete, practical projects</strong>, the gaps between language technology research, its industrial applications and everyday use, with the perspective of people with disabilities whose speech is impaired at the centre.",
                "The workshop took place on the afternoon of 30 September 2026 in the Harmónia Hall of the ELTE Lágymányos Campus. Participants were welcomed by Ádám Miklósi, member of the Hungarian Academy of Sciences, university professor and head of institute.",
            ]),
            ("My opening talk", [
                "I opened the workshop with a talk titled <em>Language technology, speech recognition and AAC in practice</em>. It drew on two kinds of analysis:",
                "<ul><li><strong>Epidemiological estimates</strong> of how widespread speech disability is worldwide, and of its causes.</li><li>A <strong>scientometric overview</strong> of language technology research as a whole.</li></ul>",
                "I then introduced the speakers and explained how their talks built on each other.",
            ]),
            ("The programme", [
                "<ul><li><strong>Tibor Fegyó and co-authors</strong> (Budapest University of Technology and Economics, Faculty of Electrical Engineering and Informatics, Department of Telecommunications and Artificial Intelligence; SpeechTex Ltd.): <em>Speech recognition: a general overview and an industrial outlook</em>. A broad picture of automatic speech recognition, followed by the challenges and results of recognising dysarthric, hard-to-understand speech.</li>"
                "<li><strong>Zita Kovács-Ördög</strong> (data scientist, Clementine / Minerva Institute): <em>The robot interviewer</em>. Lessons from developing a robot interviewer and practical uses of AI-based data collection, including aspects related to the communication of people with disabilities.</li>"
                "<li><strong>Zoltán Répási</strong> (hahodori): a live demonstration of <em>Talkie</em>, a browser-based AAC (augmentative and alternative communication) app, and the experience gained with it. A concrete, practical solution that makes everyday communication easier for people with disabilities and their families.</li></ul>",
            ]),
            ("Registrations and audience", [
                "<strong>129 people registered</strong> for the workshop: 97 on the workshop's own registration page and 32 on the Innofair platform. Figure 1 shows how the registrations on our own page built up over time.",
                "FIGURE",
                "Part of the audience were current and future special needs teachers, who work directly with people who use AAC tools. They were joined by researchers, industry experts and other interested visitors. Participants asked a great many questions, ranging from the technical side of language technology through the use of the robot interviewer to the human side and personal involvement. After the official close many stayed on, and the workshop ended in informal conversations.",
            ]),
            ("Why it matters", [
                "We wanted this programme to be part of Innofair because the event's aim, connecting research and industry, directly affects people's quality of life in our field. The perspective of people with disabilities rarely takes centre stage at technology events, yet this is where speech technology can bring some of its greatest social benefit.",
                "The speakers took part as volunteers, without a fee. Our goal is for the workshop to start new collaborations between researchers, developers, civil initiatives and the special needs education profession.",
            ]),
        ],
        "figure_caption": "Figure 1. Cumulative number of registrations on the workshop's own registration page, 8–30 September 2026 (n = 97).",
        "photos": "Photos",
        "links": [("Workshop registration page", REG_URL), ("All photos (Google Drive)", PHOTOS_URL)],
        "back": "← All projects",
        "close": "Close",
        "enlarge": "Enlarge photo",
    },
    "hu": {
        "title": "Hangot mindenkinek! Workshop az ELTE Innofair 2026-on · Keszi Roland",
        "description": "Workshop-beszámoló: nyelvtechnológia, beszédfelismerés és AAC a gyakorlatban. Szervező és moderátor: Keszi Roland, ELTE Innofair 2026.",
        "h1": "Hangot mindenkinek! – Nyelvtechnológia, beszédfelismerés és AAC a gyakorlatban",
        "lede": "Workshop az ELTE Innofair 2026-on, amelynek ötletgazdája, kezdeményezője, szervezője, moderátora és nyitóelőadója voltam. Konkrét, gyakorlati projekteken keresztül mutatta be, hogyan segíthet a nyelvtechnológia és a gépi beszédfelismerés azoknak, akiknek a beszéde akadályozott.",
        "facts": [
            ("Esemény", "ELTE Innofair 2026 · 2026. szeptember 30. · Harmónia terem, ELTE Lágymányosi Campus"),
            ("Szerepem", "Ötletgazda, szervező, moderátor és nyitóelőadó"),
            ("Közönség", "129 regisztráló: gyógypedagógusok, kutatók, ipari szakemberek"),
        ],
        "sections": [
            ("Az esemény", [
                "Szakmai workshop szervezésével vettünk részt az ELTE Innofair 2026, az Eötvös Loránd Tudományegyetem innovációs és ipari kapcsolatait bemutató kiemelt eseményén. A rendezvényen a nyelvtechnológiai kutatások, azok ipari alkalmazásai és a mindennapi használat között lévő szakadékokat igyekeztünk <strong>konkrét, gyakorlati projektek</strong> bemutatásával demonstrálni, a beszédükben akadályozott, fogyatékossággal élő személyek szempontjait kiemeltként kezelve.",
                "2026. szeptember 30-án délután az ELTE Lágymányosi Campus Harmónia termében tartottuk meg a workshopot. A résztvevőket Miklósi Ádám akadémikus, egyetemi tanár, intézetvezető köszöntötte.",
            ]),
            ("Nyitóelőadásom", [
                "A workshopot a „Nyelvtechnológia, beszédfelismerés és AAC a gyakorlatban” című nyitóelőadásom vezette be. Két elemzésre épült:",
                "<ul><li>a beszédfogyatékosság világszintű elterjedtségét és okait leíró <strong>epidemiológiai becslésekre</strong>;</li><li>a nyelvtechnológiai kutatások általános <strong>tudománymetriai áttekintésére</strong>.</li></ul>",
                "Ezt követően bemutattam az előadókat és az előadások egymásra épülésének logikáját.",
            ]),
            ("A program", [
                "<ul><li><strong>Fegyó Tibor és szerzőtársai</strong> (Budapesti Műszaki és Gazdaságtudományi Egyetem, Villamosmérnöki és Informatikai Kar, Távközlési és Mesterséges Intelligencia Tanszék; SpeechTex Kft.): <em>Beszédfelismerés – általános áttekintés és ipari kitekintés</em>. Átfogó képet adott a gépi beszédfelismerésről, majd rövid ipari kitekintésként bemutatta a dizartriás, nehezen érthető beszéd felismerésének kihívásait és eredményeit.</li>"
                "<li><strong>Kovács-Ördög Zita</strong> (adattudós, Clementine / Minerva Intézet): <em>A robot kérdezőbiztos</em>. A robot kérdezőbiztos fejlesztésének tapasztalatait és a mesterségesintelligencia-alapú adatfelvétel gyakorlati alkalmazásait mutatta be, kitérve a fogyatékossággal élők kommunikációjához kapcsolódó vonatkozásokra is.</li>"
                "<li><strong>Répási Zoltán</strong> (hahodori): élő bemutatón ismertette a <em>Talkie</em> nevű, böngészőalapú AAC-alkalmazást (augmentatív és alternatív kommunikáció) és az azzal szerzett tapasztalatokat: egy konkrét, gyakorlati megoldást, amely a fogyatékossággal élő emberek és családtagjaik mindennapi kommunikációját könnyíti meg.</li></ul>",
            ]),
            ("Regisztrációk és közönség", [
                "A workshopra <strong>129-en regisztráltak</strong>: 97-en a workshop saját regisztrációs oldalán, 32-en az Innofair felületén. A saját oldalon történt regisztrációk időbeli alakulását az 1. ábra mutatja.",
                "FIGURE",
                "A közönség egy részét jelenlegi és leendő gyógypedagógusok adták, akik munkájuk során közvetlenül érintettek az AAC-eszközöket használó emberekkel; mellettük kutatók, ipari szakemberek és érdeklődők is eljöttek. A résztvevők rengeteg kérdést tettek fel, amelyek a nyelvtechnológia technológiai kérdéseitől a robot kérdezőbiztos használatán át egészen az emberi oldalig, a személyes érintettség kérdéséig értek. A program hivatalos zárása után is sokan a helyszínen maradtak, és a workshop kötetlen, egymás közötti beszélgetésekkel zárult.",
            ]),
            ("Miért fontos", [
                "Azért tartottuk fontosnak, hogy ez a program az Innofair része legyen, mert a rendezvény célja – a kutatás és az ipar összekapcsolása – a mi területünkön közvetlenül az emberek életminőségét érinti. A fogyatékossággal élő emberek szempontjai ritkán kerülnek a technológiai rendezvények középpontjába, pedig a beszédtechnológia egyik legnagyobb társadalmi haszna éppen itt jelentkezhet.",
                "Az előadók önkéntesként, díjazás nélkül vettek részt a projektben; célunk, hogy a workshop nyomán új együttműködések induljanak a kutatók, a fejlesztők, a civil kezdeményezések és a gyógypedagógiai szakma között.",
            ]),
        ],
        "figure_caption": "1. ábra. A workshop saját regisztrációs oldalán regisztrálók kumulált száma, 2026. szeptember 8–30. (n = 97)",
        "photos": "Fotók",
        "links": [("A workshop regisztrációs oldala", REG_URL), ("Az összes fotó (Google Drive)", PHOTOS_URL)],
        "back": "← Összes projekt",
        "close": "Bezárás",
        "enlarge": "Fotó nagyítása",
    },
}


def chart(lang: str) -> None:
    """Theme-aware step chart of cumulative registrations, in the style of the other site charts."""
    en = lang == "en"
    W, H, L, R, T, B = 860, 420, 64, 24, 70, 360
    days = list(range(8, 31))
    x = lambda i: L + (W - L - R) * i / (len(days) - 1)
    y = lambda v: B - (B - T) * v / 100
    pts, prev = [], None
    for i, v in enumerate(CUMULATIVE):
        if prev is not None:
            pts.append(f"{x(i):.1f},{y(prev):.1f}")
        pts.append(f"{x(i):.1f},{y(v):.1f}")
        prev = v
    line = " ".join(pts)
    area = f"{x(0):.1f},{y(0):.1f} " + line + f" {x(len(days) - 1):.1f},{y(0):.1f}"
    grid = "".join(f'<line class="g" x1="{L}" x2="{W - R}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>'
                   f'<text x="{L - 10}" y="{y(v) + 4:.1f}" font-size="12" class="t2" text-anchor="end">{v}</text>' for v in range(0, 101, 20))
    xt = "".join(f'<text x="{x(i):.1f}" y="{B + 20}" font-size="12" class="t2" text-anchor="middle">{d}</text>'
                 for i, d in enumerate(days) if d % 2 == 0)
    marks = {1: 11, 6: 32, 9: 55, 14: 74, 20: 87, 22: 97}
    labels = "".join(f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="3.5" fill="var(--line)"/>'
                     f'<text x="{x(i) - 6:.1f}" y="{y(v) - 9:.1f}" font-size="12" font-weight="600" text-anchor="end">{v}</text>' for i, v in marks.items())
    title = "Registrations for the workshop" if en else "Regisztrációk a workshopra"
    sub = ("Cumulative, on the workshop's own registration page · September 2026 · n = 97" if en
           else "Kumulált szám, a workshop saját regisztrációs oldalán · 2026. szeptember · n = 97")
    xlab = "Day of September 2026" if en else "2026. szeptember napjai"
    desc = ("Registrations grew from 11 on 9 September to 74 by 22 September, levelled off, then rose again in the final days to 97 on 30 September."
            if en else "A regisztrációk száma szeptember 9-i 11-ről szeptember 22-ig 74-re nőtt, majd megtorpant, és az utolsó napokban szeptember 30-ig 97-re emelkedett.")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H + 30}" viewBox="0 0 {W} {H + 30}" role="img" aria-labelledby="t d">
<title id="t">{title}</title>
<desc id="d">{desc}</desc>
<style>
svg{{--bg:#ffffff;--t1:#1f2328;--t2:#59636e;--grid:#d1d9e0;--line:#2a78d6;--fill:rgba(42,120,214,.12)}}
@media (prefers-color-scheme: dark){{svg{{--bg:#0d1117;--t1:#f0f6fc;--t2:#9198a1;--grid:#30363d;--line:#3987e5;--fill:rgba(57,135,229,.18)}}}}
text{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;fill:var(--t1)}}
.t2{{fill:var(--t2)}} .g{{stroke:var(--grid);stroke-width:1}}
</style>
<rect width="{W}" height="{H + 30}" rx="8" fill="var(--bg)"/>
<text x="24" y="34" font-size="18" font-weight="600">{title}</text>
<text x="24" y="54" font-size="13" class="t2">{sub}</text>
{grid}
<polygon points="{area}" fill="var(--fill)"/>
<polyline points="{line}" fill="none" stroke="var(--line)" stroke-width="2.5" stroke-linejoin="round"/>
{labels}
{xt}
<text x="{(L + W - R) / 2:.0f}" y="{B + 44}" font-size="12" class="t2" text-anchor="middle">{xlab}</text>
</svg>
"""
    (ROOT / f"assets/img/workshop/registrations-{lang}.svg").write_text(svg, encoding="utf-8", newline="\n")


def build(lang: str) -> None:
    t = TEXT[lang]
    prefix = "" if lang == "en" else "../"
    img = f"{prefix}assets/img/workshop/"
    facts = "\n".join(f"        <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in t["facts"])
    links = " ".join(f'<a href="{u}" target="_blank" rel="noopener">{n} ↗</a>' for n, u in t["links"])
    figure = (f'      <figure><img src="{img}registrations-{lang}.svg" alt="{t["figure_caption"]}" width="860" height="450">'
              f'<figcaption>{t["figure_caption"]}</figcaption></figure>')
    sections = []
    for h, paras in t["sections"]:
        body = "\n".join(figure if p == "FIGURE" else (f"      {p}" if p.startswith("<ul>") else f"      <p>{p}</p>") for p in paras)
        sections.append(f"      <h2>{h}</h2>\n{body}")
    i = 0 if lang == "en" else 1
    gallery = "\n".join(
        f'        <figure class="photo"><a class="cert-img photo-link" href="{img}{stem}.jpg" aria-label="{t["enlarge"]}: {caps[i]}">'
        f'<img src="{img}{stem}-sm.jpg" alt="{caps[i]}" loading="lazy"></a><figcaption>{caps[i]}</figcaption></figure>'
        for stem, *caps in PHOTOS)
    body = f"""    <a class="back" href="./#projects">{t["back"]}</a>
    <section class="case-head">
      <h1>{t["h1"]}</h1>
      <p class="lede">{t["lede"]}</p>
      <dl class="facts">
{facts}
      </dl>
      <p class="meta ws-links">{links}</p>
    </section>

    <article>
{chr(10).join(sections)}
      <h2>{t["photos"]}</h2>
      <div class="photo-grid">
{gallery}
      </div>
    </article>"""
    popover = f"""
  <div id="cert-large" class="cert-pop" popover><button type="button" popovertarget="cert-large" popovertargetaction="hide" aria-label="{t["close"]}"><img alt=""></button></div>"""
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
    write_page(lang, "innofair-workshop.html", t["title"], t["description"], "assets/img/workshop/thumb.jpg",
               body, extra_popovers=popover, script=script)


if __name__ == "__main__":
    for lang in TEXT:
        chart(lang)
        build(lang)
