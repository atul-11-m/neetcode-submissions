class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxCount = 0
        for n in nums:
            if n - 1 in seen:
                continue
            counter = 1
            while n+1 in seen:
                counter += 1
                n += 1
            maxCount = max(maxCount, counter)

        return maxCount

        # instead use shortcut to create nums into set
        # nums2 = set(nums)
        # use maxStreak = max(curStreak, maxStreak)