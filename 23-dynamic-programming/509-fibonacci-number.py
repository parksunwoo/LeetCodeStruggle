import collections
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set
import numpy


class Solution:
    # dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        # sol 1.
        # if n <= 1:
        #     return n
        # else:
        #     return self.fib(n-1) + self.fib(n -2)
        
        # sol 2. memoization
        # if n <= 1:
        #     return n
        
        # if self.dp[n]:
        #     return self.dp[n]
        
        # self.dp[n] = self.fib(n-1) + self.fib(n-2)
        # return self.dp[n]
        
        # sol 3. tabulation
        # self.dp[1] = 1
        
        # for i in range(2, n+1):
        #     self.dp[i] = self.dp[i-1] + self.dp[i-2]
        # return self.dp[n]
        
        # sol 4.
        # x, y = 0, 1
        # for i in range(0, n):
        #     x, y = y, x+y
            
        # return x
        
        # sol 5.
        M = np.matri
        
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    n = 4
    sol = Solution()
    print(sol.fib(n))


