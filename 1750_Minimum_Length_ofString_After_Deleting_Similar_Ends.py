# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

# Example 1:

# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.
# Example 2:

# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".
# Example 3:

# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

def minimumLength(s: str) -> int:
    """
    Finds the minimum length of a string after removing characters 
    forming any continuous sub-strings where all characters are the same.

    Args:
        s: The input string.

    Returns:
        The minimum length of the string after removal.
    """

    if len(s) <= 1:  # Base case: String with length 0 or 1 needs no processing
        return len(s)

    while len(s) > 1 and s[0] == s[-1]:  # Loop until no more characters can be removed from ends
        i = 0
        while i + 1 < len(s) and s[i] == s[i + 1]:  # Find the end of the first repeated character block
            i += 1

        j = len(s) - 1
        while j - 1 > 0 and s[j] == s[j - 1] and j != i:  # Find the start of the last repeated character block (excluding the first block)
            j -= 1

        s = s[i + 1:j]  # Remove the characters between the pointers

    return len(s)  # Return the final length of the string


# Example usage
print(minimumLength("aabccabba"))  # Output: 2 (removing all characters 'a' and 'b')


# Time Complexity:

# The time complexity of this algorithm is  O(n), where n is the length of the input string s.

# Here's how the complexity breaks down:

# The initialization (l, r = 0, len(s) - 1) takes constant time (O(1)).
# The while loop iterates at most n times, in the worst case, where n is the length of the string. In each iteration:
# Assigning char takes constant time (O(1)).
# The inner while loops (moving l and r) iterate at most n times in the worst case, but typically much less since they stop when encountering a different character.
# The final return statement takes constant time (O(1)).
