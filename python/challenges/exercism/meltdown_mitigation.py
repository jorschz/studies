def is_criticality_balanced(temperature: int, neutrons_emitted: int) -> bool:
    """Check if the reactor is balanced in criticality.

    args:
        - temperature: the temperature of the reactor in kelvin
        - neutrons_emitted: the number of neutrons in the reactor per second

    return: True if conditions are met,  False if not
    """
    if (
        temperature < 800
        and neutrons_emitted > 500
        and (temperature * neutrons_emitted) < 500000
    ):
        return True
    else:
        return False


def reactor_efficiency(voltage: int, current: int, theorical_max_power: int) -> str:
    """Determine the efficiency of the reactor

    args:
        - voltage:
        - current
        - theorical_max_power:
    return:
        - green: efficiency of 80% or more,
        - orange: efficiency of less than 80% but at least 60%,
        - red: efficiency below 60%, but still 30% or more,
        - black: less than 30% efficient.

    """
    generated_power = voltage * current
    efficiency = float(generated_power / (theorical_max_power) * 100)
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


critical_tests = [
    ((750, 650), True),
    ((799, 501), True),
    ((500, 600), True),
    ((1000, 800), False),
    ((800, 500), False),
    ((800, 500.01), False),
    ((799.99, 500), False),
    ((500.01, 999.99), False),
    ((625, 800), False),
    ((625.99, 800), False),
    ((625.01, 799.99), False),
    ((799.99, 500.01), True),
    ((624.99, 799.99), True),
    ((500, 1000), False),
    ((500.01, 1000), False),
    ((499.99, 1000), True),
]
for args, expected in critical_tests:
    result = is_criticality_balanced(*args)
    assert (
        result == expected
    ), f"is_criticality_balanced{args} -> {result}, esperado {expected}"


efficiency_tests = [
    (1000, "green"),
    (999, "green"),
    (800, "green"),
    (799, "orange"),
    (700, "orange"),
    (600, "orange"),
    (599, "red"),
    (560, "red"),
    (400, "red"),
    (300, "red"),
    (299, "black"),
    (200, "black"),
    (0, "black"),
]

voltage = 10
theorical_max_power = 10000

for current, expected in efficiency_tests:
    result = reactor_efficiency(voltage, current, theorical_max_power)
    assert result == expected, (
        f"reactor_efficiency({voltage}, {current}, {theorical_max_power})"
        f"-> {result}, esperado {expected}"
    )

print("Todos os testes passaram.")

# Conditionals
