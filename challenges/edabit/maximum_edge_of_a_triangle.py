def mmax_third_side(side1, side2):
    return (side1 + side2) - 1


tests = ((8, 10), (5, 7), (9, 2))
for side1, side2 in tests:
    print(
        f"the maximum possible third side of a triangle with the sides {side1} and {side2} is: {mmax_third_side(side1, side2)}"
    )
