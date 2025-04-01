from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # Collect values starting from this node
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        # Join them with a separator, e.g. "->"
        return " -> ".join(values)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while (list1 and list2):
            if(list1.val <= list2.val):
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            
            tail = tail.next

        if(list1):
            tail.next = list1
        
        if(list2):
            tail.next = list2
        
        return dummy.next

sol = Solution()
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(1, ListNode(1, ListNode(4)))
res = sol.mergeTwoLists(list1, list2)
print(res)
        
