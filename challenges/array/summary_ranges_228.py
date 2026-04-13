class solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        nums = sorted(set(nums))
        start = nums[0]
        result = []
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                if start == nums[i]:
                    result.append(str(nums[i]))
                else:
                    result.append(f"{start}->{nums[i]}")
                start = nums[i + 1]
        if start == nums[-1]:
            result.append(str(nums[-1]))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result


sol = solution()
print(sol.summaryRanges([0, 2, 3, 4]))
print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))
print(sol.summaryRanges([0]))
print(sol.summaryRanges([]))

print(sol.summaryRanges([0, 1, 1, 2]))
