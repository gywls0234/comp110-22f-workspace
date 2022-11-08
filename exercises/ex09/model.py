"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi

"""Exercise 9."""

__author__ = "730617586"

class Point: 
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, t coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x,y)

    def distance(self, other: Point) -> float:
        from math import sqrt
        """Find distance between two points."""
        x: float = self.x - other.x
        y: float = self.y - other.y
        distance: float = sqrt((x)**2 + (y)**2)
        return distance

class Cell: 
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __int__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        
    def tick(self) -> None:
        self.location = self.location.add(self.direction)
        if Cell.is_infected():
            Cell.sickness += 1
        if Cell.sickness > constants.RECOVERY_PERIOD:
            Cell.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"

    def contract_disease(self) -> None:
       self.sickness = constants.INFECTED
       return None

    def is_vulnerable(self) -> bool:
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False

    def is_infected(self) -> bool:
        if self.sickness > constants.INFECTED:
            return True
        else: 
            return False

    def color(self) -> str:
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "black"

    def contact_with(self, other: Cell) -> None:
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(Cell):
        constants.IMMUNE == Cell.sickness

    def is_immune(Cell) -> bool:
        if Cell.sickness == constants.IMMUNE:
            return True

    def color(Cell) -> str:
        if Cell.is_immune():
            return "black"

    

class Model: 
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        immune: int = 0
        if infected >= cells or infected <= 0:
            raise ValueError("Infected cells cannot e greater than number of cells.")

        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected: 
                cell.contract_disease() 
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()  
            self.enforce_bounds(cell)

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

    def enforce_bounds(self, cellL: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if Cell.location.x > constants.MAX_X:
            Cell.location.x = constants.MAX_X
            Cell.direction.x += -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        if Cell.population == constants.VULNERABLE or constants.IMMUNE:
            return True
        if Cell == constants.INFECTED:
            return False 

    def check_contacts() -> None:
        Cell.location < constants.CELL_RADIUS
        Cell.contact_with()

    