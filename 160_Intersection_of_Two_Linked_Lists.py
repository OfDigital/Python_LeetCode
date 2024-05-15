from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr)
            curr = curr.next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    ll1, ll2 = headA, headB

    while ll1 != ll2:
        ll1 = ll1.next if ll1 else headB
        ll2 = ll2.next if ll2 else headA
    return ll1 


linkedList1 = LinkedList()
linkedList2 = LinkedList()

# [4,1,8,4,5]
# [5,6,1,8,4,5]

linkedList1.add(4)
linkedList1.add(1)
linkedList1.add(8)
linkedList1.add(4)
linkedList1.add(5)

linkedList2.add(5)
linkedList2.add(6)
linkedList2.add(1)
linkedList2.add(8)
linkedList2.add(4)
linkedList2.add(5)

# get the heads of the linked lists
headA = linkedList1.head
headB = linkedList2.head


print(getIntersectionNode(headA, headB))
print(linkedList1.print_list())