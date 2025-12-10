# IMPORTS #
# import time
import random
import pyxel
import config
from characters import Character
from conveyors import Conveyor
from package import Package
from truck import Truck


class Board:
    """
    Class for the game board.

    This class holds the unification of all of the other classes in order to
    provide a well structured game logic and gameplay.
    """

    def __init__(self):
        """
        Method that creates the board.
        """

        # Starting Attributes
        self.game_start = True

        self.difficulty = 0
        self.high_score = 0

        self.game_restart()

    # **************************************** #
    # **** PROPERTIES AND SETTERS SECTION **** #
    # **************************************** #

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

    @property
    def game_over(self):
        """The game_over property"""
        return self.__game_over

    @game_over.setter
    def game_over(self, game_over):
        if not isinstance(game_over, bool):
            raise TypeError("game_over must be a bool")
        else:
            self.__game_over = game_over

    @property
    def game_start(self):
        """The game_start property"""
        return self.__game_start

    @game_start.setter
    def game_start(self, game_start):
        if not isinstance(game_start, bool):
            raise TypeError("game_start must be a bool")
        else:
            self.__game_start = game_start

    # ****************************** #
    # ****** METHODS SECTION ******* #
    # ****************************** #

    # MENU SECTION #

    def menu_update(self):
        """
        Update method for the menu.

        Here lays the logic of how the menu behaves, the level selection,
        confirming and navigation.
        """
        if pyxel.btnp(pyxel.KEY_M):
            if self.menu_active:
                self.menu_active = False
                self.exec_halt = False
            else:
                self.menu_active = True
                self.exec_halt = True
        if self.menu_active:
            if pyxel.btnp(pyxel.KEY_UP) and self.__menu_selected > 0:
                self.__menu_selected -= 1
                if self.__soundtrack:
                    pyxel.play(3, 21)
            if pyxel.btnp(pyxel.KEY_DOWN) and self.__menu_selected < 4:
                self.__menu_selected += 1
                if self.__soundtrack:
                    pyxel.play(3, 21)
            if pyxel.btnp(pyxel.KEY_RETURN):
                if 0 <= self.__menu_selected <= 3:
                    self.difficulty = self.__menu_selected
                    # The line below resets the position of the menu after
                    # confirming the difficulty
                    # self.__menu_selected = 0
                    self.menu_active = False
                    self.exec_halt = False
                    if self.__soundtrack:
                        pyxel.play(3, 18)
                if self.__menu_selected == 4:
                    if self.__soundtrack:
                        self.__soundtrack = False
                    else:
                        self.__soundtrack = True

    def menu_draw(self):
        """
        Draw method for the menu.

        How the menu is drawn to the board when called upon.
        """
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

        if self.__menu_selected == 4:
            pyxel.text(config.WIDTH//2 - 24,
                       config.HEIGHT//3 + 64,
                       f"SOUND: {str(self.__soundtrack).upper()}",
                       11)
        else:
            pyxel.text(config.WIDTH//2 - 24,
                       config.HEIGHT//3 + 64,
                       f"SOUND: {str(self.__soundtrack).upper()}",
                       3)

    def top_menu(self):
        """
        Top Menu method.

        This handles the logic for the counters that will be visible during
        the gameplay that contain the score and fail counter and other buttons.
        """

        text_y = 9
        text_col = 7

        pyxel.rect(8, 8, 17, 7, 11)
        pyxel.text(9, text_y, "EXIT", text_col)

        pyxel.rect(config.WIDTH - 1.5*config.TILE_DIMENSION,
                   8, 17, 7, 9)
        pyxel.text(config.WIDTH - 1.5*config.TILE_DIMENSION + 1,
                   text_y, "MENU", text_col)

        pyxel.text(2*config.TILE_DIMENSION + 4,
                   text_y, f"SCORE: {self.score}", text_col)

        pyxel.text(4.5*config.TILE_DIMENSION + 4,
                   text_y, f"FAILS: {self.fails}", text_col)

        pyxel.text(8.5*config.TILE_DIMENSION + 4,
                   text_y, f"HIGH: {self.high_score}", text_col)

        if self.difficulty == 0:
            diff = "EASY"
        elif self.difficulty == 1:
            diff = "MEDIUM"
        elif self.difficulty == 2:
            diff = "HARD"
        else:
            diff = "EXTREME"
        pyxel.text(11*config.TILE_DIMENSION - 2,
                   text_y, f"LEVEL: {diff}", text_col)

    # DIFFICULTY SECTION #

    @staticmethod
    def __check_difficulty(self):
        """
        Difficulty checker method.

        This method checks wheter the level has changed, errases the previous
        variables and executes the new difficulty method.
        """

        if self.difficulty != self.__previous_difficulty:
            """
            This resets the variables to start clean the new difficulty.
            """
            self.mario.level = 0
            self.luigi.level = 0
            self.conveyors = []
            self.packages = []
            self.truck.number_of_packages = 0
            self.__previous_difficulty = self.difficulty
            self.score = 0
            self.fails = 0

            if self.difficulty == 0:
                self.difficulty0()
            elif self.difficulty == 1:
                self.difficulty1()
            elif self.difficulty == 2:
                self.difficulty2()
            elif self.difficulty == 3:
                self.difficulty3()

    def difficulty0(self):
        self.__number_of_conveyors = 5 + 1  # The one represents the conveyor 0
        self.__conveyor_speed = 1
        self.conveyors = [
                Conveyor(i, 1) for i in range(self.__number_of_conveyors)
                ]

        self.packages = []
        self.number_of_packages = 1
        self.__points_for_package = 50
        self.__number_of_deliveries = 0
        self.__eliminates_fails = True
        self.__deliveries_to_delete_fail = 3

        for i in range(self.number_of_packages):
            self.packages.append(Package("CONVEYOR"))

    def difficulty1(self):
        self.__number_of_conveyors = 7 + 1  # The one represents the conveyor 0
        for i in range(self.__number_of_conveyors):
            if i == 0:
                self.__conveyor_speed = 1
            elif i % 2 == 0:
                self.__conveyor_speed = 1
            else:
                self.__conveyor_speed = 1.5

            self.conveyors.append(Conveyor(i, self.__conveyor_speed))

        self.packages = []
        self.number_of_packages = 1
        self.__points_for_package = 30
        self.__number_of_deliveries = 0
        self.__eliminates_fails = True
        self.__deliveries_to_delete_fail = 5

        for i in range(self.number_of_packages):
            self.packages.append(Package("CONVEYOR"))

    def difficulty2(self):
        self.__number_of_conveyors = 9 + 1  # The one represents the conveyor 0
        for i in range(self.__number_of_conveyors):
            if i == 0:
                self.__conveyor_speed = 1
            elif i % 2 == 0:
                self.__conveyor_speed = 1.5
            else:
                self.__conveyor_speed = 2

            self.conveyors.append(Conveyor(i, self.__conveyor_speed))

        self.packages = []
        self.number_of_packages = 1
        self.__points_for_package = 30
        self.__number_of_deliveries = 0
        self.__eliminates_fails = True
        self.__deliveries_to_delete_fail = 5

        for i in range(self.number_of_packages):
            self.packages.append(Package("CONVEYOR"))

    def difficulty3(self):
        self.__number_of_conveyors = 5 + 1  # The one represents the conveyor 0
        for i in range(self.__number_of_conveyors):
            if i == 0:
                self.__conveyor_speed = 1
            else:
                self.__conveyor_speed = 1 + random.randint(1, 3)//2

            self.conveyors.append(Conveyor(i, self.__conveyor_speed))

        self.packages = []

        self.number_of_packages = 1
        self.__points_for_package = 20
        self.__number_of_deliveries = 0
        self.__eliminates_fails = False
        self.__deliveries_to_delete_fail = 0

    # DRAWINGS SECTION #

    @staticmethod
    def tests(self,
              dim=False,
              level=False,
              difficulty=False,
              tiles=False):
        """
        Test method for displaying useful information for debugging.
        """
        if dim:
            pyxel.text(32, 16, f"Width: {config.WIDTH}", 7)
            pyxel.text(32, 32, f"Height: {config.HEIGHT}", 7)

        if level:
            pyxel.text(196, 32, f"Mario level: {self.mario.level * 2}", 7)
            pyxel.text(196, 48, f"Luigi level: {self.luigi.level * 2 + 1}", 7)

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
        for i in range(config.TILES_OF_HEIGHT):
            pyxel.blt(config.WIDTH//2 - 8,  # puts the pipe in the middle
                      config.TILE_DIMENSION * i,
                      *config.PIPE_BIG)

    @staticmethod
    def draw_machine():
        pyxel.blt(config.WIDTH - 2*config.TILE_DIMENSION,
                  config.HEIGHT - 2*config.TILE_DIMENSION,
                  *config.MACHINE)

    @staticmethod
    def draw_doors():
        pyxel.blt(config.WIDTH - 1*config.TILE_DIMENSION,
                  config.HEIGHT - 3*config.TILE_DIMENSION,
                  *config.DOOR)
        for i in range(4):
            pyxel.blt(i*config.TILE_DIMENSION//2,
                      config.HEIGHT - config.TILE_DIMENSION,
                      *config.HOR_HALF_PIPE)
        pyxel.blt(0, config.HEIGHT - 1*config.TILE_DIMENSION - 4,
                  *config.DOOR_INVERTED)

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

    # UPDATE LOGIC SECTION #

    # Packages

    def __package_gen(self):
        """
        Method for package generation.
        """
        self.number_of_packages = 1 + self.score // self.__points_for_package

        if ((len(self.packages) < self.number_of_packages and
                pyxel.frame_count % 600 == 0) or
                (len(self.packages) == 0)):
            self.packages.append(Package("CONVEYOR"))
            if self.__soundtrack:
                pyxel.play(3, 18)

    def __package_update_all(self):
        """
        Method for package update.
        """
        for package in self.packages:

            """
            This sets the speed of the package to match the speed of the
            conveyor its located in.

                'self.conveyors' is the list of all conveyors in the level
                                 ordered by level
            Setting the speed is done exernaly because it affects the rate at
            which the package is updated.
            """
            package.speed = self.conveyors[package.level].speed
            package.update(self.__soundtrack)

            if package.at_the_end():
                if package.level == self.__number_of_conveyors - 1:
                    if package.level == self.luigi.level * 2 + 1:
                        self.luigi.has_package = True
                        self.truck.number_of_packages += 1
                        self.score += 1
                        package.state = "TRUCK"
                    else:
                        package.broken(self.__soundtrack)
                        self.fails += 1
                        if not self.boss.boss_active:
                            self.boss.boss_active = True
                            self.boss.boss_target = "LUIGI"
                            self.boss.boss_timer = 60

                elif package.level % 2 == 0:
                    if package.level == self.mario.level * 2:
                        package.move_to_next_conveyor(self.__soundtrack)
                        self.score += 1
                        """
                        This is here in order to change the sprite, but we
                        need to make it so it is animated, not just a 1 frame
                        change
                        """
                        self.mario.has_package = True
                    else:
                        package.broken(self.__soundtrack)
                        self.fails += 1
                        if not self.boss.boss_active:
                            self.boss.boss_active = True
                            self.boss.boss_target = "MARIO"
                            self.boss.boss_timer = 60       # 1 sec at 60 fps

                else:
                    if package.level == self.luigi.level * 2 + 1:
                        package.move_to_next_conveyor(self.__soundtrack)
                        self.score += 1
                        self.luigi.has_package = True
                    else:
                        package.broken(self.__soundtrack)
                        self.fails += 1
                        if not self.boss.boss_active:
                            self.boss.boss_active = True
                            self.boss.boss_target = "LUIGI"
                            self.boss.boss_timer = 60
            else:
                """
                This is in order to reestablish the default sprite.
                """
                self.mario.has_package = False
                self.luigi.has_package = False

            if package.state == "BROKEN" or package.state == "TRUCK":
                self.packages.remove(package)

    def __truck_delivery(self):
        """
        Here we put the logic for when the truck is full:
          resting characters, more points, ...
        """
        self.score += 10
        self.__number_of_deliveries += 1
        self.truck.number_of_packages = 0

        # Start delivery (this sets state = "DELIVERY" and stores frame)
        self.truck.start_delivery()

        # Characters rest (later use this for rest animation)
        self.mario.has_package = False
        self.luigi.has_package = False

        # Characters rest
        self.mario.resting = True
        self.luigi.resting = True
        self.mario.has_package = False
        self.luigi.has_package = False

        # Remove packages at the last conveyor end
        to_remove = []
        for pkg in self.packages:
            # if pkg.level == last_level and pkg.at_the_end():
            if pkg.at_the_end():
                to_remove.append(pkg)
        for pkg in to_remove:
            self.packages.remove(pkg)

        # Eliminate fails if possible
        if (self.__eliminates_fails and self.__number_of_deliveries %
                self.__deliveries_to_delete_fail == 0 and
                self.__number_of_deliveries != 0 and
                self.fails > 0):
            self.fails -= 1

    def __boss_reprimand(self):
        self.boss.boss_timer -= 1

        if self.boss.boss_target == "MARIO":
            self.mario.reprimand = True
            self.luigi.reprimand = False

        if self.boss.boss_target == "LUIGI":
            self.luigi.reprimand = True
            self.mario.reprimand = False

        if self.boss.boss_timer <= 0:
            self.boss.boss_active = False
            self.mario.reprimand = False
            self.luigi.reprimand = False
            self.boss.boss_timer = 0

    def game_restart(self):
        """
        Method for restarting the game.

        When invoked, the game logic will be restarted.
        Called when:
            - Game starts
            - Game Over
            - Player restart

        Only thing to keep out is high_score
        """
        self.__previous_difficulty = -1

        self.score = 0
        self.fails = 0

        self.menu_active = False
        self.__menu_selected = self.difficulty
        self.__soundtrack = True

        self.game_over = False

        self.exec_halt = False

        self.mario = Character("MARIO")
        self.luigi = Character("LUIGI")
        self.boss = Character("BOSS")
        self.truck = Truck()

    def game_start_update(self):
        self.exec_halt = True
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
            self.game_start = False
            self.menu_active = True
            self.game_restart()
            if self.__soundtrack:
                pyxel.play(3, 18)

    def game_start_draw(self):
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
        pyxel.blt(config.WIDTH/2 - 100,
                  config.HEIGHT/2 - 60,
                  *config.START_SCREEN)
        pyxel.text(config.WIDTH/2 - 12,
                   config.HEIGHT/2 + 48,
                   "<ENTER>", 3)

    def game_over_update(self):
        self.game_over = True
        self.exec_halt = True

        if pyxel.btnp(pyxel.KEY_RETURN):
            self.game_restart()
            if self.__soundtrack:
                pyxel.play(3, 18)

    def game_over_draw(self):
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
        pyxel.blt(config.WIDTH/2 - 96,
                  config.HEIGHT/2 - 64,
                  *config.GAME_OVER)
        pyxel.text(config.WIDTH/2 - 12,
                   config.HEIGHT/2 + 48,
                   "<ENTER>", 3)

    def __manage_score(self):
        """
        Method for managing score updates and deliveries.
        """
        if self.high_score < self.score:
            self.high_score = self.score

    # UPDATE and DRAW methods #

    def update(self):

        # 1) Difficulty setup
        self.__check_difficulty(self)

        # 2) Special events

        # Truck delivering
        if self.truck.delivering:
            if self.truck.delivery_done():
                self.truck.finish_delivery()
                self.mario.resting = False
                self.luigi.resting = False
                self.boss.boss_active = True
                self.boss.boss_target = "BOTH"
                self.boss.boss_timer = 60

        # Boss reprimand
        if self.boss.boss_active:
            self.__boss_reprimand()

        # 3) Normal game update when not special events
        if not self.exec_halt:
            self.mario.update(self.__number_of_conveyors, self.__soundtrack)
            self.luigi.update(self.__number_of_conveyors, self.__soundtrack)

            if not self.game_start:
                if not self.truck.delivering:
                    self.__package_gen()
                self.__package_update_all()

            self.__manage_score()

            if self.truck.number_of_packages % 8 == 0 and (
                    not self.truck.number_of_packages == 0):
                self.__truck_delivery()

            if self.fails == 3:
                self.game_over = True
                self.exec_halt = True

    def draw(self):

        self.tests(self, tiles=False, level=True)

        for conveyor in self.conveyors:
            conveyor.draw(self.exec_halt)

        for package in self.packages:
            package.draw()

        self.draw_platforms(self.__number_of_conveyors)

        self.truck.draw(self.__number_of_conveyors)

        self.mario.draw(self.__number_of_conveyors)
        self.luigi.draw(self.__number_of_conveyors)

        self.draw_pipe()
        self.draw_machine()
        self.draw_doors()

        self.top_menu()

        if self.boss.boss_active:
            self.boss.draw(self.__number_of_conveyors)
