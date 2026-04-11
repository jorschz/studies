def total_legs(chickens, cows, pigs):
    return (chickens * 2) + (cows * 4) + (pigs * 4)


tests = ((2, 3, 5), (1, 2, 3), (5, 2, 8))
for chickens, cows, pigs in tests:
    print(
        f"with {chickens} chickens, {cows} cows and {pigs} pigs, there are {total_legs(chickens, cows, pigs)} legs"
    )
