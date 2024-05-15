# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d



def mergeAlternately(word1: str, word2: str) -> str:
    result = ''  # Initialize an empty string to store the merged result
    min_length = min(len(word1), len(word2))  # Determine the minimum length of the two words

    # Iterate over the characters of the words up to the minimum length
    for i in range(min_length):
        result += word1[i] + word2[i]  # Append characters from word1 and word2 alternately

    # Append the remaining characters of the longer word, if any
    if len(word1) > len(word2):
        result += word1[min_length:]  # Append remaining characters of word1
    elif len(word1) < len(word2):
        result += word2[min_length:]  # Append remaining characters of word2
        
    return result  # Return the merged result

# Time Complexity: O(min(m, n)), where m and n are the lengths of word1 and word2 respectively.
#                  The loop iterates over the minimum length of the two words.
# Space Complexity: O(m + n), where m and n are the lengths of word1 and word2 respectively.
#                   The space complexity is dominated by the merged result string.


# print(mergeAlternately("abc", "pqrsc"))