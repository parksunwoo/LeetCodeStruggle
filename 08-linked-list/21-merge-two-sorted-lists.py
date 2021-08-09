# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
        

                          
if __name__ == '__main__':
    # begin
    s = Solution()
    l1 = [1,2,4]
    l2 = [1,3,4]
    print (s.mergeTwoLists(l1, l2))
