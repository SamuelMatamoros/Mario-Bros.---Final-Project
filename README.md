# Final Project - M2.350.16480-96 MAG. Programming 25/26-S1

This repository houses the final project's source code made by [Samuel Matamoros](https://github.com/SamuelMatamoros) and [Darío Castro](https://github.com/castrovilaug). The projects consist on recreating the game: [Mario Bros.](https://itizso.itch.io/nintendo-mario-bros). Further instructions can be found [here](/instructions/instructions.pdf).

## Basic information

The game is writen in [`Python`](python.org), using the graphics library [`Pyxel`](https://github.com/kitao/pyxel). 

> [!NOTE]
> No `venv` is included in this repository in order to maximize compatibility. In order to create your own `venv` to run the game follow the instructions in the [Virtual Environment](#Virtual-environment) section.
<!-- > The project includes a `venv` (virtual environment) with Python3.12. The choice to run this specific version is in order for the Pyxel library to properly work on all platforms as with the release of Python3.13 several breaking changes made the library not work in `GNU/Linux` systems. -->

## Running and working with the code

In order to have an ideal environment in which to develop the game, please read the following section carefully and comprise with the specified bellow.

### Python

Python version can be any version greater than Python3, preferably Python3.13 or greater. 

> [!WARNING]
> For linux users, `Python3.13` may not work as the inclusion of breaking changes to the release might have adversary behaviour with the `Pyxel` library. 
>
> `Python3.12` is recomended to linux users.

### Virtual Environment

In order to work in an isolated and controlled environment, the use of a [virtual environment]() (`venv` for short) is recomended. You can create one by executing the following command in the project directory:

```bash
python -m venv .venv
```

The final `.venv` is just the name the virtual environment directory will have, for maximal compatibility *do not* change it please.

### Requirements

The libraries that will be used in this project will be stored in the [requirements.txt](/requirements.txt) file and can be installed through the `pip` package manager with:

```bash
pip install -r requirements.txt
```

Please be sure to have the requirements installed before you run any of the code.

## Roadmap / Changelog

### First steps.

- [x] Stored project instructions under [`instructions/instructions.pdf`](/instructions/instructions.pdf)
- [x] Created the [`requirements.txt`](/requirements.txt) file
- [x] Downloaded/Created assets for the game


### Sprint 1: Objects and graphical interface

- [x] Create a class for each main game element: Characters, Conveyor, Truck, Package, etc.
- [x] All the behavior logic of each entity must be contained in its corresponding class. Avoid including game logic in the main program (penalty if it occurs).
- [x]  Design the graphical interface of the scenario: a single screen with the conveyor belts, floors, stairs, and truck.
- [x] Implement a score counter and error counter (failures) visible during the game.
- [x] Define the basic data structures that will manage the state of the conveyor belts, packages in transit, and the difficulty level.

### Sprint 2: Mario and Luigi Movement

- [x] Implement the vertical movement control of the characters:
    - [x] Mario: Arrow Up / Arrow Down keys.
    - [x] Luigi: W / S keys.
- [x] Each character must be able to go up and down floors using the stairs, respecting the upper and lower limits.
- [x] Graphically display the current position of each character (Floor0, Floor1, etc.) on the screen.

### Sprint 3: Packages movement

- [x] Implement the package flow on the conveyor belts according to the established rules:
    - [x] Conveyor0 generates empty boxes for Mario.
    - [x] Even Conveyors → controlled by Mario.
    - [x] Odd Conveyors → controlled by Luigi.
- [x] Graphical representation of the packages must change according to the belt they are on.
- [x] When a package reaches the end of a conveyor belt:
	- [x] If the corresponding character is on the correct floor, they automatically pick it up and pass it to the next conveyor belt.
	- [x] If not, the package falls and a failure is recorded.
    - [ ] \(_Extra:_\) change the sprite of Mario or Luigi.
- [x] Implement the automatic movement of packages based on the speed of the current level.

### Sprint 4: Scoring system, failures, and end of game

- [ ] Implement scoring:
	- [ ] +1 point for each package correctly delivered to the next conveyor belt.
	- [ ] +10 points for each completed truck (8 packages delivered).
- [ ] Manage the failure counter (3 failures = game over).
- [ ] Implement the truck logic and character rest:
	- [ ] When it receives 8 packages, it goes out for delivery.
	- [ ] During delivery, the conveyor belts stop temporarily. If a package is at the last position of the conveyor, it is deleted.
	- [ ] Upon return, activity resumes.
- [ ] Display a game over message or animation when 3 failures are exceeded.
- [ ] Complete Boss’s visual effects: he will appear when a package falls, after rest…

### Sprint 5: Difficulty levels and final adjustments (optional)

- [ ] Incorporate the difficulty levels (Easy, Medium, Extreme, Crazy) according to the rule table:
	- [ ] Conveyor belt speed.
	- [ ] Minimum number of packages in play.
	- [ ] Failure elimination rules for truck delivery.
- [ ] Adjust the interface to display the current level.
- [ ] Allow changing the level from the menu or before starting the game.
- [ ] Add optional sound effects: conveyor belt movement, error sounds, etc.
- [ ] Implement high score tables or local competitive mode

### Extra functionality (ultra optional)

- [x] Incorporate menu for changing difficulty.
- [ ] Incorporate welcoming screen/start menu (i.e.: a small drawing of the name of the game and animated text inviting to press ENTER to play).

## Sources and relevant links

- https://www.python.org/
- https://github.com/kitao/pyxel 
- https://itizso.itch.io/nintendo-mario-bros for the inspiration
- https://github.com/guluc3m/report-template-typst for the report template
