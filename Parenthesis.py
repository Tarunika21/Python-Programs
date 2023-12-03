def isBalancedParenthesis(str):
    stack = []
    for ch in str:
        if ch in "[{(<":
            stack.append(ch)
        elif ch in "]})>":
            if not stack:
                return False
            top = stack.pop()
            if(ch == ")" and top != "(") or(ch == "]" and top != "[") or (ch == "}" and top != "{") or (ch== ">" and top != "<"):
                return False
    return len(stack) == 0

str = input("Enter the expression:")
if(isBalancedParenthesis(str)):                       
    print(f'The given expression {str} consists of balanced parentheses.')
else:
    print(f'The given expression {str} does not contain balanced parentheses.')