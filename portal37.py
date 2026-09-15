#!/usr/bin/env python3
"""PORTAL 37 — unlisted TERRA II gate / board router (canon-backed)"""

import argparse
import random
import textwrap

import canon

ROOMS = list(canon.ROOMS)


def punch(origin=None, exit_=None):
    origin = origin or random.choice(ROOMS)
    others = [r for r in ROOMS if r != origin] or ROOMS
    exit_ = exit_ or random.choice(others)
    return {
        "ticket": f"P37-{random.choice('XYZQR')}{random.randint(10, 99)}",
        "origin": origin,
        "exit": exit_,
        "cargo": random.choice(canon.VESSELS[origin]),
        "arrival": random.choice(canon.VESSELS[exit_]),
        "from_site": random.choice(canon.PLACES[origin]),
        "to_site": random.choice(canon.PLACES[exit_]),
        "hazard": random.choice(canon.HAZARDS),
        "film": random.choice(canon.FILM),
        "style": ", ".join(random.sample(canon.STYLE, 4)),
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
        f"{t['exit']}, shot on {t['film']}, {t['style']}, "
        f"hyper-kinetic climax frame, full-bleed frame"
    )


def main():
    p = argparse.ArgumentParser(prog="portal37")
    p.add_argument(
        "mode",
        nargs="?",
        default="open",
        choices=["open", "prompt", "route", "pack"],
    )
    p.add_argument("src", nargs="?", choices=ROOMS)
    p.add_argument("dst", nargs="?", choices=ROOMS)
    p.add_argument("-n", type=int, default=1)
    p.add_argument("--seed", type=int)
    args = p.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.mode == "route":
        if not (args.src and args.dst):
            raise SystemExit("usage: fieldkit.py 37 route DARK HANGAR")
        t = punch(args.src, args.dst)
        print(ticket(t))
        print()
        print(prompt(t))
        return

    if args.mode == "pack":
        n = args.n if args.n > 1 else 12
        for i in range(n):
            print(f"{i + 1:02d}. {prompt(punch(args.src, args.dst))}")
        return

    for i in range(args.n):
        t = punch(args.src, args.dst)
        print(prompt(t) if args.mode == "prompt" else ticket(t))
        if i < args.n - 1:
            print("\n" + "-" * 42 + "\n")


if __name__ == "__main__":
    main()
