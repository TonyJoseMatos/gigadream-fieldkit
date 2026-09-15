#!/usr/bin/env python3
"""One console for Gigadream / Spektraltek / Portal 37."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HELP = """
GIGADREAM FIELDKIT  //  TERRA II console

  python3 fieldkit.py lore [args...]      field kit
  python3 fieldkit.py hangar [args...]    Spektraltek starjets
  python3 fieldkit.py 37 [args...]        Portal 37
  python3 fieldkit.py canon               print rooms
"""


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print(HELP.strip())
        return

    cmd, rest = sys.argv[1], sys.argv[2:]

    if cmd == "canon":
        import canon
        print("ROOMS", ", ".join(canon.ROOMS))
        for room in canon.ROOMS:
            print(f"\n== {room} ==")
            print("  places :", ", ".join(canon.PLACES[room][:4]), "...")
            print("  vessels:", ", ".join(canon.VESSELS[room][:3]), "...")
        return

    mapping = {
        "lore": ROOT / "gigadream.py",
        "hangar": ROOT / "starjets.py",
        "37": ROOT / "portal37.py",
        "portal": ROOT / "portal37.py",
        "jets": ROOT / "starjets.py",
    }
    target = mapping.get(cmd)
    if not target:
        print(HELP.strip())
        raise SystemExit(f"unknown desk: {cmd}")
    raise SystemExit(subprocess.call([sys.executable, str(target), *rest]))


if __name__ == "__main__":
    main()
