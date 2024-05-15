# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    length_nums = len(nums)
    
    for x in range(0, length_nums - 2):
        if x > 0 and nums[x] == nums[x -1]:
            continue

        lower, higher = x + 1, length_nums - 1
        while higher > lower:
            threeSum = nums[lower] + nums[higher] + nums[x]
            if threeSum > 0:
                higher -= 1
            elif threeSum < 0:
                lower += 1
            else:
                result.append([nums[x], nums[lower], nums[higher]])
                lower += 1
                while nums[lower] == nums[lower - 1] and lower < higher:
                    lower += 1
    return result


print(threeSum(nums = [-1,0,1,2,-1,-4]))


#Time Complexity: 
#   sort() => O(nlog(n))
#   2 loop => O(n^2)
#   Time: O(nlog(n)) + O(n^2) => O(n^2)