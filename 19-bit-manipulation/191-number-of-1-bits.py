import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def hammingWeight(self, n: int) -> int:
        #sol 1.
        # return bin(n).count('1')

        #sol 2.
        count = 
        while n:
            n &= n-1
            count += 1
        
        return count

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    n = 00000000000000000000000000001011
    sol = Solution()
    print(sol.hammingWeight(n))
    