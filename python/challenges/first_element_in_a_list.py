def first_element(numbers):
    return numbers[0]


tests = ((1, 2, 3), (80, 5, 100), (-500, 0, 50))
for numbers in tests:
    print(f"the first number in the list is: {first_element(numbers)}")
