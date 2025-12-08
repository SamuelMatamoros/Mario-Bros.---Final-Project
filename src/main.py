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
        pyxel.images[2].load(0, 128, "../assets/start_alt.png")
        self.board = Board()

        pyxel.run(self.update, self.draw)

    def update(self):
        """
        Update method for main class
        """
        # This line stops the game from executing while the menu is active
        # if not self.board.menu_active and not self.board.game_over:
        if not self.board.exec_halt:
            self.board.update()

        self.board.menu_update()

        if self.board.game_start:
            self.board.game_start_update()

        if self.board.game_over:
            self.board.game_over_update()

    def draw(self):
        """
        Draw method for main class
        """
        pyxel.cls(0)

        self.board.draw()

        # This line draws the board while is active
        if self.board.game_start:
            self.board.game_start_draw()

        if self.board.menu_active:
            self.board.menu_draw()

        if self.board.game_over:
            self.board.game_over_draw()


# Executes the main class
Main()
