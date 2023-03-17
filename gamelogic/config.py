from gamelogic.static_var import *
from gamelogic.settings import *

# Resources
START_RESOURCES = {
    PEOPLE: {
        COUNT: 2,
        MAX: 2
    },
    GOLD_ORE: {
        COUNT: 100,
        MAX: 100
    },
    STONE: {
        COUNT: 10000,
        MAX: 100
    },
    IRON_ORE: {
        COUNT: 100,
        MAX: 100
    },
    PLANK: {
        COUNT: 100,
        MAX: 100
    },
    SKIN: {
        COUNT: 100,
        MAX: 100
    },
    GOLD: {
        COUNT: 100,
        MAX: 100
    },
    IRON: {
        COUNT: 100,
        MAX: 100
    },
    WEAPON: {
        COUNT: 100,
        MAX: 100
    },
    ARMOR: {
        COUNT: 100,
        MAX: 100
    },
    WHEAT: {
        COUNT: 100,
        MAX: 100
    },
    FLOUR: {
        COUNT: 100,
        MAX: 100
    },
    BREAD: {
        COUNT: 100,
        MAX: 100
    },
    CLOTHES: {
        COUNT: 100,
        MAX: 100
    },
    FISH: {
        COUNT: 100,
        MAX: 100
    },

}

START_ARMY = {
    SWORDSMAN: {
        NAME: SWORDSMAN,
        TYPE: MILITARY,
        COUNT: 0,
        MAX: 10,
        ORDER: 0,
        COST: {
            GOLD: 0
        }
    },
    ARCHER: {
        NAME: ARCHER,
        TYPE: MILITARY,
        COUNT: 0,
        MAX: 10,
        ORDER: 0,
        COST: {
            GOLD: 0
        }
    },
    PRIEST: {
        NAME: PRIEST,
        TYPE: MILITARY,
        COUNT: 0,
        MAX: 10,
        ORDER: 0,
        COST: {
            GOLD: 0
        }
    },

    SCHROONER: {
        NAME: SCHROONER,
        TYPE: FLEET,
        COUNT: 0,
        MAX: 10,
        ORDER: 0,
        COST: {
            GOLD: 0
        }
    },
    DRAKKAR: {
            NAME: DRAKKAR,
            TYPE: FLEET,
            COUNT: 0,
            MAX: 10,
            ORDER: 0,
            COST: {
                GOLD: 0
            }
        },
    CARAVELLE: {
            NAME: CARAVELLE,
            TYPE: FLEET,
            COUNT: 0,
            MAX: 10,
            ORDER: 0,
            COST: {
                GOLD: 0
            }
        }
}

# Dictionary with buildings settings
BUILDINGS = {
    HOUSE: {
        COST: {
            STONE: 0,
        },
        PLACE: '.',
        TYPE: STATIC,
        NAME: HOUSE,
        RESOURCES_CREATE: {
            PEOPLE: 2,
        },
        IMAGE: (0, 0)
    },

    GOLD_MINE: {
        COST: {
            GOLD_ORE: 100,
        },
        PLACE: 'G',
        TYPE: DYNAMIC,
        NAME: GOLD_MINE,
        RESOURCES_CREATE: {
            GOLD_ORE: 2,
        },
        RESOURCES_USE: {
            STONE: 47
        },
        MAX_WORKERS: 3,
        IMAGE: (64, 0)
    },

    STONE_MINE: {
        COST: {
            STONE: 100,
        },
        PLACE: 'S',
        TYPE: DYNAMIC,
        NAME: STONE_MINE,
        RESOURCES_CREATE: {
            STONE: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (192, 0)
    },

    IRON_MINE: {
        COST: {
            STONE: 100,
        },
        PLACE: 'I',
        TYPE: DYNAMIC,
        NAME: IRON_MINE,
        RESOURCES_CREATE: {
            IRON_ORE: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (96, 0)
    },

    SAWMILL: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: SAWMILL,
        RESOURCES_CREATE: {
            PLANK: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (160, 0)
    },

    HUNTER: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: HUNTER,
        RESOURCES_CREATE: {
            SKIN: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (224, 0)
    },

    GOLD_MELT: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: GOLD_MELT,
        RESOURCES_CREATE: {
            GOLD: 2,
        },
        RESOURCES_USE: {
            GOLD_ORE: 2
        },
        MAX_WORKERS: 3,
        IMAGE: (288, 0)
    },

    IRON_MELT: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: IRON_MELT,
        RESOURCES_CREATE: {
            IRON: 2,
        },
        RESOURCES_USE: {
            IRON_ORE: 2
        },
        MAX_WORKERS: 3,
        IMAGE: (320, 0)
    },

    GUNSMITH: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: HOUSE,
        RESOURCES_CREATE: {
            WEAPON: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (128, 0)
    },

    BLACKSMITH: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: BLACKSMITH,
        RESOURCES_CREATE: {
            ARMOR: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (32, 0)
    },

    WHEAT_FIELD: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: WHEAT_FIELD,
        RESOURCES_CREATE: {
            WHEAT: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (416, 0)
    },

    MILL: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: MILL,
        RESOURCES_CREATE: {
            FLOUR: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (448, 0)
    },

    BAKERY: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: BAKERY,
        RESOURCES_CREATE: {
            BREAD: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (480, 0)
    },

    TAILOR: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: DYNAMIC,
        NAME: TAILOR,
        RESOURCES_CREATE: {
            CLOTHES: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (512, 0)
    },

    FISHERMAN: {
        COST: {
            STONE: 100,
        },
        PLACE: 'R',
        TYPE: DYNAMIC,
        NAME: FISHERMAN,
        RESOURCES_CREATE: {
            FISH: 2,
        },
        RESOURCES_USE: None,
        MAX_WORKERS: 3,
        IMAGE: (544, 0)
    },

    STORAGE: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: WAREHOUSE,
        NAME: STORAGE,
        RESOURCES_CREATE: {
            GOLD_ORE: 200,
            STONE: 12,
            IRON_ORE: 21,
            PLANK: 21,
            SKIN: 31,
            GOLD: 12,
            IRON: 144,
            WEAPON: 52,
            ARMOR: 235,
            WHEAT: 41,
            FLOUR: 25,
            BREAD: 25,
            CLOTHES: 14,
            FISH: 14,
        },
        IMAGE: (256, 0)
    },

    BARRACKS: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: WAR,
        NAME: BARRACKS,
        RESOURCES_CREATE: {
            SWORDSMAN: 200
        },
        IMAGE: (352, 0)
    },

    SHIPYARD: {
        COST: {
            STONE: 100,
        },
        PLACE: 'R',
        TYPE: WAR,
        NAME: SHIPYARD,
        RESOURCES_CREATE: {
            SCHROONER: 200,
            DRAKKAR: 400,
            CARAVELLE: 600
        },
        IMAGE: (384, 0)
    },
}

EXPEDITION = {
    1: {
        COST: {
            SWORDSMAN: 0,
            PRIEST: 0,
        },
        RESOURCES_CREATE: {
            STONE: 100,
        },
    },
    2: {
        COST: {
            SWORDSMAN: 0,
            PRIEST: 0,
        },
        RESOURCES_CREATE: {
            STONE: 200,
        },
    },
    3: {
        COST: {
            SWORDSMAN: 0,
            PRIEST: 0,
        },
        RESOURCES_CREATE: {
            STONE: 300,
        },
    }
}

# Town map
town_map = [
    '0000000000000000000000',
    '0IGGGSSIISGG.........0',
    '0.....GIGGSSS...www..0',
    '0.....SISIS....www...0',
    '0.....GGGSS....ww....0',
    '0..............w.....0',
    '0..............w.....0',
    '0..............w.....0',
    '0..............www...0',
    '0..............w.....0',
    '0..............w.....0',
    '0..............w.....0',
    '0..............w.....0',
    '0..............w.....0',
    '0..............w.....0',
    '0000000000000000000000',
]

# Field settings
FIELD = {
    X: -1,
    Y: -1,
    WIDTH: len(town_map[0]) - 2,
    HEIGHT: len(town_map) - 2,
}

SOLDIERS = {
        'swordsman': SWORDSMAN,
        'archer': ARCHER,
        'priest': PRIEST,
        'schrooner': SCHROONER,
        'drakkar': DRAKKAR,
        'caravelle': CARAVELLE
    }