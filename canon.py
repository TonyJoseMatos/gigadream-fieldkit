"""GIGADREAM CANON — one bible for field kit, hangar, and Portal 37."""

BOARDS = ("FRINGE", "POSH", "DARK")
ROOMS = ("FRINGE", "POSH", "DARK", "HANGAR", "LOST")

PLACES = {
    "FRINGE": [
        "glitch mangrove", "voxel tidepool", "broken GPS shrine",
        "pirated cell-tower chapel", "memetic dumpster reef",
        "off-grid Loiza backlot", "datamosh boardwalk",
    ],
    "POSH": [
        "Rincon glass villa", "diamond-cut tide deck", "Condado chrome atrium",
        "salt-white editorial beach", "luxury bunker at Isabela",
        "gold-hour product stage",
    ],
    "DARK": [
        "TERRA II blackout beach", "Guayama salt graves", "Lost Coast fogline",
        "Culebra midnight antenna", "cathedral of rusted rebar",
        "after-gate Rincon", "Isabela dune antenna", "Loiza breakwater",
    ],
    "HANGAR": [
        "Spektraltek salt apron", "prism-core service bay", "star-wake taxiway",
    ],
    "LOST": [
        "after-gate Rincon", "unmapped thirty-seventh door",
        "pre-Spektraltek airship grave",
    ],
}

VESSELS = {
    "FRINGE": [
        "DIY Pepe-bot", "Wojack salvage walker", "glitch-orisha drone",
        "anime-kernel crab tank", "voxel alchemist rig",
        "bootleg samurai modem", "unstable glyph printer",
    ],
    "POSH": [
        "latinobionic couture chassis", "diamond-riot emitter clutch",
        "sandtech jewelry armature", "orisha-modem heel",
        "77K product monolith", "gigabionic perfume reliquary",
    ],
    "DARK": [
        "salvagecore uplink coffin", "dead satellite shrine",
        "riot-blade without a hand", "sandtech ossuary rig",
        "blackout carnival float", "orisha war-modem", "latinobionic chassis",
    ],
    "HANGAR": [
        "needle-foil interceptor", "salt-scored dropship", "choir-engine bomber",
        "orisha-keel courier", "blackout carnival gunship",
        "dune-antenna scout", "reliquary tanker", "masterless blade-wing",
    ],
    "LOST": [
        "unnamed airship keel", "pre-Spektraltek choir bell", "door with no number",
    ],
}

SPIRITS = {
    "FRINGE": [
        "corrupted carnival saint", "bootleg Taíno daemon",
        "error-cult witness", "beachpunk seraph in compression artifacts",
    ],
    "POSH": [
        "orisha of chrome", "saint of wet gold",
        "editorial ghost in Ektar red", "luxury riot angel",
    ],
    "DARK": [
        "cyber-orisha in mourning chrome", "TERRA II witness",
        "Taíno glyph-current", "saint of rusted chrome",
        "masterless sword", "beachpunk psychopomp",
    ],
    "HANGAR": ["Spektraltek floor saint", "star-wake usher"],
    "LOST": ["door that remembers airships", "unlisted gatekeeper"],
}

WEATHER = {
    "FRINGE": [
        "codec storm", "rainbow banding squall", "jpeg heat death",
        "hurricane static", "purple blocking fog",
    ],
    "POSH": [
        "gold-hour EMP", "polished salt flare",
        "wet neon afterstorm", "clean whiteout luxury haze",
    ],
    "DARK": [
        "blackout carnival", "violet heat shimmer", "whiteout salt",
        "blood-gold eclipse tide", "hurricane static after the lights die",
    ],
    "HANGAR": ["prism-core shimmer", "taxiway salt blow"],
    "LOST": ["unmapped weather", "gate flicker"],
}

DRIVES = [
    "spektraltek prism core", "77K film-gate thruster", "glyph-current ram",
    "salvagecore afterburner", "Taíno star-wake coil", "diamond-riot pulse lattice",
]

LIVERIES = [
    "Ektar red over wet chrome", "whiteout salt camo", "violet heat-shimmer foil",
    "kitchcore grain gold", "mourning-chrome blackout",
    "blood-gold eclipse bands", "light-leak slash decals",
]

SQUADRONS = [
    "NO PLACE LIKE HOME", "SWORDS WITH NO MASTERS", "AFTER-GATE RINCON",
    "CULEBRA MIDNIGHT", "LOIZA BREAKWATER", "TERRA II WITNESS",
]

FILM = [
    "Kodak Ektar 100", "77K UHD overcrank", "distressed analog halo",
    "kitchcore grain", "chemical light leak slash", "halation bloom",
    "pushed film reds", "salt-scratched gate", "retro-wave religious sci-fi grade",
]

STYLE = [
    "beachpunk gigadream", "diamond riot chaos", "latinobionic futurism",
    "hyper sandtech", "hallucinatory cinematic still", "hyper-kinetic climax frame",
    "Taíno / cyber-orisha fusion", "salvagecore reliquary",
    "no readable text", "no watermark",
]

HAZARDS = [
    "halation bloom eats the callsign",
    "board leakage — POSH chrome on a DARK hull",
    "time smear: airship and starjet occupy one frame",
    "glyph-current feedback, brief saint visible",
    "salt-scratched gate, serial numbers refuse to stick",
    "Portal 37 flickers; treat destination as rumor",
]


def article(word):
    return "an" if word[:1].lower() in "aeiou" else "a"
