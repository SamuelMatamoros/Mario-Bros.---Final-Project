import config
import pyxel


class Character:

    def __init__(self, character: str):

        # Attributes
        self.character = character.upper()
        self.level = 0
        self.has_package = False

        # Methods
        self.draw()

    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int):
            raise ValueError("Level must be an integer")
        elif level < 0:
            raise ValueError("Level must be greater or equal to 0")
        self.__level = level

    # has_package property
    @property
    def has_package(self) -> bool:
        return self.__has_package

    @has_package.setter
    def has_package(self, has_package: bool):
        if not isinstance(has_package, bool):
            raise TypeError("has_package must be a boolean")
        self.__has_package = has_package

    @property
    def character(self) -> str:
        return self.__character

    @character.setter
    def character(self, character: str):
        if not isinstance(character, str):
            raise TypeError("character must be a string")
        elif character not in config.CHARACTERS:
            raise ValueError("character must be one of:",
                             str(config.CHARACTERS))
        else:
            self.__character = character

    def update(self, max_level):
        """ Update method for character class """

        if self.character == "MARIO":
            up_key = pyxel.KEY_UP
            down_key = pyxel.KEY_DOWN
        if self.character == "LUIGI":
            up_key = pyxel.KEY_W
            down_key = pyxel.KEY_S

        if pyxel.btnp(up_key) and max_level//2 - 1 > self.level:
            self.level += 1
        if pyxel.btnp(down_key) and 0 < self.level:
            self.level -= 1

    def draw(self):
        """ Draw method """
        if self.character == "MARIO":
            x = 12 * config.TILE_DIMENSION - config.TILE_DIMENSION//2
            y = 10 * config.TILE_DIMENSION + config.TILE_DIMENSION//2 + 2
            if self.level == 0:
                sprite = config.MARIO_DEF_RIGHT
            else:
                sprite = config.MARIO_DEF_LEFT
        elif self.character == "LUIGI":
            x = 4 * config.TILE_DIMENSION - config.TILE_DIMENSION//4
            y = 9 * config.TILE_DIMENSION + config.TILE_DIMENSION//2 + 2
            sprite = config.LUIGI_DEF_RIGHT
        else:
            sprite = config.BOSS_ARMS_DOWN

        pyxel.blt(x, y - 2*self.level*config.TILE_DIMENSION,
                  *sprite, scale=1.3)
