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

    def draw(self):
        """ Draw method """
        pyxel.blt(12 * config.TILE_DIMENSION,
                  10 * config.TILE_DIMENSION,
                  *config.MARIO_DEF_LEFT)
