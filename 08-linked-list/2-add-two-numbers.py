# Definition for singly-linked list.
from typing import Collection

from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # q: List = []
        q: Deque = deque()
        
        if not head:
            return True
        
        node= head
        while node is not None:
            q.append(node.val)
            node = node.next 
            
        while len(q) > 1:
            # if q.pop(0) != q.pop():
                # return False
            if q.popleft() != q.pop():
                return False
            
        return True
                    
        
                          
if __name__ == '__main__':
    # begin
    s = Solution()
    head = [1,2,2,1]
    print (s.isPalindrome(head))
    
    
    
    


    
    
    
    