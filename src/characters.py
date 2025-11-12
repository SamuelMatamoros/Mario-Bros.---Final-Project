class Character:
    """
    Class to represent a game character (Mario or Luigi).

    Attributes:
        name : str
            The character's name ("Mario" or "Luigi").
        side : str
            The side of the conveyor the character is on ("left" or "right").
        level : int
            The current level/platform (e.g., 1, 2, 3).
        has_package : bool
            Whether the character is holding a package.
        sprite : str
            The path or identifier for the character's sprite image.
    """

    def __init__(self, name: str, side: str, level: int):
        """
        This method is used to create Character objects.

        :param name: str. Name of the character.
        :param side: str. Either "left" or "right".
        :param level: int. Platform number (1, 2, 3, 4).
        :param sprite: str. Reference to the sprite for the character.
        """
        self.name = name
        self.side = side
        self.level = level
        self.has_package = False
        if self.name == "Mario":
            self.sprite = "mario_image.png"
        elif self.name == "Luigi":
            self.sprite = "luigi_image.png"
        # Format of the sprite to be changed


    # name property
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.__name = name

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

    # !!!!!!sprite property (i believe this is wrong and unnecesary it might be erased)!!!!!!
    # I dont really know yet the image representation system so this is probably wrong
    @property
    def sprite(self) -> str:
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite: str):
        if not isinstance(sprite, str):
            raise TypeError("sprite must be a string")
        self.__sprite = sprite

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the character.
        """
        return (f"{self.name} is on the {self.side} side at level {self.level}, "
                f"{'holding a package' if self.has_package else 'not holding a package'}, "
                f"sprite: {self.sprite}")

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the character.
        """
        return self.__str__()
