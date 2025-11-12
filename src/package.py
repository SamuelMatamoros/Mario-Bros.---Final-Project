class Package:
    """
    Class to represent a game package.

    Attributes:
        level : int
            The current level/platform the package is on.
        state : str
            The current state of the package: "in_conveyor", "handled", "broken", "at_truck".
        sprite : str
            The path or identifier for the package's sprite image.
    """

    def __init__(self, level: int, state: str):
        """
        This is the method used to create Package objects.

        :param level: int. Platform number (0, 1, 2, 3, 4, 5, 6).
        :param state: str. The state of the package.
        :param sprite: str. Reference to the sprite for the package.
        """
        self.level = level
        self.state = state
        if self.level == 0:
            self.sprite = "package0.png"
        elif self.level == 1:
            self.sprite = "package1.png"
        elif self.level == 2:
            self.sprite = "package2.png"
        elif self.level == 3:
            self.sprite = "package3.png"
        elif self.level == 4:
            self.sprite = "package4.png"
        elif self.level == 5:
            self.sprite = "package5.png"
        elif self.level == 6:
            self.sprite = "package_at_truck.png"
        elif self.state == "broken":
            self.sprite = "package_broken.png"
        # All this "image_x.png to be changed to the correct format"


    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int) or level < 0 or level > 6:
            raise ValueError("Level must be an int greater or equal to 0 and lower than 6")
        self.__level = level

    # state property
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        valid_states = ("in_conveyor", "handled", "broken", "at_truck")
        if state not in valid_states:
            raise ValueError(f"State must be one of {valid_states}")
        self.__state = state



    # !!!!!!sprite property (i believe this is wrong and unnecesary it might be erased)!!!!!!
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
        Return a human-readable string representation of the package.
        """
        return (f"Package at level {self.level}, state: {self.state}, "
                f"sprite: {self.sprite}")

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the package.
        """
        return self.__str__()
