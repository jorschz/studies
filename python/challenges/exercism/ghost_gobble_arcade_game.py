def eat_ghost(power_pellet_active, touching_ghost):
    """Check if the player eats a ghost.

    A ghost is eaten only when a power pellet is active
    and the player is touching a ghost.

    Args:
        power_pellet_active: Whether the power pellet effect is active.
        touching_ghost: Whether the player is touching a ghost.

    Returns:
        True if the ghost is eaten, otherwise False.
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Check if the player scores points.

    The player scores when touching a power pellet or a dot.

    Args:
        touching_power_pellet: Whether the player is touching a power pellet.
        touching_dot: Whether the player is touching a dot.

    Returns:
        True if the player scores, otherwise False.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Check if the player loses the game.

    The player loses when touching a ghost without
    an active power pellet.

    Args:
        power_pellet_active: Whether the power pellet effect is active.
        touching_ghost: Whether the player is touching a ghost.

    Returns:
        True if the player loses, otherwise False.
    """
    return touching_ghost and not power_pellet_active


def win(
    has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool
) -> bool:
    """Check if the player wins the game.

    The player wins when all dots are eaten and
    the player has not lost.

    Args:
        has_eaten_all_dots: Whether all dots were eaten.
        power_pellet_active: Whether the power pellet effect is active.
        touching_ghost: Whether the player is touching a ghost.

    Returns:
        True if the player wins, otherwise False.
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)


tests = [
    (eat_ghost, (False, True), False),
    (eat_ghost, (True, False), False),
    (eat_ghost, (True, True), True),
    (score, (False, False), False),
    (score, (False, True), True),
    (score, (True, False), True),
    (lose, (True, False), False),
    (lose, (True, True), False),
    (lose, (False, True), True),
    (win, (True, False, True), False),
    (win, (False, True, True), False),
    (win, (True, True, True), True),
    (win, (True, False, False), True),
]

# Testes organizados no formato (função, argumentos, resultado esperado sem desempacotamento no for)
for test in tests:
    func = test[0]
    args = test[1]
    expected = test[2]
    result = func(*args)
    assert result is expected, f"{func.__name__}{args} -> {result}, esperado {expected}"
print("Todos os testes passaram.")

# Bools
# Type Coercion and Truthiness
# How Booleans work under the hood
