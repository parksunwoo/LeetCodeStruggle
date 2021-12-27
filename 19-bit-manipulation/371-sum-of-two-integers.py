import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        #sol 1.
        # MASK = 0xFFFFFFFF
        # INT_MAX = 0xFFFFFFFF
        
        # a_bin = bin(a & MASK)[2:].zfill(32)
        # b_bin = bin(b & MASK)[2:].zfill(32)
        
        # result = []
        # carry = 0
        # sum = 0
        # for i in range(32):
        #     A = int(a_bin[31 - i])
        #     B = int(b_bin[31 - i])
            
        #     Q1 = A & B
        #     Q2 = A ^ B
        #     Q3 = Q2 & carry
        #     sum = carry ^ Q2
        #     carry = Q1 | Q3
            
        #     result.append(str(sum))
            
        # if carry == 1:
        #     result.append('1')
            
        
        # result = int(''.join(result[::-1]), 2 )& MASK
        # if result > INT_MAX:
        #     result = ~(result ^ MASK)
            
        # return result
    
        #sol 2.
        MASK = 0xFFFFFFFF
        INT_MAX = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    a = 1
    b = 2
    sol = Solution()
    print(sol.getSum(a, b))
    
    
    