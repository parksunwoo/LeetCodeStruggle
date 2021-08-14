# Definition for singly-linked list.
from typing import Collection, Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
            
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
                    
        odd.next = even_head
     
        return head
            
if __name__ == '__main__':
    # begin
    s = Solution()
    head = [1,2,3,4,5]  
    print (s.oddEvenList(head))
    #[1,3,5,2,4]
    
    
    


    
    
    
    