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

    def is_balanced(self, data):
        self.flush()
        data = ''.join([i for i in data if i in ['(','[','{',')',']','}']])
        for char in data:
            if char in ['(','[','{']:
                self.push(char)
            elif char in [')',']','}']:
                if self.is_empty():
                    return False
                last_bracket = self.pop()
                if last_bracket == '(' and char == ')':
                    continue
                elif last_bracket == '[' and char == ']':
                    continue
                elif last_bracket == '{' and char == '}':
                    continue
                else:
                    return False
        return True if self.is_empty() else False


s = Stack()

print(s.is_balanced("{{[[(())]]}}"))     # --> True
print(s.is_balanced("))((a+b}{"))   # --> False
print(s.is_balanced("((a+b))"))     # --> True
print(s.is_balanced("))"))          # --> False
print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}")) # --> True
print(s.reverse_string("We will conquere COVID-19"))
s.flush()
s.push(5)
s.push(3)
s.push(1)
print(s.pop())
print(s.peek())
s.print()
