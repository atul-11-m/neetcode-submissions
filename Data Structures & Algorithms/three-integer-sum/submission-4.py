class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputs = []
        if len(nums) == 0:
            return []
        a = 0
        while a < len(nums):

            if nums[a] > 0:
                break

            if nums[a] == nums[a-1] and a > 0:
                a += 1
                continue

            b, c = a + 1, len(nums) - 1

            while b < c:
                total = nums[a] + nums[b] + nums[c]

                if total == 0:
                    outputs.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while nums[b] == nums[b-1] and b < c:
                        b += 1
                elif total > 0:
                    c -= 1
                else:
                    b += 1
            a += 1
        
        return outputs

                
            

            
        