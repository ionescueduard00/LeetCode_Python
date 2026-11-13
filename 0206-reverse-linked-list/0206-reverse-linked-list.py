# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return
        stiva=[]
        stiva=list()
        dummy=ListNode()
        tail=dummy
        while head:
            stiva.append(head)
            head=head.next
        while stiva:
            tail.next=stiva.pop()
            tail=tail.next
        tail.next=None
        return dummy.next
        