# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        if head.next is None:
            return head

        curr = head.next
        prev = head
        prev.next = None

        while curr.next != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr

            print(curr.next.val)
            curr = nextNode
        
        curr.next = prev
        prev = curr
        
        return curr
            

           

        

        