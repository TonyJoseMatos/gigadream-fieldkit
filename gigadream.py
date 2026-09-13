#!/usr/bin/env python3
"""GIGADREAM field kit — Diamond Riot / Beachpunk / TERRA II"""

import argparse
import random
import sys
import textwrap
import time
from datetime import datetime
from pathlib import Path

BOARDS = {
    "FRINGE": {
        "place": [
            "glitch mangrove",
            "voxel tidepool",
            "broken GPS shrine",
            "pirated cell-tower chapel",
            "memetic dumpster reef",
            "off-grid Loiza backlot",
            "datamosh boardwalk",
        ],
        "vessel": [
            "DIY Pepe-bot",
            "Wojack salvage walker",
            "glitch-orisha drone",
            "anime-kernel crab tank",
            "voxel alchemist rig",
            "bootleg samurai modem",
            "unstable glyph printer",
        ],
        "spirit": [
            "corrupted carnival saint",
            "bootleg Taíno daemon",
            "error-cult witness",
            "beachpunk seraph in compression artifacts",
        ],
        "weather": [
            "codec storm",
            "rainbow banding squall",
            "jpeg heat death",
            "hurricane static",
            "purple blocking fog",
        ],
    },
    "POSH": {
        "place": [
            "Rincon glass villa",
            "diamond-cut tide deck",
            "Condado chrome atrium",
            "salt-white editorial beach",
            "luxury bunker at Isabela",
            "gold-hour product stage",
        ],
        "vessel": [
            "latinobionic couture chassis",
            "diamond-riot emitter clutch",
            "sandtech jewelry armature",
            "orisha-modem heel",
            "77K product monolith",
            "gigabionic perfume reliquary",
        ],
        "spirit": [
            "orisha of chrome",
            "saint of wet gold",
            "editorial ghost in Ektar red",
            "luxury riot angel",
        ],
        "weather": [
            "gold-hour EMP",
            "polished salt flare",
            "wet neon afterstorm",
            "clean whiteout luxury haze",
        ],
    },
    "DARK": {
        "place": [
            "TERRA II blackout beach",
            "Guayama salt graves",
            "Lost Coast fogline",
            "Culebra midnight antenna",
            "cathedral of rusted rebar",
            "after-gate Rincon",
            "Isabela dune antenna",
            "Loiza breakwater",
        ],
        "vessel": [
            "salvagecore uplink coffin",
            "dead satellite shrine",
            "riot-blade without a hand",
            "sandtech ossuary rig",
            "blackout carnival float",
            "orisha war-modem",
            "latinobionic chassis",
        ],
        "spirit": [
            "cyber-orisha in mourning chrome",
            "TERRA II witness",
            "Taíno glyph-current",
            "saint of rusted chrome",
            "masterless sword",
            "beachpunk psychopomp",
        ],
        "weather": [
            "blackout carnival",
            "violet heat shimmer",
            "whiteout salt",
            "blood-gold eclipse tide",
            "hurricane static after the lights die",
        ],
    },
}

FILM = [
    "Kodak Ektar 100",
    "77K UHD overcrank",
    "distressed analog halo",
    "kitchcore grain",
    "chemical light leak slash",
    "halation bloom",
    "pushed film reds",
    "salt-scratched gate",
    "retro-wave religious sci-fi grade",
]

STYLE = [
    "beachpunk gigadream",
    "diamond riot chaos",
    "latinobionic futurism",
    "hyper sandtech",
    "hallucinatory cinematic still",
    "hyper-kinetic climax frame",
    "Taíno / cyber-orisha fusion",
    "salvagecore reliquary",
    "no readable text",
    "no watermark",
]

TITLE_FORMS = [
    "SWORDS WITH NO MASTERS",
    "TERRA II: {place}",
    "THE {thing} RIOT",
    "GIGADREAM // {thing}",
    "{place} AFTER THE GATE",
    "NO PLACE LIKE {place}",
    "DIAMOND RIOT: {thing}",
    "LOST COAST {thing}",
]

CREATURES = [
    r"""
        .-~~~~-.
       /  o  o  \      {name}
      |   __    |     {board} specimen
       \  ''   /      {place}
      .-`===='-.
     /  sandtech \
    /____riot_____\
      T         T
""",
    r"""
      ,-=====-.
     /  (\\//)  \     {name}
    |  /o    o\  |    {board}
     \  \____/  /     {place}
    _/ salvage \_
   (____RIOT____)
      / /   \ \
""",
    r"""
         /\
        /  \          {name}
       /_or_\         {board} glyph
      | o  o |        {place}
      |  ▽   |
     / \ /\ / \
    /gig/  \dream\
""",
    r"""
     .--------.
    /  /\  /\  \      {name}
   |  | Tam |  |     beachpunk walker
   |  |  o  |  |     {board} / {place}
    \  V--V  /
    /| diamond |\
   /_|  riot  |_\
     ""      ""
""",
]

def article(word):
    return "an" if word[:1].lower() in "aeiou" else "a"

def blend(board=None):
    name = board or random.choice(list(BOARDS))
    bag = BOARDS[name]
    return {
        "board": name,
        "place": random.choice(bag["place"]),
        "vessel": random.choice(bag["vessel"]),
        "spirit": random.choice(bag["spirit"]),
        "weather": random.choice(bag["weather"]),
        "film": random.choice(FILM),
        "style": ", ".join(random.sample(STYLE, 4)),
    }

def title_from(b):
    vessel = b["vessel"]
    blade = any(w in vessel.lower() for w in ("sword", "blade"))
    forms = [f for f in TITLE_FORMS if "SWORDS" not in f or blade]
    form = random.choice(forms or TITLE_FORMS)
    thing = vessel.split()[-1].upper()
    place = b["place"].split()[0].upper()
    return f"{form.format(thing=thing, place=place)}  [{b['board']}]"

def title(board=None):
    return title_from(blend(board))

def transmission(b):
    body = (
        f"A {b['spirit']} mounts {article(b['vessel'])} {b['vessel']} "
        f"at {b['place']} under {b['weather']}, photographed on {b['film']}. "
        f"{b['style']}. The riot does not ask permission."
    )
    return "\n".join(
        [
            f"BOARD    {b['board']}",
            f"SITE     {b['place']}",
            f"VESSEL   {b['vessel']}",
            f"WITNESS  {b['spirit']}",
            f"WEATHER  {b['weather']}",
            f"STOCK    {b['film']}",
            "",
            "TRANSMISSION",
            textwrap.fill(body, 64),
        ]
    )

def oracle(board=None):
    return transmission(blend(board))

def prompt(board=None, extra=""):
    b = blend(board)
    shot = (
        f"[{b['board']}] {b['spirit']} with {article(b['vessel'])} {b['vessel']} "
        f"at {b['place']}, {b['weather']}, shot on {b['film']}, {b['style']}, "
        f"cinematic still, ultra detailed, full-bleed frame"
    )
    if extra:
        shot += f", {extra}"
    return shot

def viz(extra=""):
    b = blend("POSH")
    bits = [
        "photoreal product visualization",
        "hero object on a salt-white seamless",
        b["vessel"],
        b["place"],
        b["spirit"],
        "studio key light + rim",
        "wet chrome condensation",
        b["film"],
        "beachpunk luxury still",
        "diamond riot product frame",
        "no readable text",
        extra or "editorial catalog energy",
    ]
    return ", ".join(bits)

def ascii_card(board=None):
    b = blend(board)
    art = random.choice(CREATURES).format(
        name=b["vessel"].upper(),
        board=b["board"],
        place=b["place"],
    )
    return art + "\n" + title_from(b) + "\n\n" + transmission(b)

def write_pack(path, n=50, board=None, extra=""):
    lines = [
        "# GIGADREAM PROMPT PACK",
        f"# {datetime.now().isoformat(timespec='seconds')}",
        f"# board={board or 'MIX'} count={n}",
        "# style lock: beachpunk gigadream / diamond riot / TERRA II",
        "",
    ]
    for i in range(1, n + 1):
        lines.append(f"{i:02d}. {prompt(board, extra)}")
        lines.append("")
    Path(path).write_text("\n".join(lines), encoding="utf-8")
    return path

def main():
    p = argparse.ArgumentParser(prog="gigadream")
    p.add_argument(
        "mode",
        nargs="?",
        default="oracle",
        choices=["oracle", "prompt", "title", "ascii", "pack", "boards", "viz", "watch"],
    )
    p.add_argument("--board", "-b", choices=["FRINGE", "POSH", "DARK"])
    p.add_argument("--count", "-n", type=int, default=1)
    p.add_argument("--out", default="gigadream_pack.txt")
    p.add_argument("--seed", type=int)
    p.add_argument("--spice", default="")
    p.add_argument("--sec", type=float, default=4.0)
    args = p.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.mode == "boards":
        for name, bag in BOARDS.items():
            print(f"== {name} ==")
            for k, v in bag.items():
                print(f"  {k}: {', '.join(v)}")
            print()
        return

    if args.mode == "pack":
        n = args.count if args.count > 1 else 50
        path = write_pack(args.out, n=n, board=args.board, extra=args.spice)
        print(f"wrote {path}")
        return

    if args.mode == "viz":
        for i in range(args.count):
            print(viz(args.spice))
            if i < args.count - 1:
                print("\n" + "-" * 42 + "\n")
        return

    if args.mode == "watch":
        board = args.board or "DARK"
        try:
            while True:
                print("\033c", end="")
                print(ascii_card(board))
                print("\nctrl+c to kill")
                time.sleep(args.sec)
        except KeyboardInterrupt:
            print("\nfield kit closed")
        return

    fn = {
        "oracle": oracle,
        "prompt": lambda board=None: prompt(board, args.spice),
        "title": title,
        "ascii": ascii_card,
    }[args.mode]

    for i in range(args.count):
        print(fn(args.board))
        if i < args.count - 1:
            print("\n" + "-" * 42 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)