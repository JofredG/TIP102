print("__________________Problem 1:")
'''
Understand
    Given a string with [,],{,},(,) characters decide if they are all closed
Match
    Stack DS
Plan
    Iterate through the string appending all the opening characters to their respective stacks and popping from that stack
    when it's a closing character.
Implement
'''
def is_valid_post_format(posts):
    stack = []
    dic = {")": "(", "]": "[", "}": "{"}  # Mapping closing to opening brackets

    for char in posts:
        if char in {"(", "[", "{"}:  # Push opening brackets
            stack.append(char)
        elif char in {")", "]", "}"}:  # Process closing brackets
            if not stack or stack.pop() != dic[char]:  # Ensure matching
                return False

    return not stack  # True if stack is empty, False otherwise
            


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
