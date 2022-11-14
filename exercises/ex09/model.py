"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
<<<<<<< HEAD
from math import sin, cos, pi, sqrt

"""Exercise 9."""

__author__ = "730617586"


class Point: 
=======
from math import sin, cos, pi


__author__ = ""  # TODO


class Point:
>>>>>>> 43442d78c273b343364e609fc640fdee64105e18
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
<<<<<<< HEAD
        """Construct a point with x, t coordinates."""
=======
        """Construct a point with x, y coordinates."""
>>>>>>> 43442d78c273b343364e609fc640fdee64105e18
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

<<<<<<< HEAD
    def distance(self, other: Point) -> float:
        """Find distance between two points."""
        x: float = self.x - other.x
        y: float = self.y - other.y
        distance: float = sqrt((x)**2 + (y)**2)
        return distance


class Cell: 
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE
=======

class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0
>>>>>>> 43442d78c273b343364e609fc640fdee64105e18

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
<<<<<<< HEAD
        
    def tick(self) -> None:
        """Tick."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()   

    def contract_disease(self) -> None:
        """contrsct_disease."""
        self.sickness = constants.INFECTED
        return None

    def is_vulnerable(self) -> bool:
        """is_vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False

    def is_infected(self) -> bool:
        """is_infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else: 
            return False

    def color(self) -> str:
        """Color."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "red"
        if self.is_immune():
            return "black"
        return "dummy string"    

    def contact_with(self, other: Cell) -> None:
        """contact_with."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self):
        """immunize."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """is_immune."""
        if self.sickness == constants.IMMUNE:
            return True


class Model: 
    """The state of the simulation."""
    location: Point
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0:
            raise ValueError("Infected cells cannot be greater than number of cells.")
        if immune >= cells or immune < 0:
            raise ValueError("Immune cells cannot be greater than number of cells.")    

        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected:
                cell.contract_disease() 
            self.population.append(cell)
            if i >= infected and i < infected + immune:
                cell.immunize()

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()  
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0

        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        # if self.population: int = constants.VULNERABLE or constants.IMMUNE
        # return True
        # if self: int > constants.INFECTED
        return False 

    def check_contacts(self) -> None:
        """Check_contacts."""
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1
=======

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float):
        """Initialize the cells with random locations and directions."""
        self.population = []
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1

    def random_location(self) -> Point:
        """Generate a random location."""
        # TODO
        return Point(0.0, 0.0)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        # TODO
        return Point(0.0, 0.0)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        ...

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False
>>>>>>> 43442d78c273b343364e609fc640fdee64105e18
