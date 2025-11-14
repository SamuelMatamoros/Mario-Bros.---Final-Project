import config
import pyxel


class Truck:
    """
    Class for the truck, with a fixed head and a variable bed depending on cargo.
    """

    def __init__(self):
        # Attributes
        self.number_of_packages = 0

        # Methods
        self.draw()

    # loaded_boxes property
    @property
    def loaded_boxes(self) -> int:
        return self.__loaded_boxes

    @loaded_boxes.setter
    def loaded_boxes(self, loaded_boxes: int):
        if not isinstance(loaded_boxes, int):
            raise TypeError("loaded_boxes must be an integer")
        elif loaded_boxes < 0 or loaded_boxes > 8:
            raise ValueError("loaded_boxes must be between 0 and 8")
        self.__loaded_boxes = loaded_boxes

    def draw(self):
        """Draws the truck: fixed head, variable bed based on loaded_boxes."""
        # Draw truck head at fixed position (adjust x, y as needed)
        pyxel.blt(
            8,
            6 * config.TILE_DIMENSION,
            *config.TRUCK_HEAD
        )
        # Draw beds/cargo
        pyxel.blt(
            8 + config.TILE_DIMENSION,
            6 * config.TILE_DIMENSION,
            *config.TRUCK_BED[self.number_of_packages]
        )
        # Draw structure arround
        for i in range(5):
            pyxel.blt(i * 8,
                      6 * config.TILE_DIMENSION + 4,
                      *config.HOR_HALF_PIPE)
        pyxel.blt(5 * 8,
                  6 * config.TILE_DIMENSION + 4,
                  *config.L_PIPE)
