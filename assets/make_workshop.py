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
    ("opening-talk", "Opening talk by Roland Keszi", "Nyitóelőadás: Keszi Roland"),
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
            ('My opening talk', [
                'I opened the workshop with a talk titled <em>Language technology, speech recognition and AAC in practice</em>. It set out what dysarthria is, how many people it affects, why it is hard for automatic speech recognition and where research is heading, and it closed with a scientometric map of the field.',
                '<h3>What dysarthria is</h3>',
                "Dysarthria is a <strong>motor speech disorder of neurological origin</strong>. It is not a language or cognitive problem but a disorder in carrying out the movements of speech: articulation becomes imprecise and slurred, the tempo slow, halting or irregular, and listeners find the speech much harder to understand. It commonly accompanies stroke, Parkinson's disease, cerebral palsy, and ALS and other neurodegenerative conditions.",
                '<h3>How many people are affected</h3>',
                '<div class="globe-row"><picture class="globe"><source srcset="{IMG}globe.webp" type="image/webp" media="(prefers-reduced-motion: no-preference)"><img src="{IMG}globe-still.jpg" alt="Rotating globe" width="320" height="320" loading="lazy"></picture><p>I estimated the number from the global prevalence of the underlying conditions and the share of patients who develop dysarthria. Together, <strong>tens of millions of people live with dysarthria worldwide</strong>.</p></div>',
                '<div class="table-scroll"><table><thead><tr><th>Underlying condition</th><th class="num">People worldwide</th><th>Share with dysarthria</th></tr></thead><tbody><tr><td>Parkinson\'s disease</td><td class="num">11.7 million</td><td>about 90% over the course of the disease</td></tr><tr><td>Stroke survivors</td><td class="num">over 100 million</td><td>24–50%</td></tr><tr><td>Cerebral palsy</td><td class="num">17 million</td><td>about 78%, persistent</td></tr><tr><td>ALS</td><td class="num">223,000</td><td>about 70% over the course of the disease</td></tr></tbody></table></div>',
                'The sources use different methods, so the rates are not strictly comparable.',
                '<h3>Why this is hard for speech recognition</h3>',
                '<ul><li><strong>Imprecise articulation:</strong> speech sounds do not follow the usual patterns.</li><li><strong>Large individual variability:</strong> two people with dysarthria can sound very different from each other.</li><li><strong>Data scarcity:</strong> few public, annotated dysarthric recordings are available for training.</li></ul>',
                'Commercial speech recognition systems typically reach a word error rate (WER) below 5% on typical speech. For dysarthric speech the error rate is many times higher: in the talk I illustrated it with about 45%, although the value varies widely with severity and corpus.',
                '<h3>Where research is heading</h3>',
                '<ul><li><strong>Benchmarks and databases:</strong> TORGO and UASpeech as a common yardstick.</li><li><strong>Self-supervised models:</strong> wav2vec 2.0 and HuBERT, which learn from little labelled data.</li><li><strong>LLM-based error correction:</strong> language models that correct the recognition output afterwards.</li><li><strong>Personalisation and synthetic data:</strong> speaker-specific, artificially augmented training data.</li></ul>',
                'It is an active, fast-growing field, with many Interspeech, ICASSP and EUSIPCO papers in 2024–2026 and community initiatives such as the Speech Accessibility Project. Hungarian research is part of it: at <strong>EUSIPCO 2025</strong>, Péter Mihajlik, Éva Székely, Piroska Barta, Máté Soma Kádár, Gergely Dobsinszki and László Tóth (BME) improved dysarthric speech-to-text conversion through TTS-based personalisation.',
                '<h3>A scientometric map of the field</h3>',
                'For the scientometric part I queried the <strong>OpenAlex</strong> API for publications with <em>dysarthria</em> in the title or abstract. This retrieved <strong>423 documents</strong>. In <strong>VOSviewer</strong> I built a keyword co-occurrence network with full counting over all <strong>195 keywords</strong>.',
                '<div class="table-scroll"><table><thead><tr><th>Keyword</th><th class="num">Occurrences</th><th class="num">Total link strength</th></tr></thead><tbody><tr><td>dysarthria</td><td class="num">392</td><td class="num">1,862</td></tr><tr><td>medicine</td><td class="num">92</td><td class="num">620</td></tr><tr><td>audiology</td><td class="num">90</td><td class="num">609</td></tr><tr><td>psychology</td><td class="num">55</td><td class="num">347</td></tr><tr><td>computer science</td><td class="num">44</td><td class="num">307</td></tr><tr><td>intelligibility</td><td class="num">57</td><td class="num">297</td></tr><tr class="chosen"><td>speech recognition</td><td class="num">34</td><td class="num">244</td></tr><tr><td>physical medicine and rehabilitation</td><td class="num">33</td><td class="num">241</td></tr><tr><td>disease</td><td class="num">44</td><td class="num">220</td></tr><tr><td>speech therapy</td><td class="num">43</td><td class="num">207</td></tr><tr class="chosen"><td>artificial intelligence</td><td class="num">20</td><td class="num">142</td></tr></tbody></table></div>',
                '<figure><img src="{IMG}scientometric-map.jpg" alt="Keyword co-occurrence map of dysarthria research" width="783" height="792" loading="lazy"><figcaption>Keyword co-occurrence map of 423 publications on dysarthria (OpenAlex, VOSviewer). Node size shows how often a keyword occurs; colours mark clusters.</figcaption></figure>',
                'The map shows where the gap lies. The field is dominated by its clinical side: medicine, audiology, neurology and rehabilitation. The computational strand (speech recognition, feature extraction, deep learning, transformers) forms a separate cluster at the edge. It is tied to the core mainly through intelligibility and phonation. <em>Artificial intelligence</em> appears in only 20 of the 423 publications. That gap between clinical research and language technology is what the workshop set out to bridge.',
                '<details class="refs"><summary>Sources of the prevalence figures (APA 7)</summary><ol><li>Arthur, K. C., Calvo, A., Price, T. R., Geiger, J. T., Chiò, A., & Traynor, B. J. (2016). Projected increase in amyotrophic lateral sclerosis from 2015 to 2040. <em>Nature Communications, 7</em>, 12408. <a href="https://doi.org/10.1038/ncomms12408" target="_blank" rel="noopener">https://doi.org/10.1038/ncomms12408</a></li><li>Dorsey, E. R., Sherer, T., Okun, M. S., & Bloem, B. R. (2018). The emerging evidence of the Parkinson pandemic. <em>Journal of Parkinson\'s Disease, 8</em>(s1), S3–S8. <a href="https://doi.org/10.3233/JPD-181474" target="_blank" rel="noopener">https://doi.org/10.3233/JPD-181474</a></li><li>Feigin, V. L., Brainin, M., Norrving, B., Martins, S. O., Pandian, J., Lindsay, P., Grupper, M. F., & Rautalin, I. (2025). World Stroke Organization: Global Stroke Fact Sheet 2025. <em>International Journal of Stroke, 20</em>(2), 132–144. <a href="https://doi.org/10.1177/17474930241308142" target="_blank" rel="noopener">https://doi.org/10.1177/17474930241308142</a></li><li>Lin, L.-X., Yao, S.-Y., Chen, Q., Du, M.-Q., Kang, X.-H., Jiang, D.-Y., & Peng, Y. (2025). Stroke-associated dysarthria. <em>Frontiers in Neurology, 16</em>, Article 1629640. <a href="https://doi.org/10.3389/fneur.2025.1629640" target="_blank" rel="noopener">https://doi.org/10.3389/fneur.2025.1629640</a></li><li>Luo, Y., Qiao, L., Li, M., Wen, X., Zhang, W., & Li, X. (2025). Global, regional, national epidemiology and trends of Parkinson\'s disease from 1990 to 2021: Findings from the Global Burden of Disease Study 2021. <em>Frontiers in Aging Neuroscience, 16</em>, Article 1498756. <a href="https://doi.org/10.3389/fnagi.2024.1498756" target="_blank" rel="noopener">https://doi.org/10.3389/fnagi.2024.1498756</a></li><li>McIntyre, S., Goldsmith, S., Webb, A., Ehlinger, V., Hollung, S. J., McConnell, K., Arnaud, C., Smithers-Sheedy, H., Oskoui, M., Khandaker, G., Himmelmann, K., & Kerr, C. (2022). Global prevalence of cerebral palsy: A systematic analysis. <em>Developmental Medicine &amp; Child Neurology, 64</em>(12), 1494–1506. <a href="https://doi.org/10.1111/dmcn.15346" target="_blank" rel="noopener">https://doi.org/10.1111/dmcn.15346</a></li><li>Moya-Galé, G., & Levy, E. S. (2019). Parkinson\'s disease-associated dysarthria: Prevalence, impact and management strategies. <em>Research and Reviews in Parkinsonism, 9</em>, 9–16. <a href="https://doi.org/10.2147/JPRLS.S168090" target="_blank" rel="noopener">https://doi.org/10.2147/JPRLS.S168090</a></li><li>Parkinson\'s Foundation. (n.d.). <em>Statistics</em>. Retrieved September 29, 2026. <a href="https://parkinsons.org/disease/statistics" target="_blank" rel="noopener">https://parkinsons.org/disease/statistics</a></li><li>Schölderle, T., Staiger, A., Lampe, R., Strecker, K., & Ziegler, W. (2016). Dysarthria in adults with cerebral palsy: Clinical presentation and impacts on communication. <em>Journal of Speech, Language, and Hearing Research, 59</em>(2), 216–229. <a href="https://doi.org/10.1044/2015_JSLHR-S-15-0086" target="_blank" rel="noopener">https://doi.org/10.1044/2015_JSLHR-S-15-0086</a></li><li>Target ALS. (n.d.). <em>How ALS affects speech</em>. Retrieved September 29, 2026. <a href="https://targetals.org/news/how-als-affects-speech/" target="_blank" rel="noopener">https://targetals.org/news/how-als-affects-speech/</a></li><li>Vasta, R., Callegaro, S., Canosa, A., Manera, U., Grassano, M., Palumbo, F., Cabras, S., Matteoni, E., Di Pede, F., De Mattei, F., Tafaro, S., Thakur, N. M., Grosenick, R., De Marchi, F., Mazzini, L., Moglia, C., Calvo, A., Dave, K. D., & Chiò, A. (2025). Amyotrophic lateral sclerosis prevalence projection in 2040: A less rare disease. <em>Annals of Clinical and Translational Neurology, 12</em>(10), e70226. <a href="https://doi.org/10.1002/acn3.70226" target="_blank" rel="noopener">https://doi.org/10.1002/acn3.70226</a></li></ol></details>',
                'I then introduced the speakers and explained how their talks built on each other.',
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
            ('Nyitóelőadásom', [
                'A workshopot a „Nyelvtechnológia, beszédfelismerés és AAC a gyakorlatban” című nyitóelőadásom vezette be. Bemutatta, mi a dizartria, hány embert érint, miért nehéz a gépi beszédfelismerésnek, merre tart a kutatás, és a terület tudománymetriai térképével zárult.',
                '<h3>Mi a dizartria?</h3>',
                'A dizartria <strong>neurológiai eredetű motoros beszédzavar</strong>: nem nyelvi vagy kognitív, hanem a beszédmozgások kivitelezésének zavara. A hangképzés pontatlan, az artikuláció elmosódott, a beszédtempó lassú, szaggatott vagy szabálytalan, a beszéd érthetősége a hallgató számára jelentősen csökken. Gyakori kísérőtünete a stroke-nak, a Parkinson-kórnak, a cerebrális parézisnek, valamint az ALS-nek és más neurodegeneratív kórképeknek.',
                '<h3>Hányan érintettek világszerte?</h3>',
                '<div class="globe-row"><picture class="globe"><source srcset="{IMG}globe.webp" type="image/webp" media="(prefers-reduced-motion: no-preference)"><img src="{IMG}globe-still.jpg" alt="Forgó földgömb" width="320" height="320" loading="lazy"></picture><p>Az érintettek számát az alapbetegségek globális előfordulásából és a bennük jellemző dizartria-arányból becsültem. Együttesen <strong>több tízmillió ember él dizartriával világszerte</strong>.</p></div>',
                '<div class="table-scroll"><table><thead><tr><th>Alapbetegség</th><th class="num">Érintettek világszerte</th><th>Dizartria aránya</th></tr></thead><tbody><tr><td>Parkinson-kór</td><td class="num">11,7 millió</td><td>~90% a betegség során</td></tr><tr><td>Stroke-túlélők</td><td class="num">több mint 100 millió</td><td>24–50%</td></tr><tr><td>Cerebrális parézis</td><td class="num">17 millió</td><td>~78%, tartós kísérőtünet</td></tr><tr><td>ALS</td><td class="num">223 000</td><td>~70% a lefolyás során</td></tr></tbody></table></div>',
                'A hivatkozott arányszámok forrásonként eltérő módszertannal készültek, ezért nem közvetlenül összevethetők.',
                '<h3>Miért nehéz ez a gépi beszédfelismerésnek?</h3>',
                '<ul><li><strong>Artikulációs pontatlanság:</strong> a beszédhangok nem a megszokott mintázat szerint jönnek létre.</li><li><strong>Nagy egyéni variabilitás:</strong> két dizartriás beszélő beszéde is nagyon eltérő lehet egymástól.</li><li><strong>Adatszegénység:</strong> kevés nyilvános, annotált dizartriás felvétel áll rendelkezésre a tanításhoz.</li></ul>',
                'A kereskedelmi beszédfelismerő rendszerek szóhibaaránya (WER) tipikus beszédnél jellemzően 5% alatti. Dizartriás beszédnél ennek többszöröse: az előadásban kb. 45%-kal szemléltettem, bár az érték a súlyosságtól és a korpusztól függően erősen szór.',
                '<h3>Merre tart a kutatás?</h3>',
                '<ul><li><strong>Benchmark-adatbázisok:</strong> a TORGO és az UASpeech mint közös mérési alap.</li><li><strong>Self-supervised modellek:</strong> a wav2vec 2.0 és a HuBERT kevés címkézett adatból is tanul.</li><li><strong>LLM-alapú hibajavítás:</strong> nyelvi modellek a felismerés utólagos javítására.</li><li><strong>Perszonalizáció és szintetikus adat:</strong> beszélőre szabott, mesterségesen bővített tanítóadat.</li></ul>',
                'Aktív, felfutó kutatási terület: 2024 és 2026 között az Interspeech, az ICASSP és az EUSIPCO konferenciákon publikációk sokasága jelent meg, közösségi kezdeményezésekkel együtt (például Speech Accessibility Project). A hazai kutatás is az élvonalban van: az <strong>EUSIPCO 2025</strong> konferencián Mihajlik Péter, Székely Éva, Barta Piroska, Kádár Máté Soma, Dobsinszki Gergely és Tóth László (BME) TTS-alapú személyre szabással javította a dizartriás beszéd szöveggé alakításának pontosságát.',
                '<h3>A terület tudománymetriai térképe</h3>',
                'A tudománymetriai elemzéshez az <strong>OpenAlex</strong> API-ból kértem le azokat a publikációkat, amelyek címében vagy absztraktjában szerepel a <em>dysarthria</em> (dizartria) szó. Ez <strong>423 dokumentumot</strong> adott. A <strong>VOSviewer</strong> programmal kulcsszó-együttelőfordulási hálózatot készítettem teljes számlálással, mind a <strong>195 kulcsszó</strong> bevonásával.',
                '<div class="table-scroll"><table><thead><tr><th>Kulcsszó</th><th class="num">Előfordulás</th><th class="num">Összes kapcsolaterősség</th></tr></thead><tbody><tr><td>dysarthria</td><td class="num">392</td><td class="num">1,862</td></tr><tr><td>medicine</td><td class="num">92</td><td class="num">620</td></tr><tr><td>audiology</td><td class="num">90</td><td class="num">609</td></tr><tr><td>psychology</td><td class="num">55</td><td class="num">347</td></tr><tr><td>computer science</td><td class="num">44</td><td class="num">307</td></tr><tr><td>intelligibility</td><td class="num">57</td><td class="num">297</td></tr><tr class="chosen"><td>speech recognition</td><td class="num">34</td><td class="num">244</td></tr><tr><td>physical medicine and rehabilitation</td><td class="num">33</td><td class="num">241</td></tr><tr><td>disease</td><td class="num">44</td><td class="num">220</td></tr><tr><td>speech therapy</td><td class="num">43</td><td class="num">207</td></tr><tr class="chosen"><td>artificial intelligence</td><td class="num">20</td><td class="num">142</td></tr></tbody></table></div>',
                '<figure><img src="{IMG}scientometric-map.jpg" alt="A dizartria-kutatás kulcsszó-együttelőfordulási térképe" width="783" height="792" loading="lazy"><figcaption>423, a dizartriáról szóló publikáció kulcsszó-együttelőfordulási térképe (OpenAlex, VOSviewer). A körök mérete a kulcsszó gyakoriságát, a színek a klasztereket jelölik.</figcaption></figure>',
                'A térkép megmutatja, hol van a szakadék. A területet a klinikai oldal uralja: az orvostudomány, az audiológia, a neurológia és a rehabilitáció. A számítástudományi szál (beszédfelismerés, jellemzőkinyerés, mélytanulás, transzformerek) külön klasztert alkot a háló szélén, és főként az érthetőség és a fonáció kulcsszavakon keresztül kapcsolódik a maghoz. A <em>mesterséges intelligencia</em> a 423 publikációból mindössze 20-ban fordul elő. A workshop éppen ezt a klinikai kutatás és a nyelvtechnológia közötti szakadékot kívánta áthidalni.',
                '<details class="refs"><summary>Az előfordulási adatok forrásai (APA 7)</summary><ol><li>Arthur, K. C., Calvo, A., Price, T. R., Geiger, J. T., Chiò, A., & Traynor, B. J. (2016). Projected increase in amyotrophic lateral sclerosis from 2015 to 2040. <em>Nature Communications, 7</em>, 12408. <a href="https://doi.org/10.1038/ncomms12408" target="_blank" rel="noopener">https://doi.org/10.1038/ncomms12408</a></li><li>Dorsey, E. R., Sherer, T., Okun, M. S., & Bloem, B. R. (2018). The emerging evidence of the Parkinson pandemic. <em>Journal of Parkinson\'s Disease, 8</em>(s1), S3–S8. <a href="https://doi.org/10.3233/JPD-181474" target="_blank" rel="noopener">https://doi.org/10.3233/JPD-181474</a></li><li>Feigin, V. L., Brainin, M., Norrving, B., Martins, S. O., Pandian, J., Lindsay, P., Grupper, M. F., & Rautalin, I. (2025). World Stroke Organization: Global Stroke Fact Sheet 2025. <em>International Journal of Stroke, 20</em>(2), 132–144. <a href="https://doi.org/10.1177/17474930241308142" target="_blank" rel="noopener">https://doi.org/10.1177/17474930241308142</a></li><li>Lin, L.-X., Yao, S.-Y., Chen, Q., Du, M.-Q., Kang, X.-H., Jiang, D.-Y., & Peng, Y. (2025). Stroke-associated dysarthria. <em>Frontiers in Neurology, 16</em>, Article 1629640. <a href="https://doi.org/10.3389/fneur.2025.1629640" target="_blank" rel="noopener">https://doi.org/10.3389/fneur.2025.1629640</a></li><li>Luo, Y., Qiao, L., Li, M., Wen, X., Zhang, W., & Li, X. (2025). Global, regional, national epidemiology and trends of Parkinson\'s disease from 1990 to 2021: Findings from the Global Burden of Disease Study 2021. <em>Frontiers in Aging Neuroscience, 16</em>, Article 1498756. <a href="https://doi.org/10.3389/fnagi.2024.1498756" target="_blank" rel="noopener">https://doi.org/10.3389/fnagi.2024.1498756</a></li><li>McIntyre, S., Goldsmith, S., Webb, A., Ehlinger, V., Hollung, S. J., McConnell, K., Arnaud, C., Smithers-Sheedy, H., Oskoui, M., Khandaker, G., Himmelmann, K., & Kerr, C. (2022). Global prevalence of cerebral palsy: A systematic analysis. <em>Developmental Medicine &amp; Child Neurology, 64</em>(12), 1494–1506. <a href="https://doi.org/10.1111/dmcn.15346" target="_blank" rel="noopener">https://doi.org/10.1111/dmcn.15346</a></li><li>Moya-Galé, G., & Levy, E. S. (2019). Parkinson\'s disease-associated dysarthria: Prevalence, impact and management strategies. <em>Research and Reviews in Parkinsonism, 9</em>, 9–16. <a href="https://doi.org/10.2147/JPRLS.S168090" target="_blank" rel="noopener">https://doi.org/10.2147/JPRLS.S168090</a></li><li>Parkinson\'s Foundation. (n.d.). <em>Statistics</em>. Retrieved September 29, 2026. <a href="https://parkinsons.org/disease/statistics" target="_blank" rel="noopener">https://parkinsons.org/disease/statistics</a></li><li>Schölderle, T., Staiger, A., Lampe, R., Strecker, K., & Ziegler, W. (2016). Dysarthria in adults with cerebral palsy: Clinical presentation and impacts on communication. <em>Journal of Speech, Language, and Hearing Research, 59</em>(2), 216–229. <a href="https://doi.org/10.1044/2015_JSLHR-S-15-0086" target="_blank" rel="noopener">https://doi.org/10.1044/2015_JSLHR-S-15-0086</a></li><li>Target ALS. (n.d.). <em>How ALS affects speech</em>. Retrieved September 29, 2026. <a href="https://targetals.org/news/how-als-affects-speech/" target="_blank" rel="noopener">https://targetals.org/news/how-als-affects-speech/</a></li><li>Vasta, R., Callegaro, S., Canosa, A., Manera, U., Grassano, M., Palumbo, F., Cabras, S., Matteoni, E., Di Pede, F., De Mattei, F., Tafaro, S., Thakur, N. M., Grosenick, R., De Marchi, F., Mazzini, L., Moglia, C., Calvo, A., Dave, K. D., & Chiò, A. (2025). Amyotrophic lateral sclerosis prevalence projection in 2040: A less rare disease. <em>Annals of Clinical and Translational Neurology, 12</em>(10), e70226. <a href="https://doi.org/10.1002/acn3.70226" target="_blank" rel="noopener">https://doi.org/10.1002/acn3.70226</a></li></ol></details>',
                'Ezt követően bemutattam az előadókat és az előadások egymásra épülésének logikáját.',
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
        body = "\n".join(figure if p == "FIGURE" else (f"      {p.replace('{IMG}', img)}" if p.startswith(("<ul>", "<div", "<figure", "<h3", "<details")) else f"      <p>{p}</p>") for p in paras)
        sections.append(f"      <h2>{h}</h2>\n{body}")
    i = 0 if lang == "en" else 1
    def grid(photos):
        return "\n".join(
            f'        <figure class="photo"><a class="cert-img photo-link" href="{img}{stem}.jpg" aria-label="{t["enlarge"]}: {caps[i]}">'
            f'<img src="{img}{stem}-sm.jpg" alt="{caps[i]}" loading="lazy"></a><figcaption>{caps[i]}</figcaption></figure>'
            for stem, *caps in photos)
    gallery = grid(PHOTOS)
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
