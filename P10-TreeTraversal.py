class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res += self.inorder_traversal(root.right)
        return res
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorder_traversal(root.left)
            res += self.preorder_traversal(root.right)
        return res
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.data)
        return res
    def invert_tree(self, root):
       if root == None:
           return
       root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
       return root


        


