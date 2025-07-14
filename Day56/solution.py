# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Initialize the result variable to 0.
        result = 0
      
        # Traverse the linked list.
        while head:
            # Bitwise left shift result by 1 (equivalent to multiplying by 2)
            # and perform bitwise OR with the current node's value
            # to append it to the binary number we are building.
            result = (result << 1) | head.val
          
            # Move to the next node in the linked list.
            head = head.next
      
        # Return the final decimal value of the binary number.
        return result