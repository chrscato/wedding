"""Copy the venue reports into docs/ for GitHub Pages.

The report HTML files are written for claude.ai artifacts, which add the
<!doctype>/<head> skeleton at publish time. GitHub Pages serves files as-is,
so this adds that skeleton. Run after editing a report, then commit docs/.
"""
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
REPORTS = {
    "hyatt_oakbrook/hyatt-lodge-report.html": "hyatt.html",
    "makray_golf/makray-report.html": "makray.html",
    "royal_melbourne/royal-melbourne-report.html": "royal-melbourne.html",
    "lincolnshire/lincolnshire-report.html": "lincolnshire.html",
}
HEAD = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
)
BACK = (
    '<p style="max-width:880px;margin:0 auto;padding:16px 20px 0;font:14px '
    '\'IBM Plex Sans\',\'Segoe UI\',system-ui,sans-serif"><a href="./" '
    'style="color:#1f3b5c">&larr; All venues</a></p>\n'
)


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    for src, dest in REPORTS.items():
        html = (ROOT / src).read_text(encoding="utf-8")
        # head = everything up to the first <div class="doc">; body = the rest
        split = html.index('<div class="doc">')
        page = HEAD + html[:split] + "</head>\n<body>\n" + BACK + html[split:] + "\n</body>\n</html>\n"
        (DOCS / dest).write_text(page, encoding="utf-8")
        print(f"wrote docs/{dest}")


if __name__ == "__main__":
    main()
