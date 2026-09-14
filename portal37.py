#!/usr/bin/env python3
"""PORTAL 37 — unlisted TERRA II gate / board router"""

import argparse
import random
import textwrap

ORIGINS = ["FRINGE", "POSH", "DARK", "HANGAR"]
EXITS = ["FRINGE", "POSH", "DARK", "HANGAR", "LOST"]

CARGO = {
    "FRINGE": ["Wojack salvage walker", "anime-kernel crab tank", "bootleg samurai modem"],
    "POSH": ["diamond-riot emitter clutch", "orisha-modem heel", "77K product monolith"],
    "DARK": ["salvagecore uplink coffin", "orisha war-modem", "riot-blade without a hand"],
    "HANGAR": ["salt-scored dropship", "orisha-keel courier", "masterless blade-wing"],
    "LOST": ["unnamed airship keel", "pre-Spektraltek choir bell", "door with no number"],
}

SITES = {
    "FRINGE": "datamosh boardwalk",
    "POSH": "gold-hour product stage",
    "DARK": "Culebra midnight antenna",
    "HANGAR": "Spektraltek salt apron",
    "LOST": "after-gate Rincon",
}

HAZARDS = [
    "halation bloom eats the callsign",
    "board leakage — POSH chrome on a DARK hull",
    "time smear: airship and starjet occupy one frame",
    "glyph-current feedback, brief saint visible",
    "salt-scratched gate, serial numbers refuse to stick",
    "Portal 37 flickers; treat destination as rumor",
]


def punch():
    origin = random.choice(ORIGINS)
    exit_ = random.choice([e for e in EXITS if e != origin] or EXITS)
    return {
        "ticket": f"P37-{random.choice('XYZQ')}{random.randint(10, 99)}",
        "origin": origin,
        "exit": exit_,
        "cargo": random.choice(CARGO[origin]),
        "arrival": random.choice(CARGO[exit_]),
        "from_site": SITES[origin],
        "to_site": SITES[exit_],
        "hazard": random.choice(HAZARDS),
    }


def ticket(t):
    return "\n".join(
        [
            "╔══════════════════════════════════════╗",
            "║  PORTAL 37   UNLISTED GATE           ║",
            "║  TERRA II  //  SPEKTRALTEK CLEARANCE ║",
            "╚══════════════════════════════════════╝",
            f"TICKET   {t['ticket']}",
            f"ORIGIN   {t['origin']}  @ {t['from_site']}",
            f"EXIT     {t['exit']}  @ {t['to_site']}",
            f"CARGO    {t['cargo']}",
            f"ARRIVAL  {t['arrival']}",
            "",
            "HAZARD",
            textwrap.fill(t["hazard"], 64),
            "",
            "The thirty-sixth door is mapped.",
            "The thirty-seventh is a rumor that opens.",
        ]
    )


def prompt(t):
    return (
        f"cinematic still of Portal 37 opening between {t['from_site']} "
        f"and {t['to_site']}, {t['cargo']} entering, {t['arrival']} exiting, "
        f"Spektraltek / Diamond Riot / TERRA II, {t['origin']} leaking into "
        f"{t['exit']}, Kodak Ektar 100, 77K UHD, halation bloom, "
        f"hyper-kinetic climax frame, no readable text, no watermark, "
        f"full-bleed frame"
    )


def route(src, dst):
    cargo = random.choice(CARGO.get(src, CARGO["DARK"]))
    arrival = random.choice(CARGO.get(dst, CARGO["LOST"]))
    t = {
        "ticket": f"P37-R{random.randint(10, 99)}",
        "origin": src,
        "exit": dst,
        "cargo": cargo,
        "arrival": arrival,
        "from_site": SITES.get(src, SITES["LOST"]),
        "to_site": SITES.get(dst, SITES["LOST"]),
        "hazard": random.choice(HAZARDS),
    }
    return t


def main():
    p = argparse.ArgumentParser(prog="portal37")
    p.add_argument(
        "mode",
        nargs="?",
        default="open",
        choices=["open", "prompt", "route", "pack"],
    )
    p.add_argument("src", nargs="?", choices=ORIGINS)
    p.add_argument("dst", nargs="?", choices=list(SITES))
    p.add_argument("-n", type=int, default=1)
    args = p.parse_args()

    if args.mode == "route":
        if not (args.src and args.dst):
            raise SystemExit("usage: portal37.py route DARK POSH")
        t = route(args.src, args.dst)
        print(ticket(t))
        print()
        print(prompt(t))
        return

    if args.mode == "pack":
        for i in range(args.n if args.n > 1 else 12):
            print(f"{i + 1:02d}. {prompt(punch())}")
        return

    for i in range(args.n):
        t = punch()
        print(prompt(t) if args.mode == "prompt" else ticket(t))
        if i < args.n - 1:
            print("\n" + "-" * 42 + "\n")


if __name__ == "__main__":
    main()
