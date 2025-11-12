import settings


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
        :param loaded_packages: int. Number of packages inside the truck.
        :param sprite: str. Reference to the sprite for the truck.
        """
        self.loaded_packages = 0
        self.sprite = settings.TRUCK_BED_0

    # loaded_packages property
    @property
    def loaded_packages(self) -> int:
        return self.__loaded_packages

    @loaded_packages.setter
    def loaded_packages(self, loaded_packages: int):
        if not isinstance(loaded_packages, int):
            raise TypeError("loaded_packages must be an integer")
        elif loaded_packages < 0:
            raise ValueError("loaded_packages cannot be negative")
        else:
            self.__loaded_packages = loaded_packages
