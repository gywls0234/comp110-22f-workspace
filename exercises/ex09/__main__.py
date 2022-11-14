"""This specially named module makes the package runnable."""

from exercises.ex09 import constants
from exercises.ex09.model import Model
from exercises.ex09.view_controller import ViewController


def main() -> None:
<<<<<<< HEAD
    """Entrypoint of stimulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED, constants.CELL_INFECTED)
=======
    """Entrypoint of simulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED)
>>>>>>> 43442d78c273b343364e609fc640fdee64105e18
    view_controller: ViewController = ViewController(model)
    view_controller.start_simulation()


if __name__ == "__main__":
    main()