# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return 
        nod=head
        while nod:
            if nod.next is not None and nod.val==nod.next.val:
                nod.next=nod.next.next
            else: 
                nod=nod.next
            

        return head
        