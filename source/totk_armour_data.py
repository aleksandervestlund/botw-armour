from source.helpers import ArmourPiece, IndexGenerator


_idx_generator = IndexGenerator()

# fmt: off
TOTK_ARMOUR_DATA: dict[str, ArmourPiece] = {
    "Archaic Tunic": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Archaic Legwear": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Archaic Warm Greaves": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Hylian Hood": {
        "upgrades": [
            [("Bokoblin Horn", 5)],
            [("Blue Bokoblin Horn", 5), ("Bokoblin Fang", 3)],
            [("Amber", 20), ("Black Bokoblin Horn", 5), ("Bokoblin Guts", 3)],
            [("Amber", 30), ("Bokoblin Guts", 3), ("Silver Bokoblin Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Hylian Hood Down": {
        "upgrades": [
            [("Bokoblin Horn", 5)],
            [("Blue Bokoblin Horn", 5), ("Bokoblin Fang", 3)],
            [("Amber", 20), ("Black Bokoblin Horn", 5), ("Bokoblin Guts", 3)],
            [("Amber", 30), ("Bokoblin Guts", 3), ("Silver Bokoblin Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Hylian Tunic": {
        "upgrades": [
            [("Bokoblin Horn", 5)],
            [("Blue Bokoblin Horn", 5), ("Bokoblin Fang", 3)],
            [("Amber", 20), ("Black Bokoblin Horn", 5), ("Bokoblin Guts", 3)],
            [("Amber", 30), ("Bokoblin Guts", 3), ("Silver Bokoblin Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Hylian Trousers": {
        "upgrades": [
            [("Bokoblin Horn", 5)],
            [("Blue Bokoblin Horn", 5), ("Bokoblin Fang", 3)],
            [("Amber", 20), ("Black Bokoblin Horn", 5), ("Bokoblin Guts", 3)],
            [("Amber", 30), ("Bokoblin Guts", 3), ("Silver Bokoblin Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Soldier's Helm": {
        "upgrades": [
            [("Bokoblin Guts", 3), ("Chuchu Jelly", 5)],
            [("Keese Eyeball", 5), ("Moblin Guts", 3)],
            [("Flint", 30), ("Hinox Guts", 3), ("Lizalfos Tail", 3)],
            [("Amber", 30), ("Lynel Guts", 5), ("Lynel Hoof", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Soldier's Armor": {
        "upgrades": [
            [("Bokoblin Guts", 3), ("Chuchu Jelly", 5)],
            [("Keese Eyeball", 5), ("Moblin Guts", 3)],
            [("Flint", 30), ("Hinox Guts", 3), ("Lizalfos Tail", 3)],
            [("Amber", 30), ("Lynel Guts", 5), ("Lynel Hoof", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Soldier's Greaves": {
        "upgrades": [
            [("Bokoblin Guts", 3), ("Chuchu Jelly", 5)],
            [("Keese Eyeball", 5), ("Moblin Guts", 3)],
            [("Flint", 30), ("Hinox Guts", 3), ("Lizalfos Tail", 3)],
            [("Amber", 30), ("Lynel Guts", 5), ("Lynel Hoof", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snowquill Headdress": {
        "upgrades": [
            [("Red Chuchu Jelly", 3)],
            [("Red Chuchu Jelly", 5), ("Warm Safflina", 3)],
            [("Fire Keese Wing", 5), ("Fire-Breath Lizalfos Tail", 3), ("Sunshroom", 5)],
            [("Ruby", 5), ("Fire-Breath Lizalfos Horn", 5), ("Fire-Breath Lizalfos Tail", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snowquill Tunic": {
        "upgrades": [
            [("Red Chuchu Jelly", 3)],
            [("Red Chuchu Jelly", 5), ("Warm Safflina", 3)],
            [("Fire Keese Wing", 5), ("Fire-Breath Lizalfos Tail", 3), ("Sunshroom", 5)],
            [("Ruby", 5), ("Fire-Breath Lizalfos Horn", 5), ("Fire-Breath Lizalfos Tail", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snowquill Trousers": {
        "upgrades": [
            [("Red Chuchu Jelly", 3)],
            [("Red Chuchu Jelly", 5), ("Warm Safflina", 3)],
            [("Fire Keese Wing", 5), ("Fire-Breath Lizalfos Tail", 3), ("Sunshroom", 5)],
            [("Ruby", 5), ("Fire-Breath Lizalfos Horn", 5), ("Fire-Breath Lizalfos Tail", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Flamebreaker Helm": {
        "upgrades": [
            [("Moblin Horn", 3)],
            [("Fireproof Lizard", 5), ("Moblin Fang", 5)],
            [("Smotherwing Butterfly", 3), ("Flint", 15), ("Blue Moblin Horn", 5)],
            [("Smotherwing Butterfly", 5), ("Flint", 30), ("Black Moblin Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Flamebreaker Armor": {
        "upgrades": [
            [("Moblin Horn", 3)],
            [("Fireproof Lizard", 5), ("Moblin Fang", 5)],
            [("Smotherwing Butterfly", 3), ("Flint", 15), ("Blue Moblin Horn", 5)],
            [("Smotherwing Butterfly", 5), ("Flint", 30), ("Black Moblin Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Flamebreaker Boots": {
        "upgrades": [
            [("Moblin Horn", 3)],
            [("Fireproof Lizard", 5), ("Moblin Fang", 5)],
            [("Smotherwing Butterfly", 3), ("Flint", 15), ("Blue Moblin Horn", 5)],
            [("Smotherwing Butterfly", 5), ("Flint", 30), ("Black Moblin Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zora Helm": {
        "upgrades": [
            [("Lizalfos Horn", 3)],
            [("Hyrule Bass", 5), ("Lizalfos Talon", 5)],
            [("Hearty Bass", 3), ("Blue Lizalfos Horn", 5), ("Lizalfos Tail", 3)],
            [("Opal", 20), ("Black Lizalfos Horn", 5), ("Blue Lizalfos Tail", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zora Armor": {
        "upgrades": [
            [("Lizalfos Horn", 3)],
            [("Hyrule Bass", 5), ("Lizalfos Talon", 5)],
            [("Hearty Bass", 3), ("Blue Lizalfos Horn", 5), ("Lizalfos Tail", 3)],
            [("Opal", 20), ("Black Lizalfos Horn", 5), ("Blue Lizalfos Tail", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zora Greaves": {
        "upgrades": [
            [("Lizalfos Horn", 3)],
            [("Hyrule Bass", 5), ("Lizalfos Talon", 5)],
            [("Hearty Bass", 3), ("Blue Lizalfos Horn", 5), ("Lizalfos Tail", 3)],
            [("Opal", 20), ("Black Lizalfos Horn", 5), ("Blue Lizalfos Tail", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Desert Voe Headband": {
        "upgrades": [
            [("White Chuchu Jelly", 3)],
            [("White Chuchu Jelly", 5), ("Cool Safflina", 3)],
            [("Ice Keese Wing", 5), ("Ice-Breath Lizalfos Tail", 3), ("Chillshroom", 5)],
            [("Sapphire", 5), ("Ice-Breath Lizalfos Horn", 5), ("Ice-Breath Lizalfos Tail", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Desert Voe Spaulder": {
        "upgrades": [
            [("White Chuchu Jelly", 3)],
            [("White Chuchu Jelly", 5), ("Cool Safflina", 3)],
            [("Ice Keese Wing", 5), ("Ice-Breath Lizalfos Tail", 3), ("Chillshroom", 5)],
            [("Sapphire", 5), ("Ice-Breath Lizalfos Horn", 5), ("Ice-Breath Lizalfos Tail", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Desert Voe Trousers": {
        "upgrades": [
            [("White Chuchu Jelly", 3)],
            [("White Chuchu Jelly", 5), ("Cool Safflina", 3)],
            [("Ice Keese Wing", 5), ("Ice-Breath Lizalfos Tail", 3), ("Chillshroom", 5)],
            [("Sapphire", 5), ("Ice-Breath Lizalfos Horn", 5), ("Ice-Breath Lizalfos Tail", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Rubber Helm": {
        "upgrades": [
            [("Yellow Chuchu Jelly", 3), ("Electric Lizalfos Horn", 1)],
            [("Yellow Chuchu Jelly", 8), ("Voltfruit", 5)],
            [("Electric Lizalfos Tail", 5), ("Electric Safflina", 8), ("Zapshroom", 5)],
            [("Topaz", 5), ("Electric Lizalfos Horn", 5), ("Electric Lizalfos Tail", 8)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Rubber Armor": {
        "upgrades": [
            [("Yellow Chuchu Jelly", 3), ("Electric Lizalfos Horn", 1)],
            [("Yellow Chuchu Jelly", 8), ("Voltfruit", 5)],
            [("Electric Lizalfos Tail", 5), ("Electric Safflina", 8), ("Zapshroom", 5)],
            [("Topaz", 5), ("Electric Lizalfos Horn", 5), ("Electric Lizalfos Tail", 8)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Rubber Tights": {
        "upgrades": [
            [("Yellow Chuchu Jelly", 3), ("Electric Lizalfos Horn", 1)],
            [("Yellow Chuchu Jelly", 8), ("Voltfruit", 5)],
            [("Electric Lizalfos Tail", 5), ("Electric Safflina", 8), ("Zapshroom", 5)],
            [("Topaz", 5), ("Electric Lizalfos Horn", 5), ("Electric Lizalfos Tail", 8)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Stealth Mask": {
        "upgrades": [
            [("Blue Nightshade", 3)],
            [("Sunset Firefly", 5), ("Blue Nightshade", 5)],
            [("Sneaky River Snail", 5), ("Sticky Frog", 5), ("Silent Shroom", 8)],
            [("Stealthfin Trout", 10), ("Silent Princess", 5), ("Sundelion", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Stealth Chest Guard": {
        "upgrades": [
            [("Blue Nightshade", 3)],
            [("Sunset Firefly", 5), ("Blue Nightshade", 5)],
            [("Sneaky River Snail", 5), ("Sticky Frog", 5), ("Silent Shroom", 8)],
            [("Stealthfin Trout", 10), ("Silent Princess", 5), ("Sundelion", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Stealth Tights": {
        "upgrades": [
            [("Blue Nightshade", 3)],
            [("Sunset Firefly", 5), ("Blue Nightshade", 5)],
            [("Sneaky River Snail", 5), ("Sticky Frog", 5), ("Silent Shroom", 8)],
            [("Stealthfin Trout", 10), ("Silent Princess", 5), ("Sundelion", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Climber's Bandanna": {
        "upgrades": [
            [("Keese Wing", 3), ("Rushroom", 3)],
            [("Hightail Lizard", 5), ("Electric Keese Wing", 5)],
            [("Hot-Footed Frog", 10), ("Ice Keese Wing", 8)],
            [("Fire Keese Wing", 10), ("Swift Violet", 20)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Climbing Gear": {
        "upgrades": [
            [("Keese Wing", 3), ("Rushroom", 3)],
            [("Hightail Lizard", 5), ("Electric Keese Wing", 5)],
            [("Hot-Footed Frog", 10), ("Ice Keese Wing", 8)],
            [("Fire Keese Wing", 10), ("Swift Violet", 20)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Climbing Boots": {
        "upgrades": [
            [("Keese Wing", 3), ("Rushroom", 3)],
            [("Hightail Lizard", 5), ("Electric Keese Wing", 5)],
            [("Hot-Footed Frog", 10), ("Ice Keese Wing", 8)],
            [("Fire Keese Wing", 10), ("Swift Violet", 20)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Barbarian Helm": {
        "upgrades": [
            [("Mighty Thistle", 3)],
            [("Lynel Mace Horn", 2), ("Lynel Saber Horn", 2), ("Razorshroom", 5)],
            [("Razorclaw Crab", 3), ("Blue-Maned Lynel Mace Horn", 3), ("Blue-Maned Lynel Saber Horn", 3)],
            [("Bladed Rhino Beetle", 3), ("White-Maned Lynel Mace Horn", 3), ("White-Maned Lynel Saber Horn", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Barbarian Armor": {
        "upgrades": [
            [("Mighty Thistle", 3)],
            [("Lynel Mace Horn", 2), ("Lynel Saber Horn", 2), ("Razorshroom", 5)],
            [("Razorclaw Crab", 3), ("Blue-Maned Lynel Mace Horn", 3), ("Blue-Maned Lynel Saber Horn", 3)],
            [("Bladed Rhino Beetle", 3), ("White-Maned Lynel Mace Horn", 3), ("White-Maned Lynel Saber Horn", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Barbarian Leg Wraps": {
        "upgrades": [
            [("Mighty Thistle", 3)],
            [("Lynel Mace Horn", 2), ("Lynel Saber Horn", 2), ("Razorshroom", 5)],
            [("Razorclaw Crab", 3), ("Blue-Maned Lynel Mace Horn", 3), ("Blue-Maned Lynel Saber Horn", 3)],
            [("Bladed Rhino Beetle", 3), ("White-Maned Lynel Mace Horn", 3), ("White-Maned Lynel Saber Horn", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Radiant Mask": {
        "upgrades": [
            [("Luminous Stone", 10), ("Bokoblin Guts", 1)],
            [("Luminous Stone", 15), ("Moblin Guts", 2)],
            [("Luminous Stone", 20), ("Gibdo Bone", 10), ("Horriblin Guts", 3)],
            [("Luminous Stone", 30), ("Lynel Guts", 3), ("Molduga Jaw", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Radiant Shirt": {
        "upgrades": [
            [("Luminous Stone", 10), ("Bokoblin Guts", 1)],
            [("Luminous Stone", 15), ("Moblin Guts", 2)],
            [("Luminous Stone", 20), ("Gibdo Bone", 10), ("Horriblin Guts", 3)],
            [("Luminous Stone", 30), ("Lynel Guts", 3), ("Molduga Jaw", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Radiant Tights": {
        "upgrades": [
            [("Luminous Stone", 10), ("Bokoblin Guts", 1)],
            [("Luminous Stone", 15), ("Moblin Guts", 2)],
            [("Luminous Stone", 20), ("Gibdo Bone", 10), ("Horriblin Guts", 3)],
            [("Luminous Stone", 30), ("Lynel Guts", 3), ("Molduga Jaw", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Royal Guard Cap": {
        "upgrades": [
            [("Bokoblin Guts", 3), ("Boss Bokoblin Horn", 3)],
            [("Blue Boss Bokoblin Horn", 3), ("Boss Bokoblin Guts", 3)],
            [("Black Boss Bokoblin Horn", 3), ("Hinox Guts", 3)],
            [("Silver Boss Bokoblin Horn", 3), ("Gleeok Guts", 3), ("Molduga Guts", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Royal Guard Uniform": {
        "upgrades": [
            [("Bokoblin Guts", 3), ("Boss Bokoblin Horn", 3)],
            [("Blue Boss Bokoblin Horn", 3), ("Boss Bokoblin Guts", 3)],
            [("Black Boss Bokoblin Horn", 3), ("Hinox Guts", 3)],
            [("Silver Boss Bokoblin Horn", 3), ("Gleeok Guts", 3), ("Molduga Guts", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Royal Guard Boots": {
        "upgrades": [
            [("Bokoblin Guts", 3), ("Boss Bokoblin Horn", 3)],
            [("Blue Boss Bokoblin Horn", 3), ("Boss Bokoblin Guts", 3)],
            [("Black Boss Bokoblin Horn", 3), ("Hinox Guts", 3)],
            [("Silver Boss Bokoblin Horn", 3), ("Gleeok Guts", 3), ("Molduga Guts", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Froggy Hood": {
        "upgrades": [
            [("Sticky Lizard", 3)],
            [("Sticky Lizard", 5), ("Horriblin Horn", 5)],
            [("Sticky Frog", 5), ("Blue Horriblin Horn", 5)],
            [("Opal", 10), ("Black Horriblin Horn", 5), ("Horriblin Guts", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Froggy Sleeve": {
        "upgrades": [
            [("Sticky Lizard", 3)],
            [("Sticky Lizard", 5), ("Horriblin Horn", 5)],
            [("Sticky Frog", 5), ("Blue Horriblin Horn", 5)],
            [("Opal", 10), ("Black Horriblin Horn", 5), ("Horriblin Guts", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Froggy Leggings": {
        "upgrades": [
            [("Sticky Lizard", 3)],
            [("Sticky Lizard", 5), ("Horriblin Horn", 5)],
            [("Sticky Frog", 5), ("Blue Horriblin Horn", 5)],
            [("Opal", 10), ("Black Horriblin Horn", 5), ("Horriblin Guts", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Glide Mask": {
        "upgrades": [
            [("Keese Wing", 3)],
            [("Aerocuda Eyeball", 6), ("Keese Wing", 5)],
            [("Aerocuda Eyeball", 8), ("Aerocuda Wing", 6)],
            [("Aerocuda Wing", 10), ("Gibdo Wing", 8), ("Gleeok Wing", 12)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Glide Shirt": {
        "upgrades": [
            [("Keese Wing", 3)],
            [("Aerocuda Eyeball", 6), ("Keese Wing", 5)],
            [("Aerocuda Eyeball", 8), ("Aerocuda Wing", 6)],
            [("Aerocuda Wing", 10), ("Gibdo Wing", 8), ("Gleeok Wing", 12)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Glide Tights": {
        "upgrades": [
            [("Keese Wing", 3)],
            [("Aerocuda Eyeball", 6), ("Keese Wing", 5)],
            [("Aerocuda Eyeball", 8), ("Aerocuda Wing", 6)],
            [("Aerocuda Wing", 10), ("Gibdo Wing", 8), ("Gleeok Wing", 12)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Hood of the Depths": {
        "upgrades": [
            [("Deep Firefly", 3)],
            [("Dark Clump", 5), ("Blue-White Frox Fang", 3)],
            [("Zonaite", 20), ("Frox Fingernail", 3), ("Obsidian Frox Fang", 3)],
            [("Blue-White Frox Fang", 5), ("Frox Guts", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Depths": {
        "upgrades": [
            [("Deep Firefly", 3)],
            [("Dark Clump", 5), ("Blue-White Frox Fang", 3)],
            [("Zonaite", 20), ("Frox Fingernail", 3), ("Obsidian Frox Fang", 3)],
            [("Blue-White Frox Fang", 5), ("Frox Guts", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Gaiters of the Depths": {
        "upgrades": [
            [("Deep Firefly", 3)],
            [("Dark Clump", 5), ("Blue-White Frox Fang", 3)],
            [("Zonaite", 20), ("Frox Fingernail", 3), ("Obsidian Frox Fang", 3)],
            [("Blue-White Frox Fang", 5), ("Frox Guts", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Miner's Mask": {
        "upgrades": [
            [("Brightbloom Seed", 10)],
            [("Brightcap", 5), ("Brightbloom Seed", 20)],
            [("Glowing Cave Fish", 5), ("Deep Firefly", 10), ("Giant Brightbloom Seed", 15)],
            [("Diamond", 3), ("Large Zonaite", 10), ("Giant Brightbloom Seed", 20)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Miner's Top": {
        "upgrades": [
            [("Brightbloom Seed", 10)],
            [("Brightcap", 5), ("Brightbloom Seed", 20)],
            [("Glowing Cave Fish", 5), ("Deep Firefly", 10), ("Giant Brightbloom Seed", 15)],
            [("Diamond", 3), ("Large Zonaite", 10), ("Giant Brightbloom Seed", 20)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Miner's Trousers": {
        "upgrades": [
            [("Brightbloom Seed", 10)],
            [("Brightcap", 5), ("Brightbloom Seed", 20)],
            [("Glowing Cave Fish", 5), ("Deep Firefly", 10), ("Giant Brightbloom Seed", 15)],
            [("Diamond", 3), ("Large Zonaite", 10), ("Giant Brightbloom Seed", 20)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Mystic Headpiece": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Mystic Robe": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Mystic Trousers": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Ember Headdress": {
        "upgrades": [
            [("Fire Fruit", 3)],
            [("Summerwing Butterfly", 5), ("Fire-Breath Lizalfos Horn", 5)],
            [("Warm Darner", 5), ("Large Zonai Charge", 5), ("Fire Like Stone", 5)],
            [("Sizzlefin Trout", 10), ("Large Zonai Charge", 10), ("Gleeok Flame Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Ember Shirt": {
        "upgrades": [
            [("Fire Fruit", 3)],
            [("Summerwing Butterfly", 5), ("Fire-Breath Lizalfos Horn", 5)],
            [("Warm Darner", 5), ("Large Zonai Charge", 5), ("Fire Like Stone", 5)],
            [("Sizzlefin Trout", 10), ("Large Zonai Charge", 10), ("Gleeok Flame Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Ember Trousers": {
        "upgrades": [
            [("Fire Fruit", 3)],
            [("Summerwing Butterfly", 5), ("Fire-Breath Lizalfos Horn", 5)],
            [("Warm Darner", 5), ("Large Zonai Charge", 5), ("Fire Like Stone", 5)],
            [("Sizzlefin Trout", 10), ("Large Zonai Charge", 10), ("Gleeok Flame Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Charged Headdress": {
        "upgrades": [
            [("Shock Fruit", 3)],
            [("Thunderwing Butterfly", 3), ("Electric Lizalfos Horn", 5)],
            [("Electric Darner", 5), ("Large Zonai Charge", 3), ("Shock Like Stone", 5)],
            [("Voltfin Trout", 10), ("Large Zonai Charge", 5), ("Gleeok Thunder Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Charged Shirt": {
        "upgrades": [
            [("Shock Fruit", 3)],
            [("Thunderwing Butterfly", 3), ("Electric Lizalfos Horn", 5)],
            [("Electric Darner", 5), ("Large Zonai Charge", 3), ("Shock Like Stone", 5)],
            [("Voltfin Trout", 10), ("Large Zonai Charge", 5), ("Gleeok Thunder Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Charged Trousers": {
        "upgrades": [
            [("Shock Fruit", 3)],
            [("Thunderwing Butterfly", 3), ("Electric Lizalfos Horn", 5)],
            [("Electric Darner", 5), ("Large Zonai Charge", 3), ("Shock Like Stone", 5)],
            [("Voltfin Trout", 10), ("Large Zonai Charge", 5), ("Gleeok Thunder Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Frostbite Headdress": {
        "upgrades": [
            [("Ice Fruit", 3)],
            [("Winterwing Butterfly", 5), ("Ice-Breath Lizalfos Horn", 5)],
            [("Cold Darner", 5), ("Large Zonai Charge", 5), ("Ice Like Stone", 5)],
            [("Chillfin Trout", 10), ("Large Zonai Charge", 10), ("Gleeok Frost Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Frostbite Shirt": {
        "upgrades": [
            [("Ice Fruit", 3)],
            [("Winterwing Butterfly", 5), ("Ice-Breath Lizalfos Horn", 5)],
            [("Cold Darner", 5), ("Large Zonai Charge", 5), ("Ice Like Stone", 5)],
            [("Chillfin Trout", 10), ("Large Zonai Charge", 10), ("Gleeok Frost Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Frostbite Trousers": {
        "upgrades": [
            [("Ice Fruit", 3)],
            [("Winterwing Butterfly", 5), ("Ice-Breath Lizalfos Horn", 5)],
            [("Cold Darner", 5), ("Large Zonai Charge", 5), ("Ice Like Stone", 5)],
            [("Chillfin Trout", 10), ("Large Zonai Charge", 10), ("Gleeok Frost Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Yiga Mask": {
        "upgrades": [
            [("Octorok Eyeball", 2)],
            [("Fire-Breath Lizalfos Tail", 3), ("Puffshroom", 3)],
            [("Keese Eyeball", 5), ("Ice-Breath Lizalfos Tail", 5)],
            [("Black Hinox Horn", 3), ("Electric Lizalfos Tail", 5), ("Mighty Bananas", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Yiga Armor": {
        "upgrades": [
            [("Octorok Eyeball", 2)],
            [("Fire-Breath Lizalfos Tail", 3), ("Puffshroom", 3)],
            [("Keese Eyeball", 5), ("Ice-Breath Lizalfos Tail", 5)],
            [("Black Hinox Horn", 3), ("Electric Lizalfos Tail", 5), ("Mighty Bananas", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Yiga Tights": {
        "upgrades": [
            [("Octorok Eyeball", 2)],
            [("Fire-Breath Lizalfos Tail", 3), ("Puffshroom", 3)],
            [("Keese Eyeball", 5), ("Ice-Breath Lizalfos Tail", 5)],
            [("Black Hinox Horn", 3), ("Electric Lizalfos Tail", 5), ("Mighty Bananas", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Rudania Divine Helm": {
        "upgrades": [
            [("Ruby", 1), ("Zonaite", 5)],
            [("Ruby", 4), ("Zonaite", 10)],
            [("Ruby", 6), ("Large Zonaite", 5), ("Dazzlefruit", 5)],
            [("Ruby", 10), ("Large Zonaite", 10), ("Dazzlefruit", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Medoh Divine Helm": {
        "upgrades": [
            [("Sapphire", 1), ("Zonaite", 5)],
            [("Sapphire", 4), ("Zonaite", 10)],
            [("Sapphire", 6), ("Large Zonaite", 5), ("Dazzlefruit", 5)],
            [("Sapphire", 10), ("Large Zonaite", 10), ("Dazzlefruit", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Naboris Divine Helm": {
        "upgrades": [
            [("Topaz", 1), ("Zonaite", 5)],
            [("Topaz", 4), ("Zonaite", 10)],
            [("Topaz", 6), ("Large Zonaite", 5), ("Dazzlefruit", 5)],
            [("Topaz", 10), ("Large Zonaite", 10), ("Dazzlefruit", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Vah Ruta Divine Helm": {
        "upgrades": [
            [("Opal", 5), ("Zonaite", 5)],
            [("Opal", 10), ("Zonaite", 10)],
            [("Opal", 15), ("Large Zonaite", 5), ("Dazzlefruit", 5)],
            [("Opal", 25), ("Large Zonaite", 10), ("Dazzlefruit", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zonaite Helm": {
        "upgrades": [
            [("Soldier Construct Horn", 5)],
            [("Zonaite", 5), ("Captain Construct I Horn", 5), ("Soldier Construct II Horn", 5)],
            [("Large Zonaite", 5), ("Captain Construct II Horn", 5), ("Soldier Construct III Horn", 5)],
            [("Large Zonaite", 10), ("Captain Construct III Horn", 5), ("Soldier Construct IV Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zonaite Waistguard": {
        "upgrades": [
            [("Soldier Construct Horn", 5)],
            [("Zonaite", 5), ("Captain Construct I Horn", 5), ("Soldier Construct II Horn", 5)],
            [("Large Zonaite", 5), ("Captain Construct II Horn", 5), ("Soldier Construct III Horn", 5)],
            [("Large Zonaite", 10), ("Captain Construct III Horn", 5), ("Soldier Construct IV Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Zonaite Shin Guards": {
        "upgrades": [
            [("Soldier Construct Horn", 5)],
            [("Zonaite", 5), ("Captain Construct I Horn", 5), ("Soldier Construct II Horn", 5)],
            [("Large Zonaite", 5), ("Captain Construct II Horn", 5), ("Soldier Construct III Horn", 5)],
            [("Large Zonaite", 10), ("Captain Construct III Horn", 5), ("Soldier Construct IV Horn", 5)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Amber Earrings": {
        "upgrades": [
            [("Amber", 10), ("Flint", 5)],
            [("Amber", 25), ("Flint", 10)],
            [("Amber", 35), ("Flint", 15)],
            [("Amber", 60), ("Flint", 25)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Diamond Circlet": {
        "upgrades": [
            [("Diamond", 2), ("Flint", 3)],
            [("Diamond", 3), ("Flint", 5)],
            [("Diamond", 5), ("Star Fragment", 1)],
            [("Diamond", 8), ("Star Fragment", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Ruby Circlet": {
        "upgrades": [
            [("Flint", 3), ("Ruby", 2)],
            [("Flint", 5), ("Ruby", 4)],
            [("Ruby", 6), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Sapphire Circlet": {
        "upgrades": [
            [("Flint", 3), ("Sapphire", 2)],
            [("Flint", 5), ("Sapphire", 4)],
            [("Sapphire", 6), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Topaz Earrings": {
        "upgrades": [
            [("Flint", 3), ("Topaz", 2)],
            [("Flint", 5), ("Topaz", 4)],
            [("Topaz", 6)],
            [("Topaz", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Opal Earrings": {
        "upgrades": [
            [("Flint", 5), ("Opal", 6)],
            [("Flint", 10), ("Opal", 12)],
            [("Flint", 15), ("Opal", 18)],
            [("Flint", 25), ("Opal", 30)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Well-Worn Hair Band": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Cece Hat": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Lightning Helm": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Sand Boots": {
        "upgrades": [
            [("Hightail Lizard", 3)],
            [("Gibdo Bone", 20), ("Swift Carrot", 5)],
            [("Gibdo Guts", 5), ("Molduga Fin", 5), ("Rushroom", 10)],
            [("Hearty Lizard", 5), ("Molduga Guts", 5), ("Swift Violet", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Snow Boots": {
        "upgrades": [
            [("Hightail Lizard", 3)],
            [("Octorok Tentacle", 5), ("Swift Carrot", 5)],
            [("Octo Balloon", 5), ("Rushroom", 20)],
            [("Naydra's Scale", 2), ("Swift Violet", 20)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Bokoblin Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Horriblin Mask": {
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
    "Moblin Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of Memories": {
        "upgrades": [
            [("Light Dragon's Scale", 1), ("Silent Princess", 3)],
            [("Farosh's Horn", 2), ("Light Dragon's Talon", 1), ("Silent Princess", 3)],
            [("Shard of Light Dragon's Fang", 1), ("Naydra's Horn", 2), ("Silent Princess", 5)],
            [("Dinraal's Horn", 2), ("Light Dragon's Horn", 1), ("Silent Princess", 10)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Champion's Leathers": {
        "upgrades": [
            [("Light Dragon's Scale", 2), ("Silent Princess", 3)],
            [("Light Dragon's Talon", 2), ("Silent Princess", 3), ("Sundelion", 10)],
            [("Shard of Light Dragon's Fang", 2), ("Silent Princess", 5), ("Sundelion", 15)],
            [("Light Dragon's Horn", 2), ("Silent Princess", 10), ("Sundelion", 20)],
        ],
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
    "Midna's Helmet": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Majora's Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Korok Mask": {
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
    "Evil Spirit Mask": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Evil Spirit Armor": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Evil Spirit Greaves": {
        "upgrades": [],
        "index": _idx_generator.get_next_index(),
    },
    "Sheik's Mask": {
        "upgrades": [
            [("Star Fragment", 1), ("Silent Princess", 1)],
            [("Star Fragment", 2), ("Silent Princess", 2)],
            [("Star Fragment", 3), ("Silent Princess", 4)],
            [("Star Fragment", 4), ("Silent Princess", 8)],
        ],
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
    "Fierce Deity Mask": {
        "upgrades": [
            [("Dinraal's Scale", 1), ("Hinox Toenail", 5)],
            [("Dinraal's Claw", 1), ("Hinox Tooth", 5)],
            [("Shard of Dinraal's Fang", 1), ("Hinox Guts", 2)],
            [("Dinraal's Horn", 1), ("Lynel Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Fierce Deity Armor": {
        "upgrades": [
            [("Naydra's Scale", 1), ("Hinox Toenail", 5)],
            [("Naydra's Claw", 1), ("Hinox Tooth", 5)],
            [("Shard of Naydra's Fang", 1), ("Hinox Guts", 2)],
            [("Naydra's Horn", 1), ("Lynel Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Fierce Deity Boots": {
        "upgrades": [
            [("Farosh's Scale", 1), ("Hinox Toenail", 5)],
            [("Farosh's Claw", 1), ("Hinox Tooth", 5)],
            [("Shard of Farosh's Fang", 1), ("Hinox Guts", 2)],
            [("Farosh's Horn", 1), ("Lynel Guts", 2)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Mask of Awakening": {
        "upgrades": [
            [("Luminous Stone", 10), ("Star Fragment", 1)],
            [("Luminous Stone", 15), ("Star Fragment", 1)],
            [("Luminous Stone", 20), ("Star Fragment", 1)],
            [("Luminous Stone", 30), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of Awakening": {
        "upgrades": [
            [("Luminous Stone", 10), ("Star Fragment", 1)],
            [("Luminous Stone", 15), ("Star Fragment", 1)],
            [("Luminous Stone", 20), ("Star Fragment", 1)],
            [("Luminous Stone", 30), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of Awakening": {
        "upgrades": [
            [("Luminous Stone", 10), ("Star Fragment", 1)],
            [("Luminous Stone", 15), ("Star Fragment", 1)],
            [("Luminous Stone", 20), ("Star Fragment", 1)],
            [("Luminous Stone", 30), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Wild": {
        "upgrades": [
            [("Farosh's Scale", 2), ("Acorn", 10)],
            [("Farosh's Claw", 2), ("Courser Bee Honey", 5)],
            [("Energetic Rhino Beetle", 3), ("Shard of Farosh's Fang", 2), ("Shard of Farosh's Spike", 5)],
            [("Farosh's Horn", 2), ("Shard of Farosh's Spike", 10), ("Star Fragment", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Wild": {
        "upgrades": [
            [("Naydra's Scale", 2), ("Acorn", 10)],
            [("Naydra's Claw", 2), ("Courser Bee Honey", 5)],
            [("Energetic Rhino Beetle", 3), ("Shard of Naydra's Fang", 2), ("Shard of Naydra's Spike", 5)],
            [("Naydra's Horn", 2), ("Shard of Naydra's Spike", 10), ("Star Fragment", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Wild": {
        "upgrades": [
            [("Dinraal's Scale", 2), ("Acorn", 10)],
            [("Dinraal's Claw", 2), ("Courser Bee Honey", 5)],
            [("Energetic Rhino Beetle", 3), ("Shard of Dinraal's Fang", 2), ("Shard of Dinraal's Spike", 5)],
            [("Dinraal's Horn", 2), ("Shard of Dinraal's Spike", 10), ("Star Fragment", 3)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Hero": {
        "upgrades": [
            [("Ruby", 1), ("Star Fragment", 1)],
            [("Ruby", 4), ("Star Fragment", 1)],
            [("Ruby", 6), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Hero": {
        "upgrades": [
            [("Ruby", 1), ("Star Fragment", 1)],
            [("Ruby", 4), ("Star Fragment", 1)],
            [("Ruby", 6), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Hero": {
        "upgrades": [
            [("Ruby", 1), ("Star Fragment", 1)],
            [("Ruby", 4), ("Star Fragment", 1)],
            [("Ruby", 6), ("Star Fragment", 1)],
            [("Ruby", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of Time": {
        "upgrades": [
            [("Amber", 10), ("Star Fragment", 1)],
            [("Amber", 20), ("Star Fragment", 1)],
            [("Amber", 30), ("Star Fragment", 1)],
            [("Amber", 40), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of Time": {
        "upgrades": [
            [("Amber", 10), ("Star Fragment", 1)],
            [("Amber", 20), ("Star Fragment", 1)],
            [("Amber", 30), ("Star Fragment", 1)],
            [("Amber", 40), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of Time": {
        "upgrades": [
            [("Amber", 10), ("Star Fragment", 1)],
            [("Amber", 20), ("Star Fragment", 1)],
            [("Amber", 30), ("Star Fragment", 1)],
            [("Amber", 40), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Wind": {
        "upgrades": [
            [("Opal", 5), ("Star Fragment", 1)],
            [("Opal", 10), ("Star Fragment", 1)],
            [("Opal", 15), ("Star Fragment", 1)],
            [("Opal", 25), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Wind": {
        "upgrades": [
            [("Opal", 5), ("Star Fragment", 1)],
            [("Opal", 10), ("Star Fragment", 1)],
            [("Opal", 15), ("Star Fragment", 1)],
            [("Opal", 25), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Wind": {
        "upgrades": [
            [("Opal", 5), ("Star Fragment", 1)],
            [("Opal", 10), ("Star Fragment", 1)],
            [("Opal", 15), ("Star Fragment", 1)],
            [("Opal", 25), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of Twilight": {
        "upgrades": [
            [("Topaz", 1), ("Star Fragment", 1)],
            [("Topaz", 4), ("Star Fragment", 1)],
            [("Topaz", 6), ("Star Fragment", 1)],
            [("Topaz", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of Twilight": {
        "upgrades": [
            [("Topaz", 1), ("Star Fragment", 1)],
            [("Topaz", 4), ("Star Fragment", 1)],
            [("Topaz", 6), ("Star Fragment", 1)],
            [("Topaz", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of Twilight": {
        "upgrades": [
            [("Topaz", 1), ("Star Fragment", 1)],
            [("Topaz", 4), ("Star Fragment", 1)],
            [("Topaz", 6), ("Star Fragment", 1)],
            [("Topaz", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Cap of the Sky": {
        "upgrades": [
            [("Sapphire", 1), ("Star Fragment", 1)],
            [("Sapphire", 4), ("Star Fragment", 1)],
            [("Sapphire", 6), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Tunic of the Sky": {
        "upgrades": [
            [("Sapphire", 1), ("Star Fragment", 1)],
            [("Sapphire", 4), ("Star Fragment", 1)],
            [("Sapphire", 6), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Trousers of the Sky": {
        "upgrades": [
            [("Sapphire", 1), ("Star Fragment", 1)],
            [("Sapphire", 4), ("Star Fragment", 1)],
            [("Sapphire", 6), ("Star Fragment", 1)],
            [("Sapphire", 10), ("Star Fragment", 1)],
        ],
        "index": _idx_generator.get_next_index(),
    },
    "Ancient Hero's Aspect": {
        "upgrades": [
            [("Zonaite", 15), ("Silver Bokoblin Horn", 9), ("Hinox Guts", 9)],
            [("Large Zonaite", 10), ("Frox Guts", 9), ("Silver Moblin Horn", 9)],
            [("Large Zonaite", 15), ("Silver Lizalfos Horn", 9), ("Molduga Guts", 9)],
            [("Gleeok Guts", 9), ("Silver Lynel Mace Horn", 9), ("Silver Lynel Saber Horn", 9)],
        ],
        "index": _idx_generator.get_next_index(),
    },
}
# fmt: on
