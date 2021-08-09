import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [c.isalnum for c in s.lower()]
        
        is_palindrom = True
        if char_list.pop(0) != char_list.pop():
            is_palindrom = False
            
        return is_palindrom
    

answer = Solution.isPalindrome(self, s="A man, a plan, a canal: Panama")
print(answer)
