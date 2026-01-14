def reverse_string(s):
    stack = []
    # Push 
    for ch in s:
        stack.append(ch)
    reversed_str = ""
    # Pop 
    while stack:
        reversed_str += stack.pop()
    return reversed_str
input_string=input()
print(reverse_string(input_string))
