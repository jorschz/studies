EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate how many minutes are left in the oven.

    Args:
        elapsed_bake_time: Minutes the dish has already been baking.

    Returns:
        Remaining baking time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the total preparation time.

    Each layer takes a fixed amount of time to prepare.

    Args:
        number_of_layers: Number of layers in the dish.

    Returns:
        Total preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total time spent so far.

    Includes both preparation time and baking time.

    Args:
        number_of_layers: Number of layers in the dish.
        elapsed_bake_time: Minutes the dish has already been baking.

    Returns:
        Total time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(f"Total elapsed time is: {elapsed_time_in_minutes(2, 4)} minutes to bake it")


# Name Assignment (Variables & Constants)
# Constants
# Functions
# Comments
# Docstrings
