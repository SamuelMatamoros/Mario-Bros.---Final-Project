import config
import pyxel


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

    def __init__(self, level: int, speed: float):
        """
        This method is used to create Conveyor objects.

        :param level: int. Platform number (e.g., 1, 2, 3) of the conveyor.
        :param direction: str. Direction of conveyor, either "left" or "right".
        :param speed: int. Speed at which the conveyor moves packages.
        :param sprite: str. Reference to the sprite for the conveyor.
        """
        self.level = level
        self.speed = float(speed)
        self.packages = []

        self.draw()

    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int):
            raise TypeError("Level must be an int greater or equal to 0")
        elif level < 0:
            raise ValueError("Level must be greater or equal to 0")
        else:
            self.__level = level

    # speed property
    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        if not isinstance(speed, float):
            raise ValueError("Speed must be float")
        elif speed <= 0:
            raise ValueError("Speed must be a positive float")
        else:
            self.__speed = speed

    def draw(self):
        """
        Draw the conveyor
        """
        if self.level == 0:
            for i in range(3):
                pyxel.blt(13 * config.TILE_DIMENSION,
                          10 * config.TILE_DIMENSION,
                          *config.CONVEYOR_0[i])
        elif self.level % 2 == 0:  # Even conveyors
            for i in config.CONVEYOR_0:
                pyxel.blt(5 * config.TILE_DIMENSION + config.TILE_DIMENSION//2,
                          config.TILES_OF_HEIGHT - self.level * config.TILE_DIMENSION,
                          *config.CONVEYOR_0[i])
        else:
            for i in config.CONVEYOR_0:
                pyxel.blt(5 * config.TILE_DIMENSION,
                          config.TILES_OF_HEIGHT - self.level * config.TILE_DIMENSION,
                          *config.CONVEYOR_0[i])

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the conveyor.
        """
        return ("Level", self.level,
                "\nSpeed:", self.speed,
                "\nPackages:", self.packages)

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the conveyor.
        """
        return self.__str__()
