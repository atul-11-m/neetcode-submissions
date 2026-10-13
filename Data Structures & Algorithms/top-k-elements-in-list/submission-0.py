class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = [[] for i in range(len(nums)+1)]

        for n in nums:
            map[n] = 1 + map.get(n, 0)
        for n, c in map.items():
            res[c].append(n)
        
        output = []

        for i in range(len(res)-1, 0, -1):
            for n in res[i]:
                output.append(n)
                if len(output) == k:
                    return output
