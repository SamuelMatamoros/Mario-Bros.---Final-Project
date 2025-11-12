import settings


class Conveyor:
    """
    Class to represent a conveyor belt in the game.

    Attributes:
        level : int
            The current level/platform the conveyor is on.
        direction : str
            The direction of movement on the conveyor, either "odd" or "even".
        speed : int
            The speed at which the conveyor moves packages.
        sprite : str
            The path or identifier for the conveyor's sprite image.
    """

    def __init__(self, side: int, level: int, direction: str, speed: int):
        """
        This method is used to create Conveyor objects.

        :param level: int. Platform number (e.g., 1, 2, 3) of the conveyor.
        :param direction: str. Direction of conveyor, either "left" or "right".
        :param speed: int. Speed at which the conveyor moves packages.
        :param sprite: str. Reference to the sprite for the conveyor.
        """
        self.level = level
        self.direction = direction
        self.speed = speed
        self.sprite = settings.CONVEYOR_0  # To be changed

    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int) or level < 0:
            raise ValueError("Level must be an int greater or equal to 0")
        self.__level = level

    # direction property
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        if direction not in ("odd", "even"):
            raise ValueError('Direction must be "odd" or "even"')
        self.__direction = direction

    # speed property
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        if not isinstance(speed, int) or speed <= 0:
            raise ValueError("Speed must be a positive integer")
        self.__speed = speed

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
        Return a human-readable string representation of the conveyor.
        """
        return (f"Conveyor at level {self.level}, direction: {self.direction},"
                f"speed: {self.speed}, sprite: {self.sprite}")

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the conveyor.
        """
        return self.__str__()
