class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums2 = set(nums)        
        maxStreak = 0
        for item in nums2:
            if item - 1 in nums2:
                continue
            curStreak = 1
            while item + 1 in nums2:
                curStreak += 1
                item += 1
            maxStreak = max(curStreak, maxStreak)
        
        return maxStreak

        # instead use shortcut to create nums into set
        # nums2 = set(nums)
        # use maxStreak = max(curStreak, maxStreak)