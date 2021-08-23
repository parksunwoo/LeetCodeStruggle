# Definition for singly-linked list.
from typing import Collection, Optional
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        for char in s:
            print('1'*80)
            print(char)
            if char not in table:
                print('2'*80)
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                print('3'*80)
                print(table[char])
                return False
        return len(stack) == 0
                        
if __name__ == '__main__':
    # begin
    sol = Solution()
    s = "()[]{}"
    print (sol.isValid(s))
    