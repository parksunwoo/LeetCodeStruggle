import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoList(self, l1:ListNode, l2:ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoList(l1.next, l2)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol 1.
        # if not (head and head.next):
        #     return head
        
        # half, slow, fast = None, head, head
        # while fast and fast.next:
        #     half, slow, fast = slow, slow.next, fast.next.next
        # half.next = None
        
        # l1 = self.sortList(head)
        # l2 = self.sortList(slow)
        
        # return self.mergeTwoList(l1, l2) 
        
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
            
        lst.sort()
        
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    head = [4,2,1,3]
    sol = Solution()
    print(sol.sortList(head))

    
    