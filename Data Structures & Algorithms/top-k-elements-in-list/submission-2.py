class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        seen = {}

        for n in nums:
            seen[n] = 1 + seen.get(n, 0)
        
        for n in seen:
            freq[seen[n]].append(n)

        output = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
            
        