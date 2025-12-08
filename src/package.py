import config
import pyxel


class Package:
    """
    Class for a package in the game.

    Attributes:
        x : int
            x position on the board
        y : int
            y position on the board
        speed : float
            the speed at which the package updates
        level : int
            The conveyor level of the package (starts at 0, ends at 6).
        state : str
            The state of the package. "CONVEYOR", "HANDLED", "BROKEN",
            "TRUCK".
    """

    def __init__(self, state: str = "in_conveyor"):
        # Attributes
        self.x = config.WIDTH - 1*config.TILE_DIMENSION
        self.y = config.HEIGHT - 2*config.TILE_DIMENSION - 4
        self.level = 0
        self.speed = 1
        self.state = state

        self.__x_tick = 0
        self.__y_tick = -1
        self.__at_the_end = False
        self.__pipe_passes = 0
        self.__crossed_pipe = False

    # level property
    @property
    def level(self) -> int:
        """The level property"""
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int):
            raise TypeError("level must be an integer")
        elif level < 0 or level > 11:
            raise ValueError("level must be beetwen 0 and 6")
        self.__level = level

    # speed property
    @property
    def speed(self):
        """The speed property."""
        return self.__speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'speed' must be a number")
        elif value < 0 or value > 2:
            return ValueError("'speed' must be beetwen 0.5 and 2")
        else:
            self.__speed = value

    # state property
    @property
    def state(self) -> str:
        """The state property"""
        return self.__state

    @state.setter
    def state(self, state: str):
        if not isinstance(state, str):
            raise TypeError("state must be a string")
        elif state not in config.PACKAGE_STATES:
            raise ValueError(f"state must be one of: {config.PACKAGE_STATES}")
        self.__state = state

    def at_the_end(self):
        """Method that returns True if the package is at the end"""
        return self.__at_the_end

    def broken(self, sound):
        """
        Method executed when a package is at the end but the character
        is not.
        """
        self.__at_the_end = False
        self.state = "BROKEN"
        if sound:
            pyxel.play(3, 19)

    def move_to_next_conveyor(self, sound):
        """
        Method that moves the package to the next level.
        """

        self.__at_the_end = False

        self.__y_tick += 1
        if self.level != 0:
            self.y -= config.TILE_DIMENSION

        self.level += 1
        self.__x_tick = 0

        if self.level % 2 == 0:
            self.x = 4.5 * config.TILE_DIMENSION + 8
        else:
            self.x = 10 * config.TILE_DIMENSION + 8

        if self.level <= 5:
            self.__crossed_pipe = False

        if sound:
            pyxel.play(3, 20)

    def update(self, sound):
        """
        update method for package class
        """

        old_x = self.x
        frames = 90 - 30 * self.speed

        if pyxel.frame_count % frames == 0:

            if self.level == 0:
                if self.__x_tick < 4:
                    self.x -= config.TILE_DIMENSION//2
                    self.__x_tick += 1
                else:
                    self.__at_the_end = True
            elif self.level % 2 == 0:
                if self.__x_tick < 6:
                    self.x += config.TILE_DIMENSION
                    self.__x_tick += 1
                else:
                    self.__at_the_end = True
            else:
                if self.__x_tick < 6:
                    self.x -= config.TILE_DIMENSION
                    self.__x_tick += 1
                else:
                    self.__at_the_end = True

            if not self.__crossed_pipe:
                if (old_x > config.PIPE_X and self.x <= config.PIPE_X):
                    self.__pipe_passes = min(self.__pipe_passes + 1, 4)
                    self.__crossed_pipe = True
                elif (old_x < config.PIPE_X and self.x >= config.PIPE_X):
                    self.__pipe_passes = min(self.__pipe_passes + 1, 4)
                    self.__crossed_pipe = True

            if sound:
                pyxel.play(2, 22)

    def draw(self):
        if self.state == "CONVEYOR":
            sprite_idx = min(self.__pipe_passes,
                             len(config.PACKAGE_SPRITE) - 1)
            sprite = config.PACKAGE_SPRITE[sprite_idx]
        else:
            # Empty sprite (or broken/handled as needed)
            sprite = (2, 0, 0, 8, 8, 0)
        pyxel.blt(self.x, self.y, *sprite)
