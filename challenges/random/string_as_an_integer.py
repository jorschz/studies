def string_to_int(txt):
    return int(txt)


tests = ("6", "1000", "12")
for txt in tests:
    print(f"the value {string_to_int(txt)} is a {type(string_to_int(txt))}")
