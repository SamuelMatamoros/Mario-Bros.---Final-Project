import random
import pyxel
import config
from characters import Character
from conveyors import Conveyor
from package import Package
from truck import Truck


class Board:
    """ Class for the game board """

    def __init__(self):
        """
        Method that creates the board.
        """

        # Attributes
        self.difficulty = 0
        self.__previous_difficulty = -1

        self.score = 0
        self.fails = 0

        self.menu_active = False
        self.__menu_selected = self.difficulty

        self.mario = Character("MARIO")
        self.luigi = Character("LUIGI")

        self.truck = Truck()

    """
    PROPERTIES AND SETTERS SECTION
    """

    @property
    def difficulty(self):
        """The difficulty property."""
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        if not isinstance(difficulty, int):
            raise TypeError("difficulty must be an integer")
        elif difficulty < 0:
            raise ValueError("difficulty must be positive")
        else:
            self.__difficulty = difficulty

    @property
    def score(self):
        """The score property."""
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise TypeError("score must be an integer")
        elif score < 0:
            raise ValueError("score must be positive")
        else:
            self.__score = score

    @property
    def fails(self):
        """The fails property."""
        return self.__fails

    @fails.setter
    def fails(self, fails):
        if not isinstance(fails, int):
            raise TypeError("fails must be an integer")
        elif fails < 0:
            raise ValueError("fails must be positive")
        else:
            self.__fails = fails

    """
    METHODS SECTION
    """

    ################
    # MENU SECTION #
    ################

    def menu_update(self):
        if pyxel.btnp(pyxel.KEY_M):
            if self.menu_active:
                self.menu_active = False
            else:
                self.menu_active = True
        if self.menu_active:
            if pyxel.btnp(pyxel.KEY_UP) and self.__menu_selected > 0:
                self.__menu_selected -= 1
            if pyxel.btnp(pyxel.KEY_DOWN) and self.__menu_selected < 3:
                self.__menu_selected += 1
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.difficulty = self.__menu_selected
                # The line below resets the position of the menu after
                # confirming the difficulty
                # self.__menu_selected = 0
                self.menu_active = False

    def menu_draw(self):
        pyxel.dither(0.6)
        pyxel.rect(0, 0, config.WIDTH, config.HEIGHT, 1)
        pyxel.dither(1)
        pyxel.rect(32, 32,
                   config.WIDTH - 4*config.TILE_DIMENSION,
                   config.HEIGHT - 4*config.TILE_DIMENSION, 9)
        pyxel.rectb(32, 32,
                    config.WIDTH - 4*config.TILE_DIMENSION,
                    config.HEIGHT - 4*config.TILE_DIMENSION, 3)
        pyxel.rectb(32 + 1, 32 + 1,
                    config.WIDTH - 4*config.TILE_DIMENSION - 1,
                    config.HEIGHT - 4*config.TILE_DIMENSION - 1, 3)

        pyxel.text(36, 36, "CLOSE: (M)", 3)
        pyxel.text(config.WIDTH/2 - 8, 36, "MENU", 3)
        pyxel.text(config.WIDTH - 6*config.TILE_DIMENSION, 36,
                   "CONFIRM: (ENTER)", 3)

        for i in range(4):
            if i == self.__menu_selected:
                col = 11
            else:
                col = 3
            pyxel.text(config.WIDTH//2 - 24,
                       config.HEIGHT//3 + i*16,
                       f"Difficulty {i}",
                       col)

    def top_menu(self):
        # This creates the menu at the top with Exit, fails, fails and menu
        text_y = 9
        text_col = 7

        pyxel.rect(8, 8, 17, 7, 11)
        pyxel.text(9, text_y, "EXIT", text_col)

        pyxel.rect(config.WIDTH - 1.5*config.TILE_DIMENSION,
                   8, 17, 7, 9)
        pyxel.text(config.WIDTH - 1.5*config.TILE_DIMENSION + 1,
                   text_y, "MENU", text_col)

        pyxel.text(4*config.TILE_DIMENSION + 1,
                   text_y, f"SCORE: {self.score}", text_col)

        pyxel.text(10*config.TILE_DIMENSION + 1,
                   text_y, f"FAILS: {self.fails}", text_col)

    ######################
    # DIFFICULTY SECTION #
    ######################

    @staticmethod
    def __check_difficulty(self):

        if self.difficulty != self.__previous_difficulty:
            self.mario.level = 0
            self.luigi.level = 0
            self.__previous_difficulty = self.difficulty

            if self.difficulty == 0:
                self.difficulty0()
            elif self.difficulty == 1:
                self.difficulty1()
            elif self.difficulty == 2:
                self.difficulty2()
            elif self.difficulty == 3:
                self.difficulty3()

    def difficulty0(self):
        self.number_of_conveyors = 5 + 1  # The one represents the conveyor 0
        self.conveyor_speed = 1
        self.conveyors = [
                Conveyor(i, 1) for i in range(self.number_of_conveyors)
                ]
        self.packages = []
        self.number_of_packages = 1
        self.points_for_package = 50

        for i in range(self.number_of_packages):
            self.packages.append(Package("CONVEYOR"))

    def difficulty1(self):
        self.number_of_conveyors = 7 + 1  # The one represents the conveyor 0
        for i in range(self.number_of_conveyors):
            if i == 0:
                self.conveyor_speed = 1
            elif i % 2 == 0:
                self.conveyor_speed = 1
            else:
                self.conveyor_speed = 1.5

            self.conveyors.append(Conveyor(i, self.conveyor_speed))

        self.packages = []
        self.number_of_packages = 1
        self.points_for_package = 50

    def difficulty2(self):
        self.number_of_conveyors = 9 + 1  # The one represents the conveyor 0
        for i in range(self.number_of_conveyors):
            if i == 0:
                self.conveyor_speed = 1
            elif i % 2 == 0:
                self.conveyor_speed = 1.5
            else:
                self.conveyor_speed = 2

            self.conveyors.append(Conveyor(i, self.conveyor_speed))

        self.packages = []
        self.number_of_packages = 1
        self.points_for_package = 50

    def difficulty3(self):
        self.number_of_conveyors = 5 + 1  # The one represents the conveyor 0
        for i in range(self.number_of_conveyors):
            if i == 0:
                self.conveyor_speed = 1
            else:
                self.conveyor_speed = 1 + random.randint(1, 3)//2

            self.conveyors.append(Conveyor(i, self.conveyor_speed))

        self.packages = []

        self.number_of_packages = 1
        self.points_for_package = 50

    ####################
    # DRAWINGS SECTION #
    ####################

    @staticmethod
    def tests(self,
              dim=False,
              level=False,
              difficulty=False,
              tiles=False):
        # tests
        if dim:
            pyxel.text(32, 16, f"Width: {config.WIDTH}", 7)
            pyxel.text(32, 32, f"Height: {config.HEIGHT}", 7)

        if level:
            pyxel.text(196, 32, f"Mario level: {self.mario.level}", 7)
            pyxel.text(196, 48, f"Luigi level: {self.luigi.level}", 7)

        if difficulty:
            pyxel.text(196, 32, f"Difficulty: {self.difficulty}", 7)
            pyxel.text(196, 48, f"Prev diff: {self.__previous_difficulty}", 7)

        # visualizer for tiles
        if tiles:
            for i in range(config.TILES_OF_WIDTH):
                pyxel.rect(config.TILE_DIMENSION*i, 0, 16, 16, i)
            for i in range(config.TILES_OF_HEIGHT):
                pyxel.rect(0, config.TILE_DIMENSION*i, 16, 16, i)

    @staticmethod
    def draw_pipe():
        # # This creates the pipe in the middle
        for i in range(config.TILES_OF_HEIGHT):
            pyxel.blt(config.WIDTH//2 - 8,  # puts the pipe in the middle
                      config.TILE_DIMENSION * i,
                      *config.PIPE_BIG)

    @staticmethod
    def draw_machine():
        pyxel.blt(config.WIDTH - 2*config.TILE_DIMENSION,
                  config.HEIGHT - 2*config.TILE_DIMENSION,
                  *config.MACHINE)
        pyxel.blt(config.WIDTH - 1*config.TILE_DIMENSION,
                  config.HEIGHT - 3*config.TILE_DIMENSION,
                  *config.DOOR)

    @staticmethod
    def draw_platforms(level):
        for i in range(level):
            if i % 2 == 0:  # Even platforms for mario
                pyxel.blt(config.WIDTH - 4.25*config.TILE_DIMENSION,
                          config.HEIGHT - (i)*config.TILE_DIMENSION,
                          *config.STAIR)
                for j in range(2):
                    pyxel.blt(
                        config.WIDTH - (3.75 + j*0.5)*config.TILE_DIMENSION,
                        config.HEIGHT - (i+1)*config.TILE_DIMENSION,
                        *config.HOR_HALF_PIPE)
            else:
                pyxel.blt(4*config.TILE_DIMENSION - config.TILE_DIMENSION//2,
                          config.HEIGHT - (i)*config.TILE_DIMENSION,
                          *config.STAIR)
                for j in range(2):
                    pyxel.blt(
                        (3.5 + j*0.5)*config.TILE_DIMENSION,
                        config.HEIGHT - (i+1)*config.TILE_DIMENSION,
                        *config.HOR_HALF_PIPE)

    def update(self):

        self.__check_difficulty(self)

        self.mario.update(self.number_of_conveyors)
        self.luigi.update(self.number_of_conveyors)

        for package in self.packages:
            package.update()

            if package.at_the_end():
                if package.level == self.number_of_conveyors - 1:
                    print("success")
                    self.truck.number_of_packages += 1
                    self.packages.remove(package)
                if package.level % 2 == 0:
                    if package.level == self.mario.level * 2:
                        package.move_to_next_conveyor()
                    else:
                        package.broken()
                        self.packages.remove(package)
                        if self.fails < 3:
                            self.fails += 1
                else:
                    if package.level == self.luigi.level * 2 + 1:
                        package.move_to_next_conveyor()
                    else:
                        package.broken()
                        self.packages.remove(package)
                        if self.fails < 3:
                            self.fails += 1

    def draw(self):

        # self.tests(self, tiles=True, level=True)

        for conveyor in self.conveyors:
            conveyor.draw()

        for package in self.packages:
            package.draw()

        self.draw_platforms(self.number_of_conveyors)

        self.truck.draw(self.number_of_conveyors)

        self.mario.draw()
        self.luigi.draw()

        self.draw_pipe()
        self.draw_machine()

        self.top_menu()
