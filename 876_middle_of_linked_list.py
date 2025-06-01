from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next

        return " --> ".join(result)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # approach 1: counting

        # total_nodes = 0
        # start = head
        # while (head != None):
        #     total_nodes+=1
        #     head=head.next
        
        # # if there are 6 total nodes, we want to grab the 4th one. (middle or right of the two middle)
        # for _ in range(total_nodes//2):
        #     print(start)
        #     start=start.next
        
        # return start

        # approach 2: slow & fast pointer
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        return slow_ptr
    

sol = Solution()
r=sol.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
print(r)
r2=sol.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
print(r2)