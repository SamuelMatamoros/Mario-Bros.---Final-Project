import config
import pyxel


class Character:
    """
    Character class

    This class holds the code for the character behaviour.
    """

    def __init__(self, character: str):
        """
        Init method for character class.

        Attributes:
            character : str
                The name of the character in all caps
        """

        # Attributes
        self.character = character.upper()
        self.level = 0
        self.has_package = False
        self.resting = False

        self.__sprite_frame_count = -1

        self.reprimand = False

        self.boss_active = False
        self.boss_target = "NONE"
        self.boss_timer = 0

    # level property
    @property
    def level(self) -> int:
        """The level property"""
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int):
            raise ValueError("Level must be an integer")
        elif level < 0:
            raise ValueError("Level must be greater or equal to 0")
        self.__level = level

    # has_package property
    @property
    def has_package(self) -> bool:
        """The has_package property"""
        return self.__has_package

    @has_package.setter
    def has_package(self, has_package: bool):
        if not isinstance(has_package, bool):
            raise TypeError("has_package must be a boolean")
        self.__has_package = has_package

    @property
    def character(self) -> str:
        """The character property"""
        return self.__character

    @character.setter
    def character(self, character: str):
        if not isinstance(character, str):
            raise TypeError("character must be a string")
        elif character not in config.CHARACTERS:
            raise ValueError("character must be one of:",
                             str(config.CHARACTERS))
        else:
            self.__character = character

    @property
    def boss_target(self):
        """The boss_target property."""
        return self.__boss_target

    @boss_target.setter
    def boss_target(self, value):
        if not isinstance(value, str):
            raise TypeError("'boss_target' must be a string")
        elif value not in ("MARIO", "LUIGI", "BOTH", "NONE"):
            raise ValueError("'boss_target' must be Mario or Luigi")
        else:
            self.__boss_target = value

    @property
    def boss_timer(self):
        """The boss_timer property."""
        return self.__boss_timer

    @boss_timer.setter
    def boss_timer(self, value):
        if not isinstance(value, int):
            raise TypeError("'boss_timer' must be a string")
        else:
            self.__boss_timer = value

    @property
    def boss_active(self):
        """The boss_active property."""
        return self.__boss_active

    @boss_active.setter
    def boss_active(self, value):
        if not isinstance(value, bool):
            raise TypeError("'boss_active' must be a bool")
        else:
            self.__boss_active = value

    def __sprite_decide(self, max_level):
        """
        Method for deciding the self.__sprite.

        It depends on the level the character has and wheather he is holding
        package or not.
        """
        if self.character == "MARIO":
            self.__x = 12*config.TILE_DIMENSION-config.TILE_DIMENSION//2
            self.__y = 10*config.TILE_DIMENSION+config.TILE_DIMENSION//2+2
            if self.level == 0:
                if self.has_package or 0 <= self.__sprite_frame_count <= 10:
                    self.__sprite = config.MARIO_PACKAGE
                    self.__sprite_frame_count += 1
                else:
                    self.__sprite = config.MARIO_DEF_RIGHT
                    self.__sprite_frame_count = -1
            elif self.has_package or 0 <= self.__sprite_frame_count <= 10:
                self.__sprite = config.MARIO_PACKAGE
                self.__sprite_frame_count += 1
            else:
                self.__sprite = config.MARIO_DEF_LEFT
                self.__sprite_frame_count = -1

            if self.reprimand:
                self.__sprite = config.MARIO_REPRIMAND

            if self.resting:
                self.__sprite = config.MARIO_REST

        if self.character == "LUIGI":
            self.__x = 4 * config.TILE_DIMENSION-config.TILE_DIMENSION//4
            self.__y = 9 * config.TILE_DIMENSION+config.TILE_DIMENSION//2+2
            if self.level == max_level//2 - 1:
                if self.has_package or 0 <= self.__sprite_frame_count <= 10:
                    self.__sprite = config.LUIGI_PACKAGE_INVERTED
                    self.__sprite_frame_count += 1
                    self.has_package = False
                else:
                    self.__sprite = config.LUIGI_DEF_RIGHT
                    self.__sprite_frame_count = -1
            elif self.has_package or 0 <= self.__sprite_frame_count <= 10:
                self.__sprite = config.LUIGI_PACKAGE
                self.__sprite_frame_count += 1
            else:
                self.__sprite = config.LUIGI_DEF_RIGHT
                self.__sprite_frame_count = -1

            if self.reprimand:
                self.__sprite = config.LUIGI_REPRIMAND

            if self.resting:
                self.__sprite = config.LUIGI_REST

        if self.character == "BOSS":
            if self.boss_target == "LUIGI":
                self.__x = 1 * config.TILE_DIMENSION
                self.__y = 10 * config.TILE_DIMENSION
                self.__sprite = config.BOSS_ARMS_DOWN
                prev_sprite = config.BOSS_ARMS_UP
            else:
                self.__x = config.WIDTH - 2*config.TILE_DIMENSION
                self.__y = config.HEIGHT - 3.5*config.TILE_DIMENSION
                self.__sprite = config.BOSS_ARMS_DOWN_INVERTED
                prev_sprite = config.BOSS_ARMS_UP_INVERTED

            if self.boss_target == "BOTH":
                self.__x = config.WIDTH - 2*config.TILE_DIMENSION
                self.__y = config.HEIGHT - 3.5*config.TILE_DIMENSION
                self.__sprite = config.BOSS_ARMS_DOWN_INVERTED
                prev_sprite = config.BOSS_ARMS_UP_INVERTED

            if pyxel.frame_count % 20 < 10:
                self.__sprite, prev_sprite = prev_sprite, self.__sprite

    def update(self, max_level, sound):
        """Update method for character class."""

        if not (self.resting or self.reprimand):
            if self.character == "MARIO":
                up_key = pyxel.KEY_UP
                down_key = pyxel.KEY_DOWN
            if self.character == "LUIGI":
                up_key = pyxel.KEY_W
                down_key = pyxel.KEY_S

            if pyxel.btnp(up_key) and max_level//2 - 1 > self.level:
                self.level += 1
                if sound:
                    pyxel.play(3, 16)
            if pyxel.btnp(down_key) and 0 < self.level:
                self.level -= 1
                if sound:
                    pyxel.play(3, 17)

    def draw(self, max_level):
        """Draw method for character class."""
        self.__sprite_decide(max_level)
        pyxel.blt(self.__x, self.__y - 2*self.level*config.TILE_DIMENSION,
                  *self.__sprite, scale=1.3)
