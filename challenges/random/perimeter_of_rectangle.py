def perimeter_of_rectangle(length, width):
    return 2 * (length + width)


tests = ((6, 7), (20, 10), (2, 9))
for length, width in tests:
    print(
        f"The perimeter of a rectangle with {length} length and {width} width is: {perimeter_of_rectangle(length, width)}"
    )
