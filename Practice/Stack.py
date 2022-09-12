from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1] if self.container else None

if __name__ == '__main__':
    mainStack = Stack()
    supportingStack = Stack()

    def push(data):
        if not supportingStack.peek():
            supportingStack.push(data)
        elif data < supportingStack.peek():
            supportingStack.push(data)
        else:
            mainStack.push(data)

    def pop():
        curr = mainStack.pop()
        if curr == supportingStack.peek():
            supportingStack.pop()
        print(curr)

    def getMin():
        print(supportingStack.peek())


    push(2)
    push(3)
    pop()
    getMin()
    push(1)
    getMin()