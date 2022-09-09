from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        if len(self.container) == 0:
            raise Exception('Stack Underflow')
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def print(self):
        print(self.container)

    def reverse_string(self, data):
        self.flush()
        rev = ''
        for char in data:
            self.push(char)
        while self.container:
            rev += self.pop()
        return rev

    def flush(self):
        self.container.clear()

s = Stack()

print(s.reverse_string("We will conquere COVID-19"))
s.flush()
s.push(5)
s.push(3)
s.push(1)
print(s.pop())
print(s.peek())
s.print()