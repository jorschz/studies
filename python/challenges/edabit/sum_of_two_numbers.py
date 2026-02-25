def add(a, b):
    return a + b


tests = [(2, 3), (-3, -6), (7, 3)]
for a, b in tests:
    print(f"{a} + {b} = {add(a, b)}")
