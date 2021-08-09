from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price  = sys.maxsize
        
        for p in prices:
            min_price = min(p, min_price)                          
            profit = max(profit, p-min_price)
        
        return profit
                          
if __name__ == '__main__':
    # begin
    s = Solution()
    prices = [7,1,5,3,6,4]
    print (s.maxProfit(prices))