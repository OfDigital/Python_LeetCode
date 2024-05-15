# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be created from the given combination.

# Note that the resulting string can have leading zeros.

 

# Example 1:

# Input: s = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
# Example 2:

# Input: s = "0101"
# Output: "1001"
# Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".


def maximumOddBinaryNumber(s: str) -> str:
    # Count the number of '1's in the input string
    ones_count = s.count("1")
    
    # Calculate the number of '0's in the input string
    zeros_count = len(s) - ones_count

    # Construct the resulting string:
    # Concatenate '1's (except one) followed by '0's and one final '1'
    result = "1" * (ones_count - 1) + "0" * zeros_count + "1"
    
    return result


# Test the function
print(maximumOddBinaryNumber("0101"))


# Time Complexity Analysis:

# Sorting the input string s takes O(n log n) time, where n is the length of the string.
# The loop iterates through the string once, which takes O(n) time.
# Within the loop, the swap operation takes constant time.
# Finally, joining the sorted characters into a string takes O(n) time.
