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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
                
            cur.next, head.next, head = head, cur.next, head.next
            
            if head and cur.val > head.val:
                cur = parent
                
        return parent.next
        
        
        
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print(sol.merge(intervals))

    
    