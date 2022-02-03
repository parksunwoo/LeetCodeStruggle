import collections
from dataclasses import replace
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set

class Solution:
    def dart(self, dartResult:str) -> int:
        nums = [0]
        
        for s in dartResult:
            if s == 'S':
                nums[-1] **= 1
                nums.append(0)
            elif s == 'D':
                nums[-1] **= 2
                nums.append(0)
            elif s == 'T':
                nums[-1] **= 3
                nums.append(0)
            elif s == '*':
                nums[-2] *= 2
                if len(nums) >= 2:
                    nums[-3] *= 2                    
            elif s == '#':
                nums[-2] *= -1
            else:
                nums[-1] = nums[-1]*10 + int(s)
        
        return sum(nums)
            
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    # result = "1S2D*3T"
    result = "1D2S3T*"
    sol = Solution()
    print(sol.dart(result))
