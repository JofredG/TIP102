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


print("__________________Problem 2:")
'''
Understand
    Given a list of strings reverse the order.
    Input - list of strings
    Output - list of strings in reverse order
    Constraints - Null
    Edge Cases - 
Plan - Since we already are given a 'stack' (a stack is a list only we use particular methods that emulate a stack like append() and pop())
we can just pop all the items in that stack to the list we want to return.
'''
def reverse_comments_queue(comments):
    res = []
    for _ in range(len(comments)):
        #print(comments[-1])
        res.append(comments.pop())
    return res
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


print("__________________Problem 3:")
'''
Understand
    Given a string, return true if it is symmetrical
    Input - String
    Output - Boolean
'''
def is_symmetrical_title(title):
  pass

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
