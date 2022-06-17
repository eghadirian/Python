class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

def inorder_traversal(root):
    res = []
    if root:
        res = inorder_traversal(root.left)
        res.append(root)
        res += inorder_traversal(root.right)
    return res

def preorder_traversal(root):
    res = []
    if root:
        res.append(root)
        res += preorder_traversal(root.left)
        res += preorder_traversal(root.right)
    return res

def postorder_traversal(root):
    res = []
    if root:
        res = postorder_traversal(root.left)
        res += postorder_traversal(root.right)
        res.append(root.data)
    return res

def inverse(root):
    if root == None:
        return
    root.left, root.right = inverse(root.left), inverse(self.right)
    return root
