# Final Project - M2.350.16480-96 MAG. Programming 25/26-S1

This repository houses the final project's source code made by [Samuel Matamoros](https://github.com/SamuelMatamoros) and [Darío Castro](https://github.com/castrovilaug). The projects consist on recreating the game: [Mario Bros.](https://itizso.itch.io/nintendo-mario-bros). Further instructions can be found [here](/instructions/instructions.pdf).

## Basic information

The game is writen in [`Python`](python.org), using the graphics library [`Pyxel`](https://github.com/kitao/pyxel). 

> [!NOTE]
> The project includes a `venv` (virtual environment) with Python3.12. The choice to run this specific version is in order for the Pyxel library to properly work on all platforms as with the release of Python3.13 several breaking changes made the library not work in `GNU/Linux` systems.

## Roadmap / Changelog

### First steps.

- [x] Stored project instructions under [`instructions/instructions.pdf`](/instructions/instructions.pdf)
- [x] [`.venv`](/.venv) created with Python3.12.12
- [x] Downloaded the `Pyxel` library (`pip install pyxel`)
- [ ] Downloaded/Created assets for the game
<!-- - [ ]  -->


### Sprint 1: Objects and graphical interface

- [ ] Create a class for each main game element: Characters, Conveyor, Truck, Package,
etc.
- [ ] All the behavior logic of each entity must be contained in its corresponding class.
Avoid including game logic in the main program (penalty if it occurs).
- [ ]  Design the graphical interface of the scenario: a single screen with the conveyor
belts, floors, stairs, and truck.
- [ ] Implement a score counter and error counter (failures) visible during the game.
- [ ] Define the basic data structures that will manage the state of the conveyor belts,
packages in transit, and the difficulty level.

### Sprint 2: Mario and Luigi Movement

- [ ] Implement the vertical movement control of the characters:
    - [ ] Mario: Arrow Up / Arrow Down keys.
    - [ ] Luigi: W / S keys.
- [ ] Each character must be able to go up and down floors using the stairs, respecting
the upper and lower limits.
- [ ] Graphically display the current position of each character (Floor0, Floor1, etc.) on
the screen.

### Sprint 3: Packages movement

- [ ] Implement the package flow on the conveyor belts according to the established rules:
    - [ ] Conveyor0 generates empty boxes for Mario.
    - [ ] Even Conveyors → controlled by Mario.
    - [ ] Odd Conveyors → controlled by Luigi.
- [ ] Graphical representation of the packages must change according to the belt they are
on.
- [ ] When a package reaches the end of a conveyor belt:
	- [ ] If the corresponding character is on the correct floor, they automatically pick
it up and pass it to the next conveyor belt.
	- [ ] If not, the package falls and a failure is recorded.
- [ ] Implement the automatic movement of packages based on the speed of the
current level.

### Sprint 4: Scoring system, failures, and end of game

- [ ] Implement scoring:
	- [ ] +1 point for each package correctly delivered to the next conveyor belt.
	- [ ] +10 points for each completed truck (8 packages delivered).
- [ ] Manage the failure counter (3 failures = game over).
- [ ] Implement the truck logic and character rest:
	- [ ] When it receives 8 packages, it goes out for delivery.
	- [ ] During delivery, the conveyor belts stop temporarily. If a package is at the last
position of the conveyor, it is deleted.
	- [ ] Upon return, activity resumes.
- [ ] Display a game over message or animation when 3 failures are exceeded.
- [ ] Complete Boss’s visual effects: he will appear when a package falls, after rest…

### Sprint 5: Difficulty levels and final adjustments (optional)

- [ ] Incorporate the difficulty levels (Easy, Medium, Extreme, Crazy) according to the
rule table:
	- [ ] Conveyor belt speed.
	- [ ] Minimum number of packages in play.
	- [ ] Failure elimination rules for truck delivery.
- [ ] Adjust the interface to display the current level.
- [ ] Allow changing the level from the menu or before starting the game.
- [ ] Add optional sound effects: conveyor belt movement, error sounds, etc.
- [ ] Implement high score tables or local competitive mode

## Sources and relevant links

 - python.org
 - https://github.com/kitao/pyxel
 
