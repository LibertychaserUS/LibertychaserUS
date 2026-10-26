#!/usr/bin/env python3
"""Contribution calendar, drawn in the banner's own hand.

GitHub's native graph cannot be restyled, so this script reads the same
numbers from the GraphQL API and draws them on the same paper as the banner:
53 weeks by 7 days, amber for activity, ink frame, light and dark sheets.
Needs GH_TOKEN or GITHUB_TOKEN. Writes assets/contributions.svg and
assets/contributions-dark.svg.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
import urllib.request
from pathlib import Path

LOGIN = "LibertychaserUS"
W, H = 980, 240
MARGIN, TOP = 36, 84
CELL, GAP = 14.0, 3.2
MONO = "ui-monospace, 'SFMono-Regular', 'JetBrains Mono', Menlo, Consolas, monospace"

THEMES = {
    "": dict(sheet="#F4EFE4", frame="#2B2925", ink="#1F1E1B", soft="#5E5950",
             empty="#E6DFD1", levels=["#EBCF9A", "#E5A93C", "#D9822B", "#B03A2E"], edge="#2B2925"),
    "-dark": dict(sheet="#181715", frame="#8C8577", ink="#EAE4D7", soft="#9E978B",
                  empty="#2A2722", levels=["#7A5520", "#B8842E", "#E5A93C", "#D96B5C"], edge="#8C8577"),
}
LEVEL = {"NONE": -1, "FIRST_QUARTILE": 0, "SECOND_QUARTILE": 1, "THIRD_QUARTILE": 2, "FOURTH_QUARTILE": 3}
MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def fetch() -> dict:
    tok = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not tok:
        sys.exit("contributions: no GH_TOKEN / GITHUB_TOKEN in the environment")
    q = ('{ user(login:"%s") { contributionsCollection { contributionCalendar { '
         'totalContributions weeks { contributionDays { date contributionCount contributionLevel } } } } } }' % LOGIN)
    req = urllib.request.Request(
        "https://api.github.com/graphql", data=json.dumps({"query": q}).encode(),
        headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json",
                 "User-Agent": f"{LOGIN}-profile-contributions"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def render(cal: dict, t: dict, day: dt.date) -> str:
    weeks = cal["weeks"]
    pitch = CELL + GAP
    grid_w = len(weeks) * pitch - GAP
    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" role="img" '
        f'aria-label="{cal["totalContributions"]} contributions in the last twelve months, drawn by week and day">',
        "<defs>",
        '<filter id="sketch-c" x="-2%" y="-2%" width="104%" height="104%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="7" result="n"/>'
        '<feDisplacementMap in="SourceGraphic" in2="n" scale="0.7" xChannelSelector="R" yChannelSelector="G"/></filter>',
        f"<style>text{{font-family:{MONO};}}</style>",
        "</defs>",
        f'<rect width="{W}" height="{H}" rx="8" fill="{t["sheet"]}"/>',
        f'<rect x="12" y="12" width="{W-24}" height="{H-24}" rx="4" fill="none" stroke="{t["frame"]}" stroke-width="1.2" stroke-opacity="0.7"/>',
        f'<text x="{MARGIN}" y="46" font-size="11" font-weight="700" letter-spacing="1.6" fill="{t["ink"]}">CONTRIBUTION ACTIVITY</text>',
        f'<text x="{W-MARGIN}" y="46" font-size="10" fill="{t["soft"]}" text-anchor="end">'
        f'{cal["totalContributions"]} contributions · last 12 months · drawn {day.isoformat()}</text>',
    ]
    # month labels at the first week that contains the 1st of a month
    seen = set()
    for i, w in enumerate(weeks):
        for d in w["contributionDays"]:
            date = dt.date.fromisoformat(d["date"])
            if date.day == 1 and date.month not in seen and i > 0:
                seen.add(date.month)
                o.append(f'<text x="{MARGIN + i*pitch:.1f}" y="{TOP-10}" font-size="9" letter-spacing="0.8" fill="{t["soft"]}">{MONTHS[date.month-1]}</text>')
                break
    o.append(f'<g filter="url(#sketch-c)" stroke="{t["edge"]}" stroke-opacity="0.22" stroke-width="0.6">')
    for i, w in enumerate(weeks):
        for d in w["contributionDays"]:
            wd = (dt.date.fromisoformat(d["date"]).weekday() + 1) % 7  # Sunday first, like GitHub
            lv = LEVEL.get(d["contributionLevel"], -1)
            fill = t["empty"] if lv < 0 else t["levels"][lv]
            o.append(f'<rect x="{MARGIN + i*pitch:.1f}" y="{TOP + wd*pitch:.1f}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}">'
                     f'<title>{d["date"]}: {d["contributionCount"]}</title></rect>')
    o.append("</g>")
    # weekday ticks and legend
    for wd, lab in [(1, "MON"), (3, "WED"), (5, "FRI")]:
        o.append(f'<text x="{MARGIN - 6}" y="{TOP + wd*pitch + CELL - 3:.1f}" font-size="8" fill="{t["soft"]}" text-anchor="end" letter-spacing="0.5">{lab}</text>')
    ly = TOP + 7 * pitch + 10
    lx = W - MARGIN - (5 * pitch - GAP) - 62
    o.append(f'<text x="{lx - 8}" y="{ly + 11}" font-size="9" fill="{t["soft"]}" text-anchor="end">LESS</text>')
    for k, c in enumerate([t["empty"]] + t["levels"]):
        o.append(f'<rect x="{lx + k*pitch:.1f}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{c}" stroke="{t["edge"]}" stroke-opacity="0.22" stroke-width="0.6"/>')
    o.append(f'<text x="{lx + 5*pitch + 4:.1f}" y="{ly + 11}" font-size="9" fill="{t["soft"]}">MORE</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


def main() -> None:
    cal = fetch()
    print(json.dumps({"total": cal["totalContributions"], "weeks": len(cal["weeks"])}))
    Path("assets").mkdir(exist_ok=True)
    today = dt.date.today()
    for suffix, t in THEMES.items():
        Path(f"assets/contributions{suffix}.svg").write_text(render(cal, t, today), encoding="utf-8")


if __name__ == "__main__":
    main()
