# Solução 1
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        integer = 0
        n = len(digits)
        for i, numbers in enumerate(digits):
            expoent = n - 1 - i
            integer += numbers * (10**expoent)
        result = integer + 1
        digits = [int(number) for number in str(result)]
        return digits


# Solução 2
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
