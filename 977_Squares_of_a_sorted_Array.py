# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


def sortedSquares(nums: list[int]) -> list[int]:
    # Initialize left and right pointers
    l, r = 0, len(nums) - 1
    
    # Initialize an empty list to store squared values
    result = []
    
    # While the left pointer is less than or equal to the right pointer
    while l <= r:
        # Compare absolute values of numbers at left and right pointers
        if abs(nums[l]) < abs(nums[r]):
            # If absolute value of number at left pointer is smaller,
            # append square of number at right pointer to result
            result.append(nums[r] ** 2)
            # Move the right pointer to the left
            r -= 1
        else:
            # If absolute value of number at right pointer is smaller or equal,
            # append square of number at left pointer to result
            result.append(nums[l] ** 2)
            # Move the left pointer to the right
            l += 1
    
    # Return the result list in reversed order
    return result[::-1]


print(sortedSquares([-7,-3,2,3,11]))
# Time Complexity Analysis:
# The time complexity of this function is O(n), where n is the number of elements in the input list nums.
# This is because the function iterates through each element in the list once, performing constant time operations.