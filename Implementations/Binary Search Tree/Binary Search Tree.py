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
            elements += self.left.postOrder()
        if self.right:
            elements += self.right.postOrder()
        elements.append(self.data)
        return elements

    def search(self, key):
        if self.data == key:
            return True
        if key < self.data:
            if self.left:
                return self.left.search(key)
            else:
                return False
        if key > self.data:
            if self.right:
                return self.right.search(key)
            else:
                return False

    def min(self):
        if not self.left:
            return self.data
        return self.left.min()

    def max(self):
        if not self.right:
            return self.data
        return self.right.max()

    def sum(self):
        lsum = self.left.sum() if self.left else 0
        rsum = self.right.sum() if self.right else 0
        return self.data + lsum + rsum

    def levelOrder(self):
        q = Queue()
        q.enqueue(self)
        res = []
        while not q.isEmpty():
            currentNode = q.dequeue()
            res.append(currentNode.data)
            if currentNode.left:
                q.enqueue(currentNode.left)
            if currentNode.right:
                q.enqueue(currentNode.right)
        return res

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
    print(root.min())
    print(root.max())
    print(root.sum())
    print(root.levelOrder())