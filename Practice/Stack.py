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

    def flush(self):
        self.container.clear()

    def isEmpty(self):
        return len(self.container) == 0

    def is_balanced(self, string):
        self.flush()
        brackets = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }
        string = ''.join([i for i in string if i in brackets or i in brackets.values()])
        for char in string:
            if char in brackets:
                self.push(char)
            elif char in brackets.values():
                if self.isEmpty():
                    return False
                last = self.pop()
                if last == '(' and char == brackets['(']:
                    continue
                if last == '[' and char == brackets['[']:
                    continue
                if last == '{' and char == brackets['{']:
                    continue
                else:
                    return False
        return True if self.isEmpty() else False

    def reverse(self, string):
        self.flush()
        rev = ''
        for char in string:
            self.push(char)
        while not self.isEmpty():
            rev += self.pop()
        return rev

if __name__ == '__main__':
    # mainStack = Stack()
    # supportingStack = Stack()

    # def push(data):
    #     if not supportingStack.peek():
    #         supportingStack.push(data)
    #     elif data < supportingStack.peek():
    #         supportingStack.push(data)
    #     else:
    #         mainStack.push(data)

    # def pop():
    #     curr = mainStack.pop()
    #     if curr == supportingStack.peek():
    #         supportingStack.pop()
    #     print(curr)

    # def getMin():
    #     print(supportingStack.peek())

    s = Stack()
    print(s.is_balanced("{{[[(())]]}}"))     # --> True
    print(s.is_balanced("))((a+b}{"))   # --> False
    print(s.is_balanced("((a+b))"))     # --> True
    print(s.is_balanced("))"))          # --> False
    print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}")) # --> True
    print(s.reverse("We will conquere COVID-19"))

    # push(2)
    # push(3)
    # pop()
    # getMin()
    # push(1)
    # getMin()