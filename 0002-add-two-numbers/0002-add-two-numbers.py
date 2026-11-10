# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        rest=ListNode()
        dummy=ListNode()
        tail=dummy
        k=0
        while l1 and l2:
                l1.val=l1.val+l2.val+k
                if l1.val>9:
                    l1.val=l1.val%10
                    k=1
                else:
                    k=0
                tail.next=l1
                l1=l1.next
                l2=l2.next
                tail=tail.next
        
        rest = l1 if l1 else l2
        
        if k==0:
            tail.next=rest
           
               
        
        
        while rest and k==1:
            if rest.val+k<=9:
                rest.val+=1
                tail.next=rest
                return dummy.next   
            rest.val=0
            tail.next=rest
            rest=rest.next
            tail=tail.next
        if rest is None and k==1:
            tail.next = ListNode(1)
            tail=tail.next
            tail.val=1  
        return dummy.next
            
                
                
        




            
        