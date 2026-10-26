#!/usr/bin/env python3
"""Deterministic daily banner updater for GitHub Actions.

Preserves the handmade SVG layout and SMIL animations while updating the daily
door numbers on the 100-door horizon scale and the contribution stamp if provided.
"""

from __future__ import annotations

import datetime as dt
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"


def daily_doors(day_seed: int) -> list[str]:
    """Select 5 deterministic, strictly increasing door numbers in [001..100]."""
    offsets = [0, 17, 41, 62, 79]
    nums = sorted(((day_seed + off) % 100) + 1 for off in offsets)
    return [f"#{n:03d}" for n in nums]


def update_svg(path: pathlib.Path, doors: list[str], commits: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\d+\s+CONTRIBUTIONS\s+\(12M\)", f"{commits} CONTRIBUTIONS (12M)", text)
    text = re.sub(r"\d+\s+contributions\s+\(12m\)", f"{commits} contributions (12m)", text)

    existing = re.findall(r">#\d{3}<", text)
    if len(existing) == len(doors):
        idx = 0

        def repl(_match: re.Match[str]) -> str:
            nonlocal idx
            out = f">{doors[idx]}<"
            idx += 1
            return out

        text = re.sub(r">#\d{3}<", repl, text)

    path.write_text(text, encoding="utf-8")


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).date()
    day_seed = today.timetuple().tm_yday
    doors = daily_doors(day_seed)
    commits = os.environ.get("CONTRIBUTIONS_12M", "640")

    for name in ("banner.svg", "banner-dark.svg", "banner-v2.svg", "banner-v2-dark.svg"):
        svg_path = ASSETS / name
        if svg_path.exists():
            update_svg(svg_path, doors, commits)


if __name__ == "__main__":
    main()
