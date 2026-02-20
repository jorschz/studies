def remainder(x, y):
    return x % y


tests = ((7, 2), (3, 4), (5, 5), (1, 3))
for x, y in tests:
    print(f"the remainder of {x} and {y} is {remainder(x, y)}")
