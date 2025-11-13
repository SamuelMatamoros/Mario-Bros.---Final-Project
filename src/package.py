import config
import pyxel

class Package:
    """
    Class for a package in the game.

    Attributes:
        level : int
            The conveyor/platform level of the package (starts at 0, ends at 6).
        state : str
            The state of the package. "in_conveyor", "handled", "broken", "at_truck", "other".
    """

    def __init__(self, state: str = "in_conveyor"):
        # Attributes
        self.level = 0              # initial level set to 0
        self.state = state

        # Methods
        self.draw(12, 10)           # Example position; adjust as needed (i dont know yet the exact positions on the board)

    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int):
            raise ValueError("level must be an integer")
        elif level < 0 or level > 6:
            raise ValueError("level must be beetwen 0 and 6")
        self.__level = level

    # state property
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        valid_states = ["in_conveyor", "handled", "broken", "at_truck", "other"]
        if not isinstance(state, str):
            raise TypeError("state must be a string")
        elif state not in valid_states:
            raise ValueError(f"state must be one of: {valid_states}")
        self.__state = state

    def draw(self, x: int, y: int):
        """
        Draws the package at position (x, y).
        Uses sprite index based on state.
        """
        state_to_index = {
            "in_conveyor": 0,
            "handled": 1,
            "broken": 2,
            "at_truck": 3,
            "other": 4
        }
        sprite_index = state_to_index[self.state]
        pyxel.blt(
            x * config.TILE_DIMENSION,
            y * config.TILE_DIMENSION,
            *config.PACKAGE_SPRITE[sprite_index]
        )
