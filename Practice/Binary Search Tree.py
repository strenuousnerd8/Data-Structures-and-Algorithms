from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def findMin(self):
        if not self.left:
            return self.data
        return self.left.findMin()

    def findMax(self):
        if not self.right:
            return self.data
        return self.right.findMax()

    def inOrder(self):
        elements = []
        if self.left:
            elements += self.left.inOrder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrder()
        return elements

    def preOrder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrder()
        if self.right:
            elements += self.right.preOrder()
        return elements

    def postOrder(self):
        elements = []
        if self.left:
            elements += self.left.preOrder()
        if self.right:
            elements += self.right.preOrder()
        elements.append(self.data)
        return elements

    def levelOrder(self):
        q = Queue()
        q.enqueue(self)
        res = []
        while not q.isEmpty():
            current = q.dequeue()
            res.append(current.data)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
        return res

    def search(self, key):
        if key == self.data:
            return True
        if key < self.data:
            if self.left:
                return self.left.search(key)
            else:
                return False
        else:
            if self.right:
                return self.right.search(key)
            else:
                return False

    def sum(self):
        lsum = self.left.sum() if self.left else 0
        rsum = self.right.sum() if self.right else 0
        return self.data + lsum + rsum

def treeBuilder(dataset):
    if not dataset:
        return
    root = BinarySearchTreeNode(dataset[0])
    for i in range(1, len(dataset)):
        root.addChild(dataset[i])
    return root

if __name__ == "__main__":
    arr = [17, 4, 1, 20, 9, 23, 18, 34]
    root = treeBuilder(arr)
    print(root.inOrder())
    print(root.preOrder())
    print(root.postOrder())
    print(root.search(34))
    print(root.findMin())
    print(root.findMax())
    print(root.sum())
    print(root.levelOrder())