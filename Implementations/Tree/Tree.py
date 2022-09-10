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

    def printTree(self):
        spaces = " " * (self.getLevel() * 3)
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def printTreeByLevel(self, level):
        if self.getLevel() > level:
            return
        spaces = ' ' * (self.getLevel() * 3)
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.printTreeByLevel(level)

Electronics = TreeNode("Electronics")
Laptops = TreeNode("Laptops")
Electronics.addChild(Laptops)
Laptops.addChild(TreeNode("Asus"))
Laptops.addChild(TreeNode("Dell"))
Laptops.addChild(TreeNode("Lenovo"))

Phones = TreeNode("Phones")
Electronics.addChild(Phones)
Phones.addChild(TreeNode("Samsung"))
Phones.addChild(TreeNode("Sony"))
Phones.addChild(TreeNode("Apple"))

TVs = TreeNode("TVs")
Electronics.addChild(TVs)
TVs.addChild(TreeNode("LG"))
TVs.addChild(TreeNode("Benq"))
TVs.addChild(TreeNode("Toshiba"))

# Electronics.printTree()
Electronics.printTreeByLevel(2)