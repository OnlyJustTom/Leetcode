# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        carry = 0
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0 
            sum = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10
            node = ListNode(sum)
            tail.next = node
            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        result = head.next
        head.next = None
        return result