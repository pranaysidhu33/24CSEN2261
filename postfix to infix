def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def postfix_to_infix(postfix):
    stack = []
    
    # Iterate through each character in the postfix expression
    for char in postfix:
        # If the character is an operand, push it to the stack
        if not is_operator(char):
            stack.append(char)
        else:
            # Pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Create the new infix expression with parentheses
            new_expr = f"({operand1} {char} {operand2})"
            
            # Push the new expression back to the stack
            stack.append(new_expr)
    
    # The final result is the only element in the stack
    return stack.pop()

# Example usage
postfix_expr = "ab+c*d+"
infix_expr = postfix_to_infix(postfix_expr)
print(f"Postfix: {postfix_expr}")
print(f"Infix: {infix_expr}")
