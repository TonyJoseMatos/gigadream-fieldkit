#!/usr/bin/env python3
"""SPEKTRALTEK HANGAR — TERRA II starjet flight computer (canon-backed)"""

import argparse
import random
import textwrap

import canon

MISSIONS = [
    "skim the Lost Coast fogline and photograph the gate",
    "escort a latinobionic chassis off Isabela dune antenna",
    "drop a salvagecore reliquary into Guayama salt graves",
    "hold blackout carnival airspace until the choir dies",
    "cut a star-wake over Culebra midnight antenna",
    "retrieve a masterless sword from an airship wreck",
]

SILHOUETTES = [
    r"""
          /\
         /  \          {call}
        /====\         {hull}
    ___/ SPEK \___     {squad}
   /  \  TEK  /  \
   \__/=======\__/
     //       \\
    *'  star    '*
""",
    r"""
        __/\__
       /      \        {call}
    __/  ####  \__     {hull}
   /  SPEKTRALTEK \    {squad}
   \____ JET _____/
      //      \\
     **  wake  **
""",
]


def article(word):
    return canon.article(word)


def mint(seed=None):
    if seed is not None:
        random.seed(seed)
    hull = random.choice(canon.VESSELS["HANGAR"])
    tag = random.choice("ABCDEFGH") + str(random.randint(10, 99))
    return {
        "call": f"STJ-{tag}",
        "hull": hull,
        "drive": random.choice(canon.DRIVES),
        "livery": random.choice(canon.LIVERIES),
        "squad": random.choice(canon.SQUADRONS),
        "mission": random.choice(MISSIONS),
        "site": random.choice(canon.PLACES["HANGAR"] + canon.PLACES["DARK"]),
        "film": random.choice(canon.FILM),
    }


def dossier(j):
    return "\n".join(
        [
            "SPEKTRALTEK HANGAR  //  TERRA II",
            f"CALL     {j['call']}",
            f"HULL     {j['hull']}",
            f"DRIVE    {j['drive']}",
            f"LIVERY   {j['livery']}",
            f"SQUAD    {j['squad']}",
            f"SITE     {j['site']}",
            f"STOCK    {j['film']}",
            "",
            "MISSION",
            textwrap.fill(j["mission"], 64),
        ]
    )


def silhouette(j):
    art = random.choice(SILHOUETTES).format(
        call=j["call"], hull=j["hull"], squad=j["squad"]
    )
    return art + "\n" + dossier(j)


def prompt(j):
    return (
        f"photoreal cinematic still of {article(j['hull'])} {j['hull']} "
        f"starjet, Spektraltek markings {j['call']}, {j['livery']}, "
        f"{j['drive']} glowing, parked over {j['site']}, "
        f"Beachpunk Gigadream Diamond Riot, TERRA II, "
        f"shot on {j['film']}, hyper-kinetic climax frame, "
        f"no readable text, no watermark, full-bleed frame"
    )


def roster(n=5):
    lines = ["SPEKTRALTEK ROSTER", ""]
    for _ in range(n):
        j = mint()
        lines.append(f"{j['call']:8}  {j['hull']:28}  {j['squad']}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(prog="starjets")
    p.add_argument(
        "mode",
        nargs="?",
        default="hangar",
        choices=["hangar", "prompt", "roster", "mission"],
    )
    p.add_argument("-n", "--count", type=int, default=1)
    p.add_argument("--seed", type=int)
    args = p.parse_args()

    if args.mode == "roster":
        print(roster(max(args.count, 5)))
        return

    for i in range(args.count):
        j = mint(args.seed if args.count == 1 else None)
        if args.mode == "prompt":
            print(prompt(j))
        elif args.mode == "mission":
            print(dossier(j))
        else:
            print(silhouette(j))
        if i < args.count - 1:
            print("\n" + "-" * 42 + "\n")


if __name__ == "__main__":
    main()