# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs: list[str]) -> str:
        prefix=""
        if len(strs) == 0: 
            return prefix
    
        else :
            for i in range(len(strs)):
                c=strs[0][i]
                if all(a[i]==c for a in strs):
                    prefix+=c
                else:
                    break
        return prefix

print(longestCommonPrefix(["flower","flow","flight"]))