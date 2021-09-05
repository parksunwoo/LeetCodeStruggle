# Definition for singly-linked list.
from typing import Collection, Optional, List
from collections import deque

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        
        return answer
    
if __name__ == '__main__':
    # begin
    sol = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print (sol.dailyTemperatures(temperatures))
    # [1,1,4,2,1,1,0,0]
    
    
    
    
    
    
    
    
    