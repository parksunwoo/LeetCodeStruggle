import collections
from turtle import left, right
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        if input.isdigit():
            return [int(input)]
    
        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index+1:])
                results.extend(compute(left, right, value))
        return results



# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    expression = "2*3-4*5"
    sol = Solution()
    print(sol.diffWaysToCompute(expression))
