import pyxel
import settings


class Board:
    """ Class for the game board """

    def __init__(self):
        """ Method that creates the board.
        :param width: The width of the board
        :param height: The height of the board
        """
        # self.width = settings.WIDTH
        self.width = settings.DEF_WIDTH
        self.height = settings.DEF_HEIGHT

        pyxel.init(self.width,
                   self.height,
                   title="Mario Bros.",
                   fps=60, quit_key=pyxel.KEY_Q)
        pyxel.load("../assets/assets.pyxres")
        pyxel.run(self.update, self.draw)

    # Properties and setters

    """
    Im not really shure this is what I want, i don't whant the dimensions to
    be changed at any moment of the program. I need them to be read-only.
    """

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        if not isinstance(width, int):
            raise TypeError("The width must be an integer",
                            str(type(width)),
                            "is provided")
        elif width < settings.MIN_WIDTH or width > settings.MAX_WIDTH:
            raise ValueError("The width must be in the range",
                             str(settings.MIN_WIDTH),
                             "and",
                             str(settings.MAX_WIDTH)
                             )
        else:
            self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        if not isinstance(height, int):
            raise TypeError("The height must be an integer",
                            str(type(height)),
                            "is provided")
        elif height < settings.MIN_HEIGHT or height > settings.MAX_HEIGHT:
            raise ValueError("The height must be in the range",
                             str(settings.MIN_HEIGHT),
                             "and",
                             str(settings.MAX_HEIGHT)
                             )
        else:
            self.__height = height

    @staticmethod
    def tests(self):
        # tests
        pyxel.text(16, 32, f"Height {self.height}", 7)
        pyxel.text(16, 48, f"{self.height - 2*settings.TILE_DIMENSION}", 7)
        pyxel.text(16, 64, f"Width {self.width}", 7)
        pyxel.text(16, 80, f"{self.width - 2*settings.TILE_DIMENSION}", 7)

        # visualizer for tiles
        # horizontal
        for i in range(self.width//settings.TILE_DIMENSION):
            pyxel.rect(settings.TILE_DIMENSION*i, 0, 16, 16, i)

    def update(self):
        """ This is a pyxel method that gets executed in every iteration of the
        game (every frame). You need to put here all the code that has to be
        executed in every frame. Now it contains only the logic to move the
        character if a key is pressed."""
        # To exit the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        """This is a pyxel method that gets executed in every iteration of the
        game (every frame). You need to put here all the code to draw the
        sprites of the game. """

        # Erasing the previous screen
        pyxel.cls(0)

        # self.tests(self)

        # This creates the pipe in the middle
        for i in range(self.height//settings.TILE_DIMENSION):
            pyxel.blt((self.width - settings.TILE_DIMENSION)//2,
                      settings.TILE_DIMENSION * i,
                      *settings.PIPE_BIG)

        # Drawing conveyors (must change latter)
        for i in range(2, self.height//settings.TILE_DIMENSION - 1):

            if i % 2 == 0:
                pyxel.blt(4*settings.TILE_DIMENSION,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_0)
                pyxel.blt(6*settings.TILE_DIMENSION,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_0)
                pyxel.blt(3*settings.TILE_DIMENSION,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_LEFT_0)
                pyxel.blt(7*settings.TILE_DIMENSION,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_RIGHT_0)
            else:
                pyxel.blt(3*settings.TILE_DIMENSION + 8,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_LEFT_0)
                pyxel.blt(4*settings.TILE_DIMENSION + 8,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_0_HALF)
                pyxel.blt(6*settings.TILE_DIMENSION,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_0_HALF)
                pyxel.blt(7*settings.TILE_DIMENSION - 8,
                          i * settings.TILE_DIMENSION,
                          *settings.CONVEYOR_RIGHT_0)

        pyxel.blt(10 * settings.TILE_DIMENSION - 8,
                  6 * settings.TILE_DIMENSION,
                  *settings.CONVEYOR_LEFT_0)
        pyxel.blt(10 * settings.TILE_DIMENSION + 8,
                  6 * settings.TILE_DIMENSION,
                  *settings.CONVEYOR_0_HALF)
        pyxel.blt(10 * settings.TILE_DIMENSION,
                  7 * settings.TILE_DIMENSION,
                  *settings.MACHINE)

        # Little Mario for reference
        pyxel.blt(3*self.width//4,
                  3*self.height//4,
                  *settings.MARIO_DEF_RIGHT)
