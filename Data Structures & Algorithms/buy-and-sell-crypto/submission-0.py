class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prev_index = 0
        next_index = 1
        max_profit = 0
        while next_index < len(prices):
            if prices[prev_index] > prices[next_index]:
                prev_index = next_index
            else:
                max_profit = max(prices[next_index]- prices[prev_index], max_profit)

            next_index += 1
        return max_profit

