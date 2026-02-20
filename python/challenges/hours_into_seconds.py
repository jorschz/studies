def hours_to_seconds(hours):
    return hours * (60**2)


tests = (2, 10, 24, 36)
for hours in tests:
    print(f"{hours} in seconds is: {hours_to_seconds(hours)}")
