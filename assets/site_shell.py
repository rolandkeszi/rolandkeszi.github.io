"""Shared page shell for the generated pages (about, certificates, education).

The header, photo popover and footer are copied from index.html and
hu/index.html, so generated pages always match the hand-written ones.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://rolandkeszi.github.io/"


def external_new_tab(page: str) -> str:
    """Make every external link (http/https/mailto) open in a new window, so no click leaves the site."""
    def fix(m: re.Match) -> str:
        tag = m.group(0)
        if not re.search(r'href="(https?:|mailto:)', tag) or 'target="' in tag:
            return tag
        rel = re.search(r'rel="([^"]*)"', tag)
        if rel:
            if "noopener" not in rel.group(1).split():
                tag = tag.replace(rel.group(0), f'rel="{rel.group(1)} noopener"')
            return tag[:-1] + ' target="_blank">'
        return tag[:-1] + ' target="_blank" rel="noopener">'
    return re.sub(r"<a\b[^>]*>", fix, page)


def css_version() -> str:
    return re.search(r"style\.css\?v=(\d+)", (ROOT / "index.html").read_text(encoding="utf-8")).group(1)


def write_page(lang: str, page: str, title: str, description: str, og_image: str, body: str,
               extra_popovers: str = "", script: str = "") -> None:
    """Write <page> (e.g. "certificates.html") at the site root (en) or under hu/ (hu)."""
    src = ROOT / ("index.html" if lang == "en" else "hu/index.html")
    home = src.read_text(encoding="utf-8")
    prefix = "" if lang == "en" else "../"
    en_href, hu_href = (page, f"hu/{page}") if lang == "en" else (f"../{page}", page)

    header = re.search(r'<header class="top">.*?</header>', home, re.S).group(0)
    header = header.replace('href="#projects"', 'href="./#projects"')
    header = header.replace(f'<a href="{page}">', f'<a href="{page}" aria-current="page">')
    header = re.sub(r'(<a[^>]*?href=")[^"]*(" hreflang="en")', rf"\g<1>{en_href}\2", header)
    header = re.sub(r'(<a[^>]*?href=")[^"]*(" hreflang="hu")', rf"\g<1>{hu_href}\2", header)
    popovers = re.search(r'<div id="photo-large".*?</button></div>', home, re.S).group(0)
    footer = re.search(r"<footer>.*?</footer>", home, re.S).group(0)

    out = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{SITE}{og_image}">
  <link rel="alternate" hreflang="en" href="{SITE}{page}">
  <link rel="alternate" hreflang="hu" href="{SITE}hu/{page}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/style.css?v={css_version()}">
</head>
<body>
  {header}
  {popovers}{extra_popovers}
  <div class="wrap">

{body}

    {footer}
  </div>{script}
</body>
</html>
"""
    (ROOT / ("" if lang == "en" else "hu") / page).write_text(external_new_tab(out), encoding="utf-8", newline="\n")
    print("wrote", ("" if lang == "en" else "hu/") + page)
