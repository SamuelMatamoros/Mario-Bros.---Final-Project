"""
This script contains all the constants for the game.
"""

# Dimensions

TILE_DIMENSION = 16

TILES_OF_WIDTH = 16
TILES_OF_HEIGHT = 12
WIDTH = TILES_OF_WIDTH * TILE_DIMENSION
HEIGHT = TILES_OF_HEIGHT * TILE_DIMENSION

# Sprites & characters

CHARACTERS = ["MARIO", "LUIGI", "BOSS"]

# NAME = (img_bank, x_start, y_start, with, height, [colkey])
MARIO_DEF_LEFT = (0, 0, 0, 16, 16, 11)
MARIO_DEF_RIGHT = (0, 16, 16, 16, 16, 11)
MARIO_LOOK_LEFT_SMEAR = (0, 32, 0, 16, 16, 11)
MARIO_LOOK_LEFT = (0, 48, 0, 16, 16, 11)
MARIO_PACKAGE = (0, 16, 0, 16, 16, 11)
MARIO_PACKAGE_FLIPPED = (0, 16, 0, -16, 16, 11)
MARIO_REST = (0, 0, 16, 16, 16, 11)
MARIO_REPRIMAND = (0, 32, 16, 16, 16, 11)

LUIGI_DEF_RIGHT = (0, 0, 32, 16, 16, 8)
LUIGI_DEF_LEFT = (0, 16, 48, 16, 16, 8)
LUIGI_PACKAGE_1 = (0, 48, 32, 16, 16, 8)
LUIGI_PACKAGE_2 = (0, 32, 32, 16, 16, 8)
LUIGI_PACKAGE = (0, 16, 32, 16, 16, 8)
LUIGI_REST = (0, 0, 48, 16, 16, 8)
LUIGI_REPRIMAND = (0, 32, 48, 16, 16, 8)

BOSS_ARMS_UP = (0, 0, 64, 16, 16, 0)
BOSS_ARMS_DOWN = (0, 16, 64, 16, 16, 0)

BOSS_ARMS_UP_INVERTED = (0, 0, 64, -16, 16, 0)
BOSS_ARMS_DOWN_INVERTED = (0, 16, 64, -16, 16, 0)

GAME_OVER = (2, 0, 0, 192, 128, 10)
START_SCREEN = (2, 0, 128, 192, 128, 10)


PACKAGE_STATES = ["CONVEYOR", "HANDLED", "BROKEN", "TRUCK"]
PACKAGE_SPRITE = [
        (1, 0, 0, 16, 16, 0),
        (1, 16, 0, 16, 16, 0),
        (1, 32, 0, 16, 16, 0),
        (1, 48, 0, 16, 16, 0),
        (1, 0, 16, 16, 16, 0)
        ]

TRUCK_HEAD = (1, 0, 32, 16, 16, 0)
TRUCK_BED = [
        (1, 16, 32, 16, 16, 0),
        (1, 0, 48, 16, 16, 0),
        (1, 16, 48, 16, 16, 0),
        (1, 32, 48, 16, 16, 0),
        (1, 48, 48, 16, 16, 0),
        (1, 0, 64, 16, 16, 0),
        (1, 16, 64, 16, 16, 0),
        (1, 32, 64, 16, 16, 0),
        (1, 48, 64, 16, 16, 0)
        ]

CONVEYOR_0 = [
        (1, 48, 80, 16, 16, 0),      # Conveyor left 0
        (1, 0, 96, 16, 16, 0),       # Conveyor 0
        (1, 0, 96, 16, 16, 0),       # Conveyor 0
        (1, 0, 96, 16, 16, 0),       # Conveyor 0
        (1, 0, 96, 16, 16, 0),       # Conveyor 0
        (1, 32, 96, 16, 16, 0),      # Conveyor right 0
        ]

CONVEYOR_1 = [
        (1, 32, 80, 16, 16, 0),      # Conveyor left 1
        (1, 16, 96, 16, 16, 0),      # Conveyor 1
        (1, 16, 96, 16, 16, 0),      # Conveyor 1
        (1, 16, 96, 16, 16, 0),      # Conveyor 1
        (1, 16, 96, 16, 16, 0),      # Conveyor 1
        (1, 48, 96, 16, 16, 0),      # Conveyor right 1
        ]

PIPE_X = WIDTH//2 - 8
PIPE_BIG = (1, 32, 32, 16, 16, 0)
HOR_HALF_PIPE = (1, 0, 112, 8, 16, 0)
L_PIPE = (1, 16, 112, 16, 16, 0)
VERT_PIPE = (1, 38, 112, 4, 16, 0)

MACHINE = (1, 64, 16, 32, 32, 0)
DOOR = (1, 0, 80, 16, 16, 0)

STAIR = (1, 48, 112, 16, 16, 0, 0)
