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

    def __init__(self, side: str, level: int, sprite: tuple):
        """
        This method is used to create Character objects.

        :param name: str. Name of the character.
        :param side: str. Either "left" or "right".
        :param level: int. Platform number (1, 2, 3, 4).
        :param sprite: str. Reference to the sprite for the character.
        """
        self.side = side
        self.level = level
        self.has_package = False
        self.sprite = sprite

    # side property
    @property
    def side(self) -> str:
        return self.__side

    @side.setter
    def side(self, side: str):
        if side not in ("left", "right"):
            raise ValueError('Side must be "left" or "right"')
        self.__side = side

    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int) or level < 1:
            raise ValueError("Level must be an int greater than 0")
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
    def sprite(self) -> tuple:
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite: tuple):
        if not isinstance(sprite, tuple):
            raise TypeError("sprite must be a string")
        elif len(sprite) != 6:
            raise ValueError("sprite lenght must be 6")
        else:
            self.__sprite = sprite

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
