stack = []
postfix = ""
lastItem = ""


def pref(char):
    if char in ["+", "-"]:
        return 1
    elif char in ["*", "/"]:
        return 2
    elif char == "^":
        return 3
    else:
        return -1


def infix_to_postfix(equation):
    """
    Covert infix equation to postfix equation
    :param equation: input equation
    """
    global postfix, lastItem

    for char in equation:
        if char.isalnum():
            postfix = postfix + char
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while len(stack) != 0 and stack[-1] != "(":
                postfix = postfix + stack.pop()
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                return -1
        else:
            while len(stack) != 0 and pref(char) <= pref(stack[-1]):
                postfix = postfix + stack.pop()
            stack.append(char)

    while len(stack) != 0:
        postfix = postfix + stack.pop()

    print(postfix)


class Stack:
    data = []

    def __init__(self):
        pass

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            self.data.pop()

    def push(self, x):
        self.data.append(x)

def main():
    equation = "c*(a+(b/e))"
    infix_to_postfix(equation)


if __name__ == '__main__':
    main()

# c * a + b