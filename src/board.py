import pyxel
import config
from conveyors import Conveyor
from characters import Character


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

        # Public Methods
        # self.menu()
        self.difficulty0()
        # self.difficulty1()
        # self.difficulty2()
        # self.difficulty3()
        self.update()
        self.draw()

        # Private Methods

    def difficulty0(self):
        self.number_of_conveyors = 5
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
            pyxel.blt(config.WIDTH//2,  # puts the pipe in the 8th tile
                      config.TILE_DIMENSION * i,
                      *config.PIPE_BIG)

    def update(self):
        # To exit the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):

        # self.tests(self)

        self.draw_pipe()

        if self.difficulty == 0:
            self.mario = Character("MARIO")
            self.mario.draw()
