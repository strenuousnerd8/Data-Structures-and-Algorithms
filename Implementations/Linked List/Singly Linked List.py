class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value): # Insert in the beginning
        node = Node(value, self.head)
        self.head = node

    def print(self): # Print all the elements in the LL
        if self.head is None:
            print('The Linked List is Empty!')
            return False
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr + 'None')

    def append(self, value): # Insert at the end
        if self.head is None:
            self.head = Node(value, None)
            return True
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)

    def len(self): # Count the length of the LL
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def map(self, data): # Insert by iterable
        self.head = None
        for value in data:
            self.append(value)

    def pop(self, index): # Remove by Index
        if index < 0 or index >= self.len():
            raise IndexError("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return True
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        return True

    def insert(self, index, value): # Insert by Index
        if index < 0 or index > self.len():
            raise IndexError("Invalid Index")
        if index == 0:
            self.push(value)
            return True
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def add(self, key, value): # Insert after data
        if self.head is None:
            print('Linked List is Empty!')
            return False
        if self.head.data == key:
            self.head = Node(value, self.head.next)
            return True
        itr = self.head
        while itr:
            if itr.data == key:
                itr.next = Node(value, itr.next)
                break
            itr = itr.next

    def remove(self, value): # Remove by data
        if self.head is None:
            print('Linked List is Empty')
            return False
        if self.head.data == value:
            self.head = self.head.next
            return True
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
            itr = itr.next

    def reverse(self):
        prev = None
        current = nextNode = self.head
        while nextNode is not None:
            nextNode = nextNode.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev


newList = LinkedList()
newList.map([3,1,2])
newList.pop(2)
newList.insert(1, 'ugh')
newList.add('ugh', 2)
newList.remove('ugh')
newList.print()
newList.reverse()
newList.print()
print(newList.len())