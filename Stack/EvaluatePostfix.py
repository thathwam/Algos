operator = ["+", "-", "*", "/", "^"]


def evaluate_postfix(equation):
    stack = []
    for ch in equation:
        if ch.isnumeric():
            stack.append(ch)
        elif ch in operator:
            right = stack.pop()
            left = stack.pop()
            eqn = left + ch + right
            stack.append(str(eval(eqn)))

    print("Answer = ", stack.pop())


evaluate_postfix("234+2-+")
