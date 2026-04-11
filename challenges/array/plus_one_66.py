class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        n = len(digits)
        for i, numbers in enumerate(digits):
            expoent = n - 1 - i
            integer += numbers * (10**expoent)
        result = integer + 1
        digits = [int(number) for number in str(result)]
        return digits
