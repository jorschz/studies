def area_of_a_triangle(base, height):
    return 0.5 * base * height


tests = ((3, 2), (5, 4), (10, 10), (0, 60), (12, 11))
for base, height in tests:
    print(
        f"The area of a triangle with base {base} and height {height} is: {int(area_of_a_triangle(base, height))}"
    )
