from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #use Floyd's tortoise and hare algorithm
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tor, hare = head, head
        while tor and hare and hare.next:
            tor = tor.next
            hare = hare.next.next

            if tor == hare:
                return True
        return False

        
        