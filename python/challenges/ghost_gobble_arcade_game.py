def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
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
