class Truck:
    """
    Class to represent the delivery truck in the game.

    Attributes:
        level : int
            The current level/platform where the truck is positioned.
        loaded_packages : int
            The number of packages currently inside the truck.
        sprite : str
            The path or identifier for the truck's sprite image.
    """

    def __init__(self):
        """
        This method is used to create Truck objects.

        :param level: int. Platform number (e.g., 1, 2, 3) where the truck is located.
        :param loaded_packages: int. Number of packages currently inside the truck.
        :param sprite: str. Reference to the sprite for the truck.
        """
        self.loaded_packages = 0
        if self.loaded_packages == 0:
            self.sprite = "truck0.png"
        elif self.loaded_packages == 1:
            self.sprite = "truck1.png"
        elif self.loaded_packages == 2:
            self.sprite = "truck2.png"
        elif self.loaded_packages == 3:
            self.sprite = "truck3.png"
        elif self.loaded_packages == 4:
            self.sprite = "truck4.png"
        elif self.loaded_packages == 5:
            self.sprite = "truck5.png"
        elif self.loaded_packages == 6:
            self.sprite = "truck6.png"
        elif self.loaded_packages == 7:
            self.sprite = "truck7.png"
        elif self.loaded_packages == 8:
            self.sprite = "truck_full.png"
        # All this "image_x.png to be changed to the correct format"


    # loaded_packages property
    @property
    def loaded_packages(self) -> int:
        return self.__loaded_packages

    @loaded_packages.setter
    def loaded_packages(self, loaded_packages: int):
        if not isinstance(loaded_packages, int) or loaded_packages < 0:
            raise ValueError("loaded_packages must be a non-negative integer")
        self.__loaded_packages = loaded_packages

