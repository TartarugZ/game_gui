from game.static_var import *

# Window size
WINDOW_HEIGHT = 640
WINDOW_WIDTH = 1280

# States
STATE_TOWN = 1
STATE_BUILD = 2

# Settings
FPS = 60
TILESIZE = 32

# Layers
HOUSE_LAYER = 3
PLACE_LAYER = 2
TERRA_LAYER = 1

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR_STONE = (200, 200, 200)
COLOR_GOLD = (255, 215, 0)
WATER = (0, 255, 255)
GROUND = (11, 200, 81)
BEACH = (244, 164, 96)

# Resources
RESOURCES = {
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
    ARMY: {
        COUNT: 100,
        MAX: 200
    },
    FLEET: {
        COUNT: 0,
        MAX: 200
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
        }
    },

    GOLD_MINE: {
        COST: {
            GOLD_ORE: 100,
        },
        PLACE: 'G',
        TYPE: DYNAMIC,
        NAME: GOLD_MINE,
        RESOURCES_CREATE: {
            GOLD_ORE: 20,
        },
        RESOURCES_USE: {
            STONE: 47
        },
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        MAX_WORKERS: 3
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
        }
    },

    BARRACKS: {
        COST: {
            STONE: 100,
        },
        PLACE: '.',
        TYPE: WAREHOUSE,
        NAME: BARRACKS,
        RESOURCES_CREATE: {
            ARMY: 200
        }
    },

    SHIPYARD: {
        COST: {
            STONE: 100,
        },
        PLACE: 'R',
        TYPE: WAREHOUSE,
        NAME: SHIPYARD,
        RESOURCES_CREATE: {
            FLEET: 200
        }
    },

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
    '0..............wwwwww0',
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
