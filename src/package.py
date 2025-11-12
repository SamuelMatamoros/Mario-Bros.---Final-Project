import settings


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
        self.sprite = settings.PACKAGE_1

    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int):
            raise ValueError("Level must be an integer")
        elif level < 0 or level > 6:
            raise ValueError("Level must be between 0 and 6")
        self.__level = level

    # state property
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        valid_states = ("in_conveyor", "handled", "broken", "at_truck")
        if not isinstance(state, str):
            raise TypeError("package state must be a str")
        elif state not in valid_states:
            raise ValueError(f"State must be one of {valid_states}")
        else:
            self.__state = state

    # sprite property
    @property
    def sprite(self) -> tuple:
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite: tuple):
        if not isinstance(sprite, tuple):
            raise TypeError("sprite must be a tuple")
        elif len(sprite) != 6:
            raise ValueError("sprite lenght must be 6")
        else:
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
