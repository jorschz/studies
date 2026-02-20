def increment(num):
    return num + 1


tests = (2, -9, 0, 999, 73)
for num in tests:
    print(f"The number after {num} is: {increment(num)}")
    