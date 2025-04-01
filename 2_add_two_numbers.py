from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"  # This will recursively print the entire linked list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        i, carrying = 0, 0
        while l1 or l2 or carrying:
            # Calculate the number of the current sum
            i = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carrying
            print(f"i: {i}")
            # If it's 2 digits, carry the 1 to the next sum
            if(i>9):
                i-=10
                tail.next = ListNode(i)
                carrying = 1

            # If it's one digit, simply add it to the tail and set carrying to no
            else:
                tail.next = ListNode(i)
                carrying = 0

            tail=tail.next
            # Go to the next number if there is one, if there's none left, the code will exit the while
            l2 = l2.next if l2 else None
            l1 = l1.next if l1 else None
        
        return dummy.next

sol = Solution()
r = sol.addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))), ListNode(1,ListNode(6,ListNode(4))))
print(r)
r = sol.addTwoNumbers(ListNode(0,ListNode(0,ListNode(1))), ListNode(1,ListNode(2,ListNode(3))))
print(r)
r = sol.addTwoNumbers(ListNode(9,ListNode(9,ListNode(9, ListNode(9, ListNode(9))))), ListNode(1,ListNode(2,ListNode(3))))
print(r)