class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_Profit = 0
        left_ptr = 0
        if len(prices) == 1:
            return 0
        right_ptr = 1

        while right_ptr < len(prices):
            profit = prices[right_ptr] - prices[left_ptr]
            if profit > max_Profit:
                max_Profit = profit
            elif profit < 0:
                left_ptr = right_ptr
            right_ptr += 1
        return max_Profit
            

        

        