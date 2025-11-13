import config
import pyxel


class Character:
    """
    Class to represent a game character (Mario or Luigi).

    Attributes:
        side : str
            The side of the conveyor the character is on ("left" or "right").
        level : int
            The current level/platform (e.g., 1, 2, 3).
        has_package : bool
            Whether the character is holding a package.
        sprite : str
            The path or identifier for the character's sprite image.
    """

    def __init__(self, character: str):
        """
        This method is used to create Character objects.

        :param character: str. Name of the character.
        """

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

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the character.
        """
        return (f"side {self.side}\nlevel {self.level}"
                f"has package? {self.has_package}"
                f"sprite: {self.sprite}")

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the character.
        """
        return self.__str__()
