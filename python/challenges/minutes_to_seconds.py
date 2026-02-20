def minutes_to_seconds(minutes):
    return minutes * 60


tests = (6, 4, 8, 60)
for minutes in tests:
    print(f"{minutes} minutes in seconds is: {minutes_to_seconds(minutes)}")
