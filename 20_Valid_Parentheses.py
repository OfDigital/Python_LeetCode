# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


def isValid(s):
    # TC = O(n) ; SC = O(n)
    # because we need to iterate over the string once
    # and we are using a check dictionary and stack for space 
    # so space complexity = O(n)
    
    n = len(s)
    if n&1 or n < 2:
        return False
    
    # odd length strings wont ever be balanced/valid
    # similarly strings with a single bracket wont be valid
    
    mapping = {'(':')', '{':'}','[':']'}
    stack = []
    for bracket in s:
        # if its character is opening bracket
        # then add it to stack

        if bracket in mapping:
            stack.append(bracket)

        # otherwise if the stack is empty
        # or if the closing bracket is not of the same type as the opening one
        # then sequence is not valid
        elif len(stack) == 0 or mapping[stack.pop()] != bracket:
            return False
        
    # if length of the stack is 0 meaning that all opening and closing
    # brackets matched then ans is Valid
    return len(stack) == 0

print(isValid("([]){}"))
