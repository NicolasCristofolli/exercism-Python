EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time in minutes.

    Parameters:
        elapsed_bake_time (int): Baking time already elapsed.

    Returns:
        int: Remaining time (in minutes) needed to bake the lasagna.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: Total preparation time in minutes (2 minutes per layer).
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time spent cooking (preparation + baking).

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.

    Returns:
        int: The total time elapsed (in minutes) preparing and baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time