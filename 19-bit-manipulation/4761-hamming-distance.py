import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')


# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    x = 1
    y = 4
    sol = Solution()
    print(sol.hammingDistance(x, y))
    