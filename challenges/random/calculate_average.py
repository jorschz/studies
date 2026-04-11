def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


assert find_average([1, 2, 3]) == 2
assert find_average([]) == 0
assert find_average([1, 2]) == 1.5
print("All test passed")
