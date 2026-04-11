"""Reactor control system module"""


def is_criticality_balanced(temperature: int, neutrons_emitted: int) -> bool:
    """Check if the reactor is balanced in criticality.

    args:
        - temperature: the temperature of the reactor in kelvin
        - neutrons_emitted: the number of neutrons in the reactor per second

    return: True if conditions are met,  False if not
    """
    return (
        temperature < 800
        and neutrons_emitted > 500
        and (temperature * neutrons_emitted) < 500000
    )


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
    if efficiency >= 60:
        return "orange"
    if efficiency >= 30:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Fail-safe mechanism to avoid overload and meltdown

    args:
        - temperature: measured in kelvin
        - neutrons_produced_per_second:
        - threshold:

    """
    power = temperature * neutrons_produced_per_second
    if power < threshold * 0.9:
        return "LOW"
    if 0.9 * threshold <= power <= 1.1 * threshold:
        return "NORMAL"
    return "DANGER"


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

fail_safe_tests = [
    (399, "LOW"),
    (300, "LOW"),
    (1, "LOW"),
    (0, "LOW"),
    (901, "NORMAL"),
    (1000, "NORMAL"),
    (1099, "NORMAL"),
    (899, "LOW"),
    (700, "LOW"),
    (400, "LOW"),
    (1101, "DANGER"),
    (1200, "DANGER"),
]
temperature = 10
threshold = 10000
for neutrons_produced_per_second, expected in fail_safe_tests:
    result = fail_safe(temperature, neutrons_produced_per_second, threshold)
    assert result == expected, (
        f"fail_safe({temperature}, {neutrons_produced_per_second}, {threshold})"
        f" -> {result} esperado {expected}"
    )

print("Todos os testes passaram.")

# Conditionals
