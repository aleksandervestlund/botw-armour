import os

from source.helpers import ArmourPiece, IndexGenerator


FONT = ("Arial", 12, "bold")
ARMOUR_WIDTH = 950
TOTALS_WIDTH = 200

DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

STAR = "☆"

_idx_generator = IndexGenerator()

ARMOUR_DATA: dict[str, ArmourPiece] = {
    "Old Shirt": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Well-Worn Trousers": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Champion's Tunic": {
        "upgrades": [
            [("Silent Princess", 3)],
            [("Silent Princess", 3), ("Shard of Farosh's Horn", 2)],
            [("Silent Princess", 3), ("Shard of Naydra's Horn", 2)],
            [("Silent Princess", 3), ("Shard of Dinraal's Horn", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Hylian Hood": {
        "upgrades": [
            [("Bokoblin Horn", 5)],
            [("Bokoblin Horn", 8), ("Bokoblin Fang", 5)],
            [("Bokoblin Fang", 10), ("Bokoblin Guts", 5)],
            [("Bokoblin Guts", 15), ("Amber", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Hylian Tunic": {
        "upgrades": [
            [("Bokoblin Horn", 5)],
            [("Bokoblin Horn", 8), ("Bokoblin Fang", 5)],
            [("Bokoblin Fang", 10), ("Bokoblin Guts", 5)],
            [("Bokoblin Guts", 15), ("Amber", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Hylian Trousers": {
        "upgrades": [
            [("Bokoblin Horn", 5)],
            [("Bokoblin Horn", 8), ("Bokoblin Fang", 5)],
            [("Bokoblin Fang", 10), ("Bokoblin Guts", 5)],
            [("Bokoblin Guts", 15), ("Amber", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Soldier's Helm": {
        "upgrades": [
            [("Chuchu Jelly", 5), ("Bokoblin Guts", 3)],
            [("Keese Eyeball", 3), ("Moblin Guts", 3)],
            [("Lizalfos Tail", 2), ("Hinox Guts", 2)],
            [("Lynel Hoof", 2), ("Lynel Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Soldier's Armor": {
        "upgrades": [
            [("Chuchu Jelly", 5), ("Bokoblin Guts", 3)],
            [("Keese Eyeball", 3), ("Moblin Guts", 3)],
            [("Lizalfos Tail", 3), ("Hinox Guts", 1)],
            [("Lynel Hoof", 2), ("Lynel Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Soldier's Greaves": {
        "upgrades": [
            [("Chuchu Jelly", 5), ("Bokoblin Guts", 3)],
            [("Keese Eyeball", 3), ("Moblin Guts", 3)],
            [("Lizalfos Tail", 3), ("Hinox Guts", 1)],
            [("Lynel Hoof", 2), ("Lynel Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Amber Earrings": {
        "upgrades": [
            [("Amber", 3), ("Flint", 3)],
            [("Amber", 10), ("Flint", 3)],
            [("Amber", 20), ("Flint", 3)],
            [("Amber", 30), ("Flint", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Warm Doublet": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Ruby Circlet": {
        "upgrades": [
            [("Ruby", 2), ("Flint", 3)],
            [("Ruby", 4), ("Flint", 3)],
            [("Ruby", 6), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snowquill Headdress": {
        "upgrades": [
            [("Red Chuchu Jelly", 3)],
            [("Red Chuchu Jelly", 5), ("Warm Safflina", 3)],
            [("Sunshroom", 5), ("Fire Keese Wing", 8)],
            [("Red Lizalfos Tail", 10), ("Ruby", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snowquill Tunic": {
        "upgrades": [
            [("Red Chuchu Jelly", 3)],
            [("Red Chuchu Jelly", 5), ("Warm Safflina", 3)],
            [("Sunshroom", 5), ("Fire Keese Wing", 8)],
            [("Red Lizalfos Tail", 10), ("Ruby", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snowquill Trousers": {
        "upgrades": [
            [("Red Chuchu Jelly", 3)],
            [("Red Chuchu Jelly", 5), ("Warm Safflina", 3)],
            [("Sunshroom", 5), ("Fire Keese Wing", 8)],
            [("Red Lizalfos Tail", 10), ("Ruby", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Sapphire Circlet": {
        "upgrades": [
            [("Sapphire", 2), ("Flint", 3)],
            [("Sapphire", 4), ("Flint", 3)],
            [("Sapphire", 6), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Desert Voe Headband": {
        "upgrades": [
            [("White Chuchu Jelly", 3)],
            [("White Chuchu Jelly", 5), ("Ice Keese Wing", 3)],
            [("Ice Keese Wing", 8), ("Icy Lizalfos Tail", 3)],
            [("Icy Lizalfos Tail", 10), ("Sapphire", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Desert Voe Spaulder": {
        "upgrades": [
            [("White Chuchu Jelly", 3)],
            [("White Chuchu Jelly", 5), ("Ice Keese Wing", 3)],
            [("Ice Keese Wing", 8), ("Icy Lizalfos Tail", 3)],
            [("Icy Lizalfos Tail", 10), ("Sapphire", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Desert Voe Trousers": {
        "upgrades": [
            [("White Chuchu Jelly", 3)],
            [("White Chuchu Jelly", 5), ("Ice Keese Wing", 3)],
            [("Ice Keese Wing", 8), ("Icy Lizalfos Tail", 3)],
            [("Icy Lizalfos Tail", 10), ("Sapphire", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Gerudo Veil": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Gerudo Top": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Gerudo Sirval": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Topaz Earrings": {
        "upgrades": [
            [("Topaz", 2), ("Flint", 3)],
            [("Topaz", 4), ("Flint", 3)],
            [("Topaz", 6), ("Star Fragment", 1)],
            [("Topaz", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Rubber Helm": {
        "upgrades": [
            [("Yellow Chuchu Jelly", 3)],
            [("Yellow Chuchu Jelly", 5), ("Voltfruit", 5)],
            [("Zapshroom", 5), ("Yellow Lizalfos Tail", 5)],
            [("Yellow Lizalfos Tail", 10), ("Topaz", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Rubber Armor": {
        "upgrades": [
            [("Yellow Chuchu Jelly", 3)],
            [("Yellow Chuchu Jelly", 5), ("Voltfruit", 5)],
            [("Zapshroom", 5), ("Yellow Lizalfos Tail", 5)],
            [("Yellow Lizalfos Tail", 10), ("Topaz", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Rubber Tights": {
        "upgrades": [
            [("Yellow Chuchu Jelly", 3)],
            [("Yellow Chuchu Jelly", 5), ("Voltfruit", 5)],
            [("Zapshroom", 5), ("Yellow Lizalfos Tail", 5)],
            [("Yellow Lizalfos Tail", 10), ("Topaz", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Flamebreaker Helm": {
        "upgrades": [
            [("Fireproof Lizard", 1), ("Moblin Horn", 2)],
            [("Fireproof Lizard", 3), ("Moblin Fang", 4)],
            [("Smotherwing Butterfly", 3), ("Moblin Guts", 3)],
            [("Smotherwing Butterfly", 5), ("Hinox Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Flamebreaker Armor": {
        "upgrades": [
            [("Fireproof Lizard", 1), ("Moblin Horn", 2)],
            [("Fireproof Lizard", 3), ("Moblin Fang", 4)],
            [("Smotherwing Butterfly", 3), ("Moblin Guts", 3)],
            [("Smotherwing Butterfly", 5), ("Hinox Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Flamebreaker Boots": {
        "upgrades": [
            [("Fireproof Lizard", 1), ("Moblin Horn", 2)],
            [("Fireproof Lizard", 3), ("Moblin Fang", 4)],
            [("Smotherwing Butterfly", 3), ("Moblin Guts", 3)],
            [("Smotherwing Butterfly", 5), ("Hinox Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Opal Earrings": {
        "upgrades": [
            [("Opal", 3), ("Flint", 3)],
            [("Opal", 8), ("Flint", 3)],
            [("Opal", 16), ("Flint", 3)],
            [("Opal", 20), ("Flint", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zora Helm": {
        "upgrades": [
            [("Lizalfos Horn", 3)],
            [("Lizalfos Talon", 5), ("Hyrule Bass", 5)],
            [("Lizalfos Tail", 5), ("Hearty Bass", 5)],
            [("Lizalfos Tail", 10), ("Opal", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zora Armor": {
        "upgrades": [
            [("Lizalfos Horn", 3)],
            [("Lizalfos Talon", 5), ("Hyrule Bass", 5)],
            [("Lizalfos Tail", 5), ("Hearty Bass", 5)],
            [("Lizalfos Tail", 10), ("Opal", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zora Greaves": {
        "upgrades": [
            [("Lizalfos Horn", 3)],
            [("Lizalfos Talon", 5), ("Hyrule Bass", 5)],
            [("Lizalfos Tail", 5), ("Hearty Bass", 5)],
            [("Lizalfos Tail", 10), ("Opal", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Stealth Mask": {
        "upgrades": [
            [("Blue Nightshade", 3)],
            [("Blue Nightshade", 5), ("Sunset Firefly", 5)],
            [("Silent Shroom", 8), ("Sneaky River Snail", 5)],
            [("Stealthfin Trout", 10), ("Silent Princess", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Stealth Chest Guard": {
        "upgrades": [
            [("Blue Nightshade", 3)],
            [("Blue Nightshade", 5), ("Sunset Firefly", 5)],
            [("Silent Shroom", 8), ("Sneaky River Snail", 5)],
            [("Stealthfin Trout", 10), ("Silent Princess", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Stealth Tights": {
        "upgrades": [
            [("Blue Nightshade", 3)],
            [("Blue Nightshade", 5), ("Sunset Firefly", 5)],
            [("Silent Shroom", 8), ("Sneaky River Snail", 5)],
            [("Stealthfin Trout", 10), ("Silent Princess", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Sheik's Mask": {
        "upgrades": [
            [("Silent Princess", 1), ("Star Fragment", 1)],
            [("Silent Princess", 2), ("Star Fragment", 2)],
            [("Silent Princess", 3), ("Star Fragment", 3)],
            [("Silent Princess", 4), ("Star Fragment", 4)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Thunder Helm": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Climber's Bandana": {
        "upgrades": [
            [("Keese Wing", 3), ("Rushroom", 3)],
            [("Electric Keese Wing", 5), ("Hightail Lizard", 5)],
            [("Ice Keese Wing", 5), ("Hot-Footed Frog", 10)],
            [("Fire Keese Wing", 5), ("Swift Violet", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Climbing Gear": {
        "upgrades": [
            [("Keese Wing", 3), ("Rushroom", 3)],
            [("Electric Keese Wing", 5), ("Hightail Lizard", 5)],
            [("Ice Keese Wing", 5), ("Hot-Footed Frog", 10)],
            [("Fire Keese Wing", 5), ("Swift Violet", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Climbing Boots": {
        "upgrades": [
            [("Keese Wing", 3), ("Rushroom", 3)],
            [("Electric Keese Wing", 5), ("Hightail Lizard", 5)],
            [("Ice Keese Wing", 5), ("Hot-Footed Frog", 10)],
            [("Fire Keese Wing", 5), ("Swift Violet", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Barbarian Helm": {
        "upgrades": [
            [("Lynel Horn", 1)],
            [("Lynel Horn", 3), ("Lynel Hoof", 2)],
            [("Lynel Hoof", 4), ("Lynel Guts", 1)],
            [("Lynel Guts", 2), ("Shard of Dinraal's Horn", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Barbarian Armor": {
        "upgrades": [
            [("Lynel Horn", 1)],
            [("Lynel Horn", 3), ("Lynel Hoof", 2)],
            [("Lynel Hoof", 4), ("Lynel Guts", 1)],
            [("Lynel Guts", 2), ("Shard of Farosh's Horn", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Barbarian Leg Wraps": {
        "upgrades": [
            [("Lynel Horn", 1)],
            [("Lynel Horn", 3), ("Lynel Hoof", 2)],
            [("Lynel Hoof", 4), ("Lynel Guts", 1)],
            [("Lynel Guts", 2), ("Shard of Naydra's Horn", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Fierce Deity Mask": {
        "upgrades": [
            [("Hinox Toenail", 5), ("Dinraal's Scale", 1)],
            [("Hinox Tooth", 5), ("Dinraal's Claw", 1)],
            [("Hinox Guts", 2), ("Shard of Dinraal's Fang", 1)],
            [("Lynel Guts", 2), ("Shard of Dinraal's Horn", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Fierce Deity Armor": {
        "upgrades": [
            [("Hinox Toenail", 5), ("Naydra's Scale", 1)],
            [("Hinox Tooth", 5), ("Naydra's Claw", 1)],
            [("Hinox Guts", 2), ("Shard of Naydra's Fang", 1)],
            [("Lynel Guts", 2), ("Shard of Naydra's Horn", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Fierce Deity Tights": {
        "upgrades": [
            [("Hinox Toenail", 5), ("Farosh's Scale", 1)],
            [("Hinox Tooth", 5), ("Farosh's Claw", 1)],
            [("Hinox Guts", 2), ("Shard of Farosh's Fang", 1)],
            [("Lynel Guts", 2), ("Shard of Farosh's Horn", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Radiant Mask": {
        "upgrades": [
            [("Luminous Stone", 5), ("Bokoblin Guts", 3)],
            [("Luminous Stone", 8), ("Moblin Guts", 3)],
            [("Luminous Stone", 10), ("Molduga Guts", 3)],
            [("Luminous Stone", 20), ("Lynel Guts", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Radiant Shirt": {
        "upgrades": [
            [("Luminous Stone", 5), ("Bokoblin Guts", 3)],
            [("Luminous Stone", 8), ("Moblin Guts", 3)],
            [("Luminous Stone", 10), ("Molduga Guts", 3)],
            [("Luminous Stone", 20), ("Lynel Guts", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Radiant Tights": {
        "upgrades": [
            [("Luminous Stone", 5), ("Bokoblin Guts", 3)],
            [("Luminous Stone", 8), ("Moblin Guts", 3)],
            [("Luminous Stone", 10), ("Molduga Guts", 3)],
            [("Luminous Stone", 20), ("Lynel Guts", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Diamond Circlet": {
        "upgrades": [
            [("Diamond", 2), ("Flint", 3)],
            [("Diamond", 4), ("Flint", 3)],
            [("Diamond", 6), ("Star Fragment", 1)],
            [("Diamond", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Ancient Helm": {
        "upgrades": [
            [("Ancient Screw", 5), ("Ancient Spring", 5)],
            [("Ancient Spring", 15), ("Ancient Gear", 10)],
            [("Ancient Shaft", 15), ("Ancient Core", 5)],
            [("Giant Ancient Core", 2), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Ancient Cuirass": {
        "upgrades": [
            [("Ancient Screw", 5), ("Ancient Spring", 5)],
            [("Ancient Spring", 15), ("Ancient Gear", 10)],
            [("Ancient Shaft", 15), ("Ancient Core", 5)],
            [("Giant Ancient Core", 2), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Ancient Greaves": {
        "upgrades": [
            [("Ancient Screw", 5), ("Ancient Spring", 5)],
            [("Ancient Spring", 15), ("Ancient Gear", 10)],
            [("Ancient Shaft", 15), ("Ancient Core", 5)],
            [("Giant Ancient Core", 2), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Sand Boots": {
        "upgrades": [
            [("Molduga Fin", 5), ("Hightail Lizard", 10)],
            [("Molduga Fin", 10), ("Swift Carrot", 10)],
            [("Molduga Guts", 3), ("Rushroom", 15)],
            [("Molduga Guts", 4), ("Swift Violet", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snow Boots": {
        "upgrades": [
            [("Octorok Tentacle", 5), ("Hightail Lizard", 10)],
            [("Octo Balloon", 5), ("Swift Carrot", 10)],
            [("Octorok Eyeball", 5), ("Rushroom", 15)],
            [("Naydra's Scale", 2), ("Swift Violet", 15)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Bokoblin Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Moblin Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Lizalfos Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Lynel Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Dark Hood": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Dark Tunic": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Dark Trousers": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of Time": {
        "upgrades": [
            [("Amber", 3), ("Star Fragment", 1)],
            [("Amber", 5), ("Star Fragment", 1)],
            [("Amber", 15), ("Star Fragment", 1)],
            [("Amber", 30), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of Time": {
        "upgrades": [
            [("Amber", 3), ("Star Fragment", 1)],
            [("Amber", 5), ("Star Fragment", 1)],
            [("Amber", 15), ("Star Fragment", 1)],
            [("Amber", 30), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of Time": {
        "upgrades": [
            [("Amber", 3), ("Star Fragment", 1)],
            [("Amber", 5), ("Star Fragment", 1)],
            [("Amber", 15), ("Star Fragment", 1)],
            [("Amber", 30), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Wind": {
        "upgrades": [
            [("Opal", 3), ("Star Fragment", 1)],
            [("Opal", 5), ("Star Fragment", 1)],
            [("Opal", 10), ("Star Fragment", 1)],
            [("Opal", 20), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Wind": {
        "upgrades": [
            [("Opal", 3), ("Star Fragment", 1)],
            [("Opal", 5), ("Star Fragment", 1)],
            [("Opal", 10), ("Star Fragment", 1)],
            [("Opal", 20), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Wind": {
        "upgrades": [
            [("Opal", 3), ("Star Fragment", 1)],
            [("Opal", 5), ("Star Fragment", 1)],
            [("Opal", 10), ("Star Fragment", 1)],
            [("Opal", 20), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of Twilight": {
        "upgrades": [
            [("Topaz", 1), ("Star Fragment", 1)],
            [("Topaz", 3), ("Star Fragment", 1)],
            [("Topaz", 5), ("Star Fragment", 1)],
            [("Topaz", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of Twilight": {
        "upgrades": [
            [("Topaz", 1), ("Star Fragment", 1)],
            [("Topaz", 3), ("Star Fragment", 1)],
            [("Topaz", 5), ("Star Fragment", 1)],
            [("Topaz", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of Twilight": {
        "upgrades": [
            [("Topaz", 1), ("Star Fragment", 1)],
            [("Topaz", 3), ("Star Fragment", 1)],
            [("Topaz", 5), ("Star Fragment", 1)],
            [("Topaz", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Sky": {
        "upgrades": [
            [("Sapphire", 1), ("Star Fragment", 1)],
            [("Sapphire", 3), ("Star Fragment", 1)],
            [("Sapphire", 5), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Sky": {
        "upgrades": [
            [("Sapphire", 1), ("Star Fragment", 1)],
            [("Sapphire", 3), ("Star Fragment", 1)],
            [("Sapphire", 5), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Sky": {
        "upgrades": [
            [("Sapphire", 1), ("Star Fragment", 1)],
            [("Sapphire", 3), ("Star Fragment", 1)],
            [("Sapphire", 5), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Hero": {
        "upgrades": [
            [("Ruby", 1), ("Star Fragment", 1)],
            [("Ruby", 3), ("Star Fragment", 1)],
            [("Ruby", 5), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Hero": {
        "upgrades": [
            [("Ruby", 1), ("Star Fragment", 1)],
            [("Ruby", 3), ("Star Fragment", 1)],
            [("Ruby", 5), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Hero": {
        "upgrades": [
            [("Ruby", 1), ("Star Fragment", 1)],
            [("Ruby", 3), ("Star Fragment", 1)],
            [("Ruby", 5), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Wild": {
        "upgrades": [
            [("Acorn", 10), ("Farosh's Scale", 2)],
            [("Courser Bee Honey", 5), ("Farosh's Claw", 2)],
            [("Energetic Rhino Beetle", 5), ("Shard of Farosh's Fang", 2)],
            [("Star Fragment", 1), ("Shard of Farosh's Horn", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Wild": {
        "upgrades": [
            [("Acorn", 10), ("Naydra's Scale", 2)],
            [("Courser Bee Honey", 5), ("Naydra's Claw", 2)],
            [("Energetic Rhino Beetle", 5), ("Shard of Naydra's Fang", 2)],
            [("Star Fragment", 1), ("Shard of Naydra's Horn", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Wild": {
        "upgrades": [
            [("Acorn", 10), ("Dinraal's Scale", 2)],
            [("Courser Bee Honey", 5), ("Dinraal's Claw", 2)],
            [("Energetic Rhino Beetle", 5), ("Shard of Dinraal's Fang", 2)],
            [("Star Fragment", 1), ("Shard of Dinraal's Horn", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Nintendo Switch Shirt": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Korok Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Majora's Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Tingle's Hood": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Tingle's Shirt": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Tingle's Tights": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Midna's Helmet": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Phantom Helmet": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Phantom Armor": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Phantom Greaves": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Island Lobster Shirt": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Ravio's Hood": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Zant's Helmet": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Royal Guard Cap": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Royal Guard Uniform": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Royal Guard Boots": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Phantom Ganon Skull": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Phantom Ganon Armor": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Phantom Ganon Greaves": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Ruta Divine Helm": {
        "upgrades": [
            [("Ancient Screw", 5), ("Ancient Spring", 5)],
            [("Ancient Spring", 15), ("Ancient Gear", 10)],
            [("Ancient Shaft", 15), ("Ancient Core", 5)],
            [("Giant Ancient Core", 2), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Medoh Divine Helm": {
        "upgrades": [
            [("Ancient Screw", 5), ("Ancient Spring", 5)],
            [("Ancient Spring", 15), ("Ancient Gear", 10)],
            [("Ancient Shaft", 15), ("Ancient Core", 5)],
            [("Giant Ancient Core", 2), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Rudania Divine Helm": {
        "upgrades": [
            [("Ancient Screw", 5), ("Ancient Spring", 5)],
            [("Ancient Spring", 15), ("Ancient Gear", 10)],
            [("Ancient Shaft", 15), ("Ancient Core", 5)],
            [("Giant Ancient Core", 2), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Naboris Divine Helm": {
        "upgrades": [
            [("Ancient Screw", 5), ("Ancient Spring", 5)],
            [("Ancient Spring", 15), ("Ancient Gear", 10)],
            [("Ancient Shaft", 15), ("Ancient Core", 5)],
            [("Giant Ancient Core", 2), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Salvager Headwear": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Salvager Vest": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Salvager Trousers": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
}
