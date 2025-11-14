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
        self.score = 0
        self.fails = 0

        self.mario = Character("MARIO")
        # self.luigi = Character("LUIGI")
        # self.boss = Character("BOSS")

        self.truck = Truck()

        # Public Methods
        # self.menu_screen()
        self.difficulty0()
        # self.difficulty1()
        # self.difficulty2()
        # self.difficulty3()
        self.update()
        self.draw()

        # Private Methods
        self.top_menu()

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

    def difficulty0(self):
        self.number_of_conveyors = 5 + 1  # The one represents the conveyor 0
        self.conveyors = [
                Conveyor(i, 1) for i in range(self.number_of_conveyors)
                ]
        self.packages = []
        self.number_of_packages = 1
        self.points_for_package = 50

    @staticmethod
    def tests(self):
        # tests
        pyxel.text(32, 16, f"Width: {config.WIDTH}", 7)
        pyxel.text(32, 32, f"Height: {config.HEIGHT}", 7)

        # visualizer for tiles
        # horizontal
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

    def top_menu(self):
        # This creates the menu at the top with Exit, score, fails and menu
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

    def update(self):
        # To exit the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):

        # self.tests(self)

        if self.difficulty == 0:
            for conveyor in self.conveyors:
                conveyor.draw()
            for i in range(self.number_of_conveyors):
                if i % 2 == 0:  # Even platforms for mario
                    pyxel.blt(config.WIDTH - 4.5*config.TILE_DIMENSION,
                              config.HEIGHT - (i+0.5)*config.TILE_DIMENSION,
                              *config.STAIR)
                    for j in range(3):
                        pyxel.blt(
                            config.WIDTH - (3.5 + j*0.5)*config.TILE_DIMENSION,
                            config.HEIGHT - (i+1.5)*config.TILE_DIMENSION,
                            *config.HOR_HALF_PIPE)
                else:
                    pyxel.blt(4*config.TILE_DIMENSION,
                              config.HEIGHT - (i+0.5)*config.TILE_DIMENSION,
                              *config.STAIR)
                    for j in range(3):
                        pyxel.blt(
                            (3.5 + j*0.5)*config.TILE_DIMENSION,
                            config.HEIGHT - (i+1.5)*config.TILE_DIMENSION,
                            *config.HOR_HALF_PIPE)

            self.truck.draw()
            self.mario.draw()

        self.draw_pipe()
        self.draw_machine()

        self.top_menu()