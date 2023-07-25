from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        head = curr = ListNode()

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                curr.next, ptr1 = ptr1, ptr1.next
            else:
                curr.next, ptr2 = ptr2, ptr2.next
            curr = curr.next
                    
        while ptr1:
            curr.next, ptr1 = ptr1, ptr1.next
            curr = curr.next

        while ptr2:
            curr.next, ptr2 = ptr2, ptr2.next
            curr = curr.next
        
        return head.next