import collections
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set

class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
    
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    n = 3
    sol = Solution()
    print(sol.climbStairs(n))
