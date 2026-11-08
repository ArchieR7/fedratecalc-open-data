#!/usr/bin/env python3
"""Sync FedRateCalc open data from the live /data/ hub into a local repo folder.

Downloads every file linked from https://fedratecalc.com/data/ (CSV, JSON, ICS), reads each dataset page's
schema.org Dataset JSON-LD, and writes README.md, LICENSE and CITATION.cff. Plain HTTP GETs to our own site.

Usage: python3 -I sync.py <repo_dir>
"""
import datetime as dt
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

BASE = "https://fedratecalc.com"
UA = {"User-Agent": "fedratecalc-open-data-sync"}


def get(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()


def main(repo: Path):
    hub = get(f"{BASE}/data/").decode("utf-8", "replace")
    files = sorted(set(re.findall(r'href="(/data/files/[^"]+)"', hub)))
    pages = sorted(set(p for p in re.findall(r'href="(/data/[a-z0-9-]+/)"', hub) if not p.startswith("/data/files/")))
    if not files or not pages:
        sys.exit(f"nothing found on /data/ (files={len(files)}, pages={len(pages)})")
    data = repo / "data"
    data.mkdir(parents=True, exist_ok=True)
    for f in files:
        name = f.rsplit("/", 1)[-1]
        (data / name).write_bytes(get(BASE + f))
    datasets = []
    for p in pages:
        s = get(BASE + p).decode("utf-8", "replace")
        for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>([\s\S]*?)</script>', s):
            try:
                j = json.loads(html.unescape(block))
            except json.JSONDecodeError:
                continue
            for node in (j if isinstance(j, list) else j.get("@graph", [j])):
                if isinstance(node, dict) and node.get("@type") == "Dataset":
                    dl = node.get("distribution") or []
                    datasets.append({
                        "name": node.get("name", p),
                        "description": node.get("description", ""),
                        "url": BASE + p,
                        "modified": node.get("dateModified", ""),
                        "files": [d.get("contentUrl", "").rsplit("/", 1)[-1] for d in dl if isinstance(d, dict)],
                        "sources": [c.get("url") if isinstance(c, dict) else c for c in (node.get("isBasedOn") or [])] if node.get("isBasedOn") else [],
                    })
    datasets.sort(key=lambda d: d["name"])
    today = dt.date.today().isoformat()
    lines = [
        "# FedRateCalc open data",
        "",
        "U.S. federal rate, calendar, holiday, wage, sales tax and electricity price data in CSV, JSON and ICS, mirrored from the "
        f"[FedRateCalc open data hub]({BASE}/data/). Each dataset is generated from official sources (Federal Reserve "
        "Board, BLS, BEA, OPM, EIA, state labor and tax departments) and checked on the date shown on its page.",
        "",
        f"Synced from {BASE}/data/ on {today}. The website is the canonical, most current copy; "
        "this repository is a convenience mirror.",
        "",
        "## Datasets",
        "",
        "| Dataset | Files | Updated | Page |",
        "| --- | --- | --- | --- |",
    ]
    for d in datasets:
        fl = ", ".join(f"[`{n}`](data/{n})" for n in d["files"] if n) or "see page"
        lines.append(f"| {d['name']} | {fl} | {d['modified'] or '-'} | [{d['url'].replace(BASE, 'fedratecalc.com')}]({d['url']}) |")
    lines += [
        "",
        "## License and citation",
        "",
        "The compiled datasets are licensed under [CC BY 4.0](LICENSE): credit **FedRateCalc** with a link to "
        f"{BASE}/data/. The underlying U.S. government figures are in the public domain.",
        "",
        "Suggested citation: FedRateCalc. *<dataset name>*. " + f"{BASE}/data/ (accessed <date>).",
        "",
        "GitHub shows a \"Cite this repository\" button from [CITATION.cff](CITATION.cff).",
        "",
        "## Updates",
        "",
        "Files are refreshed from the website when the underlying data changes (for example after an FOMC meeting "
        "or a new release calendar, a state sales tax rate, or a new EIA electricity price month). Corrections: open an issue, or see the source links on each dataset page.",
        "",
    ]
    (repo / "README.md").write_text("\n".join(lines))
    # LICENSE holds the official CC BY 4.0 legal code (so GitHub detects it); never overwritten here.
    (repo / "CITATION.cff").write_text(
        "cff-version: 1.2.0\n"
        "message: \"If you use these datasets, please cite FedRateCalc and link to the open data hub.\"\n"
        "title: \"FedRateCalc open data\"\n"
        "type: dataset\n"
        "authors:\n"
        "  - name: \"FedRateCalc\"\n"
        f"url: \"{BASE}/data/\"\n"
        "repository-code: \"https://github.com/ArchieR7/fedratecalc-open-data\"\n"
        "license: CC-BY-4.0\n"
        f"date-released: \"{today}\"\n"
        "keywords:\n"
        "  - fomc\n  - federal funds rate\n  - economic calendar\n  - federal holidays\n  - minimum wage\n  - sales tax\n  - electricity rates\n"
    )
    (repo / "sync.py").write_text(Path(__file__).read_text())
    print(f"files {len(files)}, datasets {len(datasets)}")
    for d in datasets:
        print(" -", d["name"], d["files"], d["modified"])


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve())
