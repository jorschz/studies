class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        consecutive = 0
        for i in nums:
            if i == 1:
                consecutive += 1
            else:
                consecutive = 0
            if consecutive >= result:
                result = consecutive
            # I could use: result = max(result, consecutive) in here
        return result


sol = Solution()
print(sol.findMaxConsecutiveOnes([1]))
