#!/usr/bin/env python3
"""Generate the profile banner: a seeded network and a data-rain field.

The README points at assets/banner.svg; a scheduled workflow re-runs this
script each day, so the network and the rain evolve on their own.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import math
import random
from pathlib import Path

W, H = 1280, 360
ACCENT = "#2ad4ff"
NODE = "#9feaff"
TEXT = "#f2fbff"
TAG = "#8fe8ff"
DIM = "#2d6d80"

MONO = (
    "ui-monospace, SFMono-Regular, Menlo, Consolas, "
    "'Liberation Mono', monospace"
)


def make_nodes(rng: random.Random) -> list[tuple[float, float, float]]:
    centers = [
        (150, 120), (300, 235), (120, 260), (420, 120), (360, 300), (230, 60)
    ]
    nodes = []
    for _ in range(92):
        cx, cy = centers[rng.randrange(len(centers))]
        x = min(max(rng.gauss(cx, 52), 18), 540)
        y = min(max(rng.gauss(cy, 44), 24), 338)
        r = rng.choice([1.1, 1.3, 1.5, 1.8, 2.1, 2.4])
        if rng.random() < 0.09:
            r = rng.uniform(3.0, 4.4)  # hub
        nodes.append((x, y, r))
    return nodes


def make_edges(
    nodes: list[tuple[float, float, float]], rng: random.Random
) -> list[tuple[int, int, float]]:
    n = len(nodes)
    near: set[tuple[int, int]] = set()

    for i in range(n):
        xi, yi, _ = nodes[i]
        dists = sorted(
            (
                (math.hypot(xi - nodes[j][0], yi - nodes[j][1]), j)
                for j in range(n)
                if j != i
            )
        )
        for _, j in dists[:2]:
            near.add((min(i, j), max(i, j)))

    while len(near) < n * 2:
        i, j = rng.randrange(n), rng.randrange(n)
        if i == j:
            continue
        d = math.hypot(nodes[i][0] - nodes[j][0], nodes[i][1] - nodes[j][1])
        if 120 < d < 420:
            near.add((min(i, j), max(i, j)))

    edges = []
    for i, j in sorted(near):
        d = math.hypot(nodes[i][0] - nodes[j][0], nodes[i][1] - nodes[j][1])
        opacity = 0.10 + 0.22 * max(0.0, 1 - d / 460)
        edges.append((i, j, opacity))
    return edges


def make_rain(rng: random.Random) -> list[str]:
    parts = []
    x = 768
    while x < 1272:
        for _ in range(rng.randint(2, 9)):
            y = rng.uniform(8, 336)
            w = rng.choice([3, 4, 5])
            h = rng.choice([2, 3, 4, 6, 8])
            op = rng.uniform(0.05, 0.42)
            if rng.random() < 0.12:
                op = rng.uniform(0.45, 0.75)
            parts.append(
                f'<rect x="{x:.0f}" y="{y:.1f}" width="{w}" height="{h}" '
                f'fill="{ACCENT}" opacity="{op:.2f}"/>'
            )
        x += rng.randint(8, 16)

    for _ in range(6):
        x0 = rng.uniform(820, 1180)
        y0 = rng.uniform(-40, 120)
        length = rng.uniform(160, 340)
        parts.append(
            f'<line x1="{x0:.0f}" y1="{y0:.0f}" '
            f'x2="{x0 + length * 0.62:.0f}" y2="{y0 + length * 0.78:.0f}" '
            f'stroke="{ACCENT}" stroke-width="1.4" '
            f'opacity="{rng.uniform(0.05, 0.13):.2f}"/>'
        )
    return parts


def build(date: dt.date, seed: int) -> str:
    rng = random.Random(seed)
    nodes = make_nodes(rng)
    edges = make_edges(nodes, rng)
    rain = make_rain(rng)

    edge_svg = [
        f'    <line x1="{nodes[i][0]:.1f}" y1="{nodes[i][1]:.1f}" '
        f'x2="{nodes[j][0]:.1f}" y2="{nodes[j][1]:.1f}" '
        f'stroke="{ACCENT}" stroke-width="0.8" opacity="{op:.2f}"/>'
        for i, j, op in edges
    ]

    node_svg = []
    for x, y, r in nodes:
        if r > 3:
            node_svg.append(
                f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{r * 3.2:.1f}" '
                f'fill="{ACCENT}" opacity="0.07"/>'
            )
        node_svg.append(
            f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{NODE}"/>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Oliver Zhang — AI infrastructure and systems engineering</title>
  <desc id="d">A seeded network on the left and a field of data rain on the right, regenerated daily.</desc>
  <defs>
    <radialGradient id="glowL" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowR" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0.09"/>
      <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="1.6" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="right"><rect x="748" y="0" width="532" height="{H}"/></clipPath>
    <style>
      .mono {{ font-family: {MONO}; }}
    </style>
  </defs>

  <rect width="{W}" height="{H}" fill="#02060b"/>
  <ellipse cx="250" cy="180" rx="360" ry="230" fill="url(#glowL)"/>
  <ellipse cx="1090" cy="170" rx="320" ry="220" fill="url(#glowR)"/>

  <g>
{chr(10).join(edge_svg)}
  </g>
  <g filter="url(#soft)">
{chr(10).join(node_svg)}
  </g>

  <g clip-path="url(#right)">
{chr(10).join(rain)}
  </g>

  <text class="mono" x="{W // 2}" y="178" text-anchor="middle" font-size="52" font-weight="600" letter-spacing="12" fill="{TEXT}">OLIVER</text>
  <text class="mono" x="{W // 2}" y="212" text-anchor="middle" font-size="12.5" letter-spacing="3.2" fill="{TAG}">// AI INFRASTRUCTURE &amp; SYSTEMS ENGINEERING</text>
  <text class="mono" x="{W // 2}" y="330" text-anchor="middle" font-size="9.5" letter-spacing="1.6" fill="{DIM}">NETWORK · SEED {seed:08x} · {date.isoformat()}</text>
</svg>
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="assets/banner.svg")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD; defaults to today (UTC)")
    parser.add_argument("--seed", default=None, help="integer seed; defaults to a hash of the date")
    args = parser.parse_args()

    date = (
        dt.date.fromisoformat(args.date)
        if args.date
        else dt.datetime.now(dt.timezone.utc).date()
    )
    if args.seed is not None:
        seed = int(args.seed)
    else:
        digest = hashlib.sha256(date.isoformat().encode()).digest()
        seed = int.from_bytes(digest[:4], "big")

    svg = build(date, seed)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} (seed {seed:08x}, {date.isoformat()})")


if __name__ == "__main__":
    main()
