import config
import pyxel


class Package:
    """
    Class for a package in the game.

    Attributes:
        level : int
            The conveyor level of the package (starts at 0, ends at 6).
        state : str
            The state of the package. "in_conveyor", "handled", "broken",
            "at_truck", "other".
    """

    def __init__(self, state: str = "in_conveyor"):
        # Attributes
        self.level = 0              # initial level set to 0
        self.x = config.WIDTH - 1*config.TILE_DIMENSION
        self.y = config.HEIGHT - 2*config.TILE_DIMENSION - 4
        self.speed = 1
        self.state = state
        self.pipe_passes = 0   # i have to do setter and property
        self.crossed_pipe = False

        self.__x_tick = 0
        self.__y_tick = -1
        self.__at_the_end = False

    # level property
    @property
    def level(self) -> int:
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
        return self._speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'speed' must be a number")
        elif value < 0 or value > 2:
            return ValueError("'speed' must be beetwen 0.5 and 2")
        else:
            self._speed = value

    # state property
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        if not isinstance(state, str):
            raise TypeError("state must be a string")
        elif state not in config.PACKAGE_STATES:
            raise ValueError(f"state must be one of: {config.PACKAGE_STATES}")
        self.__state = state

    def at_the_end(self):
        return self.__at_the_end

    def broken(self):
        self.__at_the_end = False
        self.state = "BROKEN"

    def move_to_next_conveyor(self):

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
            self.crossed_pipe = False

    def update(self):
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

            if not self.crossed_pipe:
                if (old_x > config.PIPE_X and self.x <= config.PIPE_X):
                    print("######## CRUCE DERECHA -> IZQUIERDA ########")
                    self.pipe_passes = min(self.pipe_passes + 1, 4)
                    self.crossed_pipe = True
                elif (old_x < config.PIPE_X and self.x >= config.PIPE_X):
                    print("######## CRUCE IZQUIERDA -> DERECHA ########")
                    self.pipe_passes = min(self.pipe_passes + 1, 4)
                    self.crossed_pipe = True

                            

    def draw(self):
        if self.state == "CONVEYOR":
            sprite_idx = min(self.pipe_passes, len(config.PACKAGE_SPRITE) - 1)
            sprite = config.PACKAGE_SPRITE[sprite_idx]
            print(f"Drawing sprite index: {sprite_idx} for pipe_passes: {self.pipe_passes}")
        else:  # For all other states
            sprite = (2, 0, 0, 8, 8, 0)  # Empty sprite (or broken/handled as needed)
        pyxel.blt(self.x, self.y, *sprite)




