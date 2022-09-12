class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print(self):
        spaces = " " * (self.getLevel() * 3)
        prefix = spaces + "|__ "
        print(prefix + self.data)
        for child in self.children:
            child.print()

    def printByLevel(self, level):
        if self.getLevel() > level:
            return
        spaces = " " * (self.getLevel() * 3)
        prefix = spaces + "|__ "
        print(prefix + self.data)
        for child in self.children:
            child.printByLevel(level)

root = TreeNode("Electronics")
node = TreeNode("Laptop")
root.addChild(node)
node.addChild(TreeNode("HP"))
node.addChild(TreeNode("Lenovo"))
node.addChild(TreeNode("Asus"))
root.print()
print()
root.printByLevel(1)