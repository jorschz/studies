def digitize(n):
    return [int(d) for d in str(n)[::-1]]


assert digitize(35231) == [1, 3, 2, 5, 3]
assert digitize(0) == [0]
assert digitize(23582357) == [7, 5, 3, 2, 8, 5, 3, 2]
assert digitize(984764738) == [8, 3, 7, 4, 6, 7, 4, 8, 9]
print("All tests passed")
