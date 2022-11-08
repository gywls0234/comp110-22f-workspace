"""This specially named module makes the package runnable."""

from exercises.ex09 import constants
from exercises.ex09.model import Model
from excercises.ex09.view_controller import ViewController


def main() -> None:
    """Entrypoint of stimulation."""
    model: Model = Model(constants.CELL_Count, constants.CELL_SPEED, constants.infected)
    view_controller: ViewController = ViewController(model)
    view_controller.start_stimulation()


    if __name__ == "__main__":
        main()