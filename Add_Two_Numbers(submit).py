# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy 

        front_digit = 0

        while l1 is not None or l2 is not None :
            a = l1.val if l1 is not None else 0 
            b = l2.val if l2 is not None else 0 

            amount = a + b + front_digit 
            reserve_values = str(amount)

            if len(reserve_values) >= 2 :
                front_digit = int(reserve_values[0])
                rear_digit = int(reserve_values[1])
                current.next = ListNode(int(rear_digit))
            else :
                front_digit = 0
                current.next = ListNode(int(reserve_values))
            
            current = current.next
            if l1 is not None: 
                l1 = l1.next
            if l2 is not None: 
                l2 = l2.next
        
        if front_digit > 0 :
            current.next = ListNode(front_digit)

        return dummy.next
        