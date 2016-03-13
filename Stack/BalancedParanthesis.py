"""
There are 3 things to consider...
    1) "[] { ()" -- code need to identify this case
    2) Stack is empty or not before popping in case of "{}]()"
    3) Stack is empty or not at the end
"""

pair = {'}': '{', ')': '(', ']': '['}


def check_balanced_parenthesis(equation):
    stack = []
    balanced = False

    for index, ch in enumerate(equation, start=1):
        if ch in ['{', '(', '[']:
            stack.append(ch)
        elif ch in ['}', ')', ']']:
            if len(stack) != 0:
                popped_item = stack.pop()
            else:
                raise UnbalancedParenthesis(index)

            if pair[ch] == popped_item:
                balanced = True
            else:
                raise UnbalancedParenthesis(index)

    if balanced and len(stack) == 0:
        print("Equation = " + equation + " is balanced")
    else:
        raise UnbalancedParenthesis(equation.index(stack.pop()) + 1)


class UnbalancedParenthesis(Exception):
    def __init__(self, position):
        super().__init__("Unbalance found at position = " + str(position))


check_balanced_parenthesis("{}[()")
