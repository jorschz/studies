def power_calculator(voltage, current):
    return voltage * current


tests = ((110, 3), (230, 10), (480, 20))
for voltage, current in tests:
    print(
        f"the power of {voltage} voltage and {current} current is: {power_calculator(voltage, current)}"
    )
