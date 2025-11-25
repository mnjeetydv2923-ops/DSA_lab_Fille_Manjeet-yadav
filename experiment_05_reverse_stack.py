# Experiment 05: Reverse a String using Stack

def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)

    rev = ""
    while stack:
        rev += stack.pop()
    return rev

# Example:
# print(reverse_string("hello"))
