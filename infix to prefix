def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def infix_to_postfix(infix):
    stack = []
    postfix = []
    
    for char in infix:
        # If character is an operand, append it to the postfix expression
        if char.isalnum():
            postfix.append(char)
        # If character is '(', push it to the stack
        elif char == '(':
            stack.append(char)
        # If character is ')', pop from the stack until '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop '(' from stack
        # If character is an operator
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)
    
    # Pop all the remaining operators from the stack
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

def infix_to_prefix(infix):
    # Step 1: Reverse the infix expression
    infix = infix[::-1]
    
    # Step 2: Reverse parentheses in the expression
    infix = infix.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    # Step 3: Convert the modified infix to postfix
    postfix = infix_to_postfix(infix)
    
    # Step 4: Reverse the postfix expression to get the prefix expression
    return postfix[::-1]

# Example usage
infix_expr = "(A-B/C)*(A/K-L)"
prefix_expr = infix_to_prefix(infix_expr)
print(f"Infix: {infix_expr}")
print(f"Prefix: {prefix_expr}")
