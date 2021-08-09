# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next =node.next, prev
            return reverse(next, node)
                    
            
                          
if __name__ == '__main__':
    # begin
    s = Solution()
    head = [1,2,3,4,5]
    print (s.reverseList(head))
    # Output: [5,4,3,2,1]
