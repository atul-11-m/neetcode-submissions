class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2 = set()
        if not nums:
            return 0
        for n in nums:
            nums2.add(n)
        maxStreak = 0
        for item in nums2:
            if item - 1 in nums2:
                continue
            curStreak = 1
            while item + 1 in nums2:
                curStreak += 1
                item += 1
            if curStreak > maxStreak:
                maxStreak = curStreak
        
        return maxStreak