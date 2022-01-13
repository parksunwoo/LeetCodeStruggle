import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        
        # for i in range(len(prices)-1):
        #     if prices[i+1] > prices[i]:
        #         result += prices[i+1] - prices[i]
        # return result
    
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
    
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    sol = Solution()
    print(sol.maxProfit(prices))
    
    
    