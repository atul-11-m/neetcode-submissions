class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if not nums:
            return 0
        curStreak = 1
        maxStreak = 1

        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                break
            if n == nums[i+1]:
                continue
            elif nums[i+1] == n+1:
                curStreak += 1
            else:
                curStreak = 1
            if curStreak >= maxStreak:
                maxStreak = curStreak
        
        return maxStreak
