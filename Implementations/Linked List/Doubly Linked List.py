class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            node = Node(value, self.head, None)
            self.head = node
            return True
        node = Node(value, self.head, None)
        self.head.prev = node
        self.head = node

    def print(self):
        if self.head is None:
            print('The Linked List is Empty')
            return False
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr + 'None')

    def append(self, value):
        if self.head is None:
            node = Node(value, None, self.head)
            self.head = node
            return True
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(value, None, itr)
        itr.next = node

    def len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def map(self, dataset):
        self.head = None
        for value in dataset:
            self.append(value)

    def pop(self, index):
        if index < 0 or index >= self.len():
            raise IndexError('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return True
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert(self, index, value):
        if index < 0 or index > self.len():
            raise IndexError('Invalid Index')
        if index == 0:
            self.push(value)
            return True
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def printbackward(self):
        if self.head is None:
            print('Linked List is Empty')
            return False
        llstr = ''
        itr = self.last()
        while itr:
            llstr += ' <-- ' + str(itr.data)
            itr = itr.prev
        print('None' + llstr)

    def add(self, key, value):
        if self.head is None:
            print('Linked List is Empty')
            return False
        if self.head.data == key:
            node = Node(value, self.head.next, self.head)
            self.head.next = node
            return True
        itr = self.head
        while itr:
            if itr.data == key:
                node = Node(value, itr.next, itr)
                itr.next = node
                break
            itr = itr.next

if __name__ == '__main__':
    newList = DoublyLinkedList()
    newList.map(['and'])
    newList.push('3,')
    newList.push(1)
    newList.append(4)
    newList.append(4)
    newList.pop(4)
    newList.insert(1, 'two')
    newList.add(4, 'five')
    newList.print()
    newList.printbackward()
    print(newList.len())