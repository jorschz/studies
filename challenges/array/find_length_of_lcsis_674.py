class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        result = 1
        consecutive = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                consecutive += 1
            else:
                consecutive = 1
            if consecutive >= result:
                result = consecutive
        return result


sol = Solution()
print(sol.findLengthOfLCIS([1, 3, 5, 4, 7]))
print(sol.findLengthOfLCIS([5]))
