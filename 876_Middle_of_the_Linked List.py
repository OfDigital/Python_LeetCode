# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 
# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Finds the middle node of a singly-linked list.

    Args:
      head: The head node of the linked list.

    Returns:
      The middle node of the linked list, or None if the list is empty.

    This function uses the two-pointer technique with a time complexity of O(n)
    and a space complexity of O(1).
    """

    if not head:  # Handle empty list case
      return None

    slow = head
    fast = head

    # Traverse the list using two pointers:
    # - slow: Moves one step at a time.
    # - fast: Moves two steps at a time (if possible).
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # slow will be at the middle node when fast reaches the end or the second
    # node from the end (in case of an even-length list).
    return slow

if __name__ == "__main__":
    # Create some sample linked list nodes (replace with your actual data)
    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)

    # Create the head of the linked list
    head = node3

    # Call the middleNode function to find the middle node
    solution = Solution()
    middle_node = solution.middleNode(head)

    # Print the value of the middle node (or None if empty)
    if middle_node:
        print("Middle Node Value:", middle_node.val)
    else:
        print("Linked list is empty.")