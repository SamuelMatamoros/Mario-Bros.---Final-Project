import pyxel
import config

from board import Board


class Main:
    """
    Main class for the game
    """

    def __init__(self):
        pyxel.init(config.WIDTH,
                   config.HEIGHT,
                   "Mario Bros.",
                   fps=60,
                   quit_key=pyxel.KEY_Q,
                   capture_scale=3,
                   capture_sec=0)
        pyxel.load("../assets/assets.pyxres")
        self.board = Board()

        pyxel.run(self.update, self.draw)

    def update(self):
        """
        Update method for main class
        """
        self.board.update()

    def draw(self):
        """
        Draw method for main class
        """
        pyxel.cls(0)
        self.board.draw()


Main()
