# Definition for singly-linked list.
from typing import Collection, Optional
from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        print('1'*80)
        print(sorted(set(s)))
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            print('2'*80)
            print(char)
            print(s.index(char))
            print(s[s.index(char):])
            if set(s) == set(suffix):
                print('3'*80)
                print(set(s))
                print(set(suffix))
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''



                
if __name__ == '__main__':
    # begin
    sol = Solution()
    s = "bcabc"
    # s = "cbacdcbc"
    print (sol.removeDuplicateLetters(s))
    