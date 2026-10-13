class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxA = 0
        while left < right:
            curA = min(heights[left], heights[right]) * (right - left)
            if curA > maxA:
                maxA = curA
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxA

        # initialize left, right in one line