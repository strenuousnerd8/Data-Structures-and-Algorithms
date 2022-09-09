from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1] if self.container else None

    def print(self):
        for i in self.container:
            print(i)

if __name__ == "__main__":
    mainStack = Stack()
    supportingStack = Stack()
    def push(value):
        if supportingStack.peek() is None:
            supportingStack.push(value)
        elif value < supportingStack.peek():
            supportingStack.push(value)
        else:
            mainStack.push(value)

    def pop():
        current = mainStack.pop()
        if current == supportingStack.peek():
            supportingStack.pop()

    def getMin():
        print(supportingStack.peek())

    push(2)
    push(3)
    pop()
    getMin()
    push(1)
    getMin()