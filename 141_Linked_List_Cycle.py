# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        all_nodes = []

        while head:
            if head in all_nodes:
                print("Linked list has a cycle.")
                return True
            else:
                all_nodes.append(head)
                head = head.next
        
        print("Linked list does not have a cycle.")
        return False

# Example usage:
if __name__ == "__main__":
    # Create a linked list with a cycle for testing
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Introducing a cycle

    solution = Solution()
    solution.hasCycle(node1)




# Time Complexity: O(n)
# The algorithm iterates through each node in the linked list once,
# where n is the number of nodes in the linked list. In the worst case, 
# it visits each node exactly once before reaching the end of the list. 
# Thus, the time complexity is linear with respect to the number of nodes in the linked list.