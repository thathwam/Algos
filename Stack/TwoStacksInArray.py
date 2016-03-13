class TwoStacks:
    def __init__(self, size=20):
        self.size = size
        self.array = ['x'] * size
        self.tail1 = -1
        self.tail2 = size

    def push1(self, item):
        if self.tail1 + 1 != self.tail2:
            self.tail1 += 1
            self.array[self.tail1] = item
            print("1st Stack: Pushed item = " + item)
        else:
            raise StackIsFull()

    def push2(self, item):
        if self.tail2 - 1 != self.tail1:
            self.tail2 -= 1
            self.array[self.tail2] = item
            print("2nd Stack: Pushed item = " + item)
        else:
            raise StackIsFull()

    def pop1(self):
        if self.tail1 == -1:
            raise StackIsEmpty()
        else:
            self.tail1 -= 1
            print("1st Stack: Popping item = " + str(self.array[self.tail1 + 1]))
            return self.array[self.tail1 + 1]

    def pop2(self):
        if self.tail2 == self.size:
            raise StackIsEmpty()
        else:
            self.tail2 += 1
            print("1st Stack: Popping item = " + str(self.array[self.tail2 - 1]))
            return self.array[self.tail2 - 1]


class StackIsFull(Exception):
    def __init__(self):
        super().__init__("Stack is Full. Can't push")


class StackIsEmpty(Exception):
    def __init__(self):
        super().__init__("Stack is Empty. Can't pop")


t = TwoStacks(5)

t.push1('a')
t.push2('z')
t.push1('b')
t.push2('y')
t.push1('c')
t.pop1()
t.pop2()
