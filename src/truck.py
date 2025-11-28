import config
import pyxel


class Truck:
    """
    Class for the truck, with a fixed head and a variable bed depending on
    cargo.
    """

    def __init__(self):
        # Attributes
        self.number_of_packages = 0
        self.state = "LOADING"

    # number_of_packages property
    @property
    def number_of_packages(self) -> int:
        return self.__number_of_packages

    @number_of_packages.setter
    def number_of_packages(self, number_of_packages: int):
        if not isinstance(number_of_packages, int):
            raise TypeError("number_of_packages must be an integer")
        elif number_of_packages < 0 or number_of_packages > 8:
            raise ValueError("number_of_packages must be between 0 and 8")
        else:
            self.__number_of_packages = number_of_packages

    @property
    def state(self):
        """The state property."""
        return self.__state

    @state.setter
    def state(self, value):
        if not isinstance(value, str):
            raise TypeError("state must be a string")
        elif value not in ("LOADING", "DELIVERY"):
            raise ValueError("state must be either 'LOADING' or 'DELIVERY'")
        else:
            self.__state = value

    def draw(self, level):
        """
        Draws the truck: fixed head, variable bed based on number_of_packages.
        """
        # Draw truck head at fixed position (adjust x, y as needed)
        pyxel.blt(
            8,
            12*config.TILE_DIMENSION - level*config.TILE_DIMENSION + 4,
            *config.TRUCK_HEAD
        )
        # Draw beds/cargo
        pyxel.blt(
            8 + config.TILE_DIMENSION,
            12*config.TILE_DIMENSION - level*config.TILE_DIMENSION + 4,
            *config.TRUCK_BED[self.number_of_packages]
        )
        # Draw structure arround
        for i in range(4):
            pyxel.blt(i * 8,
                      12*config.TILE_DIMENSION - level*config.TILE_DIMENSION+8,
                      *config.HOR_HALF_PIPE)
        pyxel.blt(4 * 8,
                  12*config.TILE_DIMENSION - level * config.TILE_DIMENSION+8,
                  *config.L_PIPE)
