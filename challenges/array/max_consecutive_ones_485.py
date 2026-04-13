class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        consecutive = 0
        for i in nums:
            if i == 1:
                consecutive += 1
            else:
                consecutive = 0
            result = max(result, consecutive)
        return result


sol = Solution()
print(sol.findMaxConsecutiveOnes([1]))
