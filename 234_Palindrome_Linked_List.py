# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True

# print(isPalindrome([1,2,2,1]))