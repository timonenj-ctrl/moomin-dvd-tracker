#!/usr/bin/env python3
import json, datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SOURCES = BASE / "data" / "sources.json"
OUT = BASE / "data" / "live-picks.json"

def main():
    data = json.loads(SOURCES.read_text(encoding="utf-8"))
    out = {
        "updated": datetime.date.today().isoformat(),
        "note": "Safe placeholder picks. Extend with RSS/API-based picks or stable sources. Prefer live search links for reliability.",
        "countries": {}
    }
    for c in data.get("countries", []):
        picks = []
        for src in c.get("sources", []):
            for u in (src.get("search_urls") or [])[:1]:
                picks.append({"source": src.get("name"), "title": u.get("label"), "url": u.get("url")})
        out["countries"][c["code"]] = picks[:6]
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
