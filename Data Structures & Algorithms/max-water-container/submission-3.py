class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0
        while l < r:
            smaller = min(heights[l], heights[r])
            area = smaller * (r-l)
            maximum = max(maximum, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maximum
        # initialize left, right in one line