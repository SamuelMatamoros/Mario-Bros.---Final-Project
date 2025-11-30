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
                   title="Mario Bros.",
                   fps=60,
                   quit_key=pyxel.KEY_Q,
                   capture_scale=3,
                   capture_sec=0)
        pyxel.load("../assets/assets.pyxres")
        pyxel.images[2].load(0, 0, "../assets/game_over.png")
        self.board = Board()

        pyxel.run(self.update, self.draw)

    def update(self):
        """
        Update method for main class
        """
        self.board.menu_update()

        # This line stops the game from executing while the menu is active
        if not self.board.menu_active and not self.board.game_over:
            self.board.update()

    def draw(self):
        """
        Draw method for main class
        """
        pyxel.cls(0)

        self.board.draw()

        # This line draws the board while is active
        if self.board.menu_active:
            self.board.menu_draw()

        if self.board.game_over:
            pyxel.blt(64, 64, *config.GAME_OVER)


# Executes the main class
Main()
