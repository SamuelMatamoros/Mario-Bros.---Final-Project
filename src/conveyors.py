import config
import pyxel


class Conveyor:
    """
    Class to represent a conveyor belt in the game.

    Attributes:
        level : int
            The self.__current level/platform the conveyor is on.
        speed : int
            The speed at which the conveyor moves packages.
    """

    def __init__(self, level: int, speed: float):
        """
        This method is used to create Conveyor objects.

        :param level: int. Platform number (e.g., 1, 2, 3) of the conveyor.
        :param speed: int. Speed at which the conveyor moves packages.
        """
        self.level = level
        self.speed = float(speed)

        self.__current = config.CONVEYOR_0
        self.__previous = config.CONVEYOR_1

    def __str__(self):
        string = (f"level: {self.level}\n"
                  f"speed: {self.speed}\n")

        return string

    def __repr__(self):
        return self.__str__()

    # level property
    @property
    def level(self) -> int:
        """The level property"""
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
        """The speed property"""
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
        Draw the conveyor.
        """

        frame_rate = 120 - 30*self.speed

        # This animates the coveyors depending on the speed
        if pyxel.frame_count % frame_rate == 0:
            self.__previous, self.__current = self.__current, self.__previous
        # self.__current = config.CONVEYOR_1

        if self.level == 0:
            for i in range(3):
                pyxel.blt((13 + i) * config.TILE_DIMENSION,
                          10 * config.TILE_DIMENSION,
                          *self.__current[i])
        elif self.level % 2 == 0:  # Even conveyors
            for i in range(len(self.__current)):
                pyxel.blt(
                    (5 + i) * config.TILE_DIMENSION + config.TILE_DIMENSION//4,
                    config.HEIGHT - (self.level + 1) * config.TILE_DIMENSION,
                    *self.__current[i])
        else:
            for i in range(len(self.__current)):
                pyxel.blt(
                    (5 + i) * config.TILE_DIMENSION,
                    config.HEIGHT - (self.level + 1) * config.TILE_DIMENSION,
                    *self.__current[i])
