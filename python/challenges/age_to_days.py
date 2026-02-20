def age_to_days(age):
    return age * 365


tests = (65, 0, 20)
for age in tests:
    print(f"The age of {age} in days is: {age_to_days(age)}")
