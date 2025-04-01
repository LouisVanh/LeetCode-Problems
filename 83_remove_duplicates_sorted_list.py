from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}" 
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sorted in ascending order,
        # We can use a sliding window to traverse the linked list
        dummy = head
        if(not head): return head
        while head.next:
            print(f"d: {dummy}")
            print(f"h: {head}")
            prev = head.val
            curr = head.next.val
            if(prev != curr): head = head.next
            else: head.next = head.next.next

        print("end")
        return dummy
    

sol = Solution()
r=sol.deleteDuplicates(ListNode(5, ListNode(6, ListNode(7,ListNode(7, ListNode(8, ListNode(8)))))))
print(r)
r=sol.deleteDuplicates(ListNode(1, ListNode(1, ListNode(1,ListNode(1, ListNode(1, ListNode(1)))))))
print(r)
r=sol.deleteDuplicates(ListNode(None))
print(r)