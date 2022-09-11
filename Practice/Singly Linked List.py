class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertEnd(self, data):
        if not self.head:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insertAt(self, index, data):
        if index < 0 or index >= self.getLength():
            raise IndexError('Index out of range')
        if index == 0:
            self.insertBeginning(data)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def print(self):
        if not self.head:
            print('Stack underflow!')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr + 'None')

    def insertValues(self, dataset):
        self.head = None
        if not dataset:
            return -1
        for element in dataset:
            self.insertEnd(element)

    def removeAt(self, index):
        if index < 0 or index > self.getLength():
            raise IndexError('Index out of range')
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            count += 1
            itr = itr.next

    def reverse(self):
        nextNode = current = self.head
        prev = None
        while nextNode:
            nextNode = nextNode.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

    def checkCycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def addCycle(self):
        head = self.head
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(1, head.next)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertBeginning(1)
    ll.insertBeginning(3)
    ll.insertEnd(0)
    ll.insertEnd(-1)
    ll.insertAt(1, 2)
    ll.insertValues([1, 2, 3, 4, 5])
    ll.removeAt(4)
    ll.print()
    ll.reverse()
    ll.print()
    print('Length:', ll.getLength())
    #ll.addCycle()
    print(ll.checkCycle())