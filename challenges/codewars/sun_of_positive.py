def positive_sum(arr):
    total = 0
    for i in arr:
        if i >= 0:
            total = total + i
    return total

assert positive_sum([1,2,3,4,5]) == 15
assert positive_sum([1,-2,3,4,5]) == 13
assert positive_sum([-1,2,3,4,-5]) == 9

assert positive_sum([]) == 0

assert positive_sum([-1,-2,-3,-4,-5]) == 0
print("All tests passed")

# Can be done as: sum(i for i in arr if i > 0)

