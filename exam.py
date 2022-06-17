def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(l, r, arr):
    if len(arr) == 1:
        return arr
    if l < r:
        pi = partition(l, r, arr)
        quick_sort(l, pi-1, arr)
        quick_sort(pi+1, r, arr)
    return arr
def partition(l, r, arr):
    pvt, ptr = arr[r], l
    for i in range(l, r):
        if arr[i] < pvt:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[r] = arr[r], arr[ptr]
    return ptr

def sum_of_two(arr, val):
    found = set()
    for el in arr:
        if val - el in found:
            return True
        found.add(el)
    return False
def func(arr):
    n = len(arr)
    for i in range(n):
        if sum_of_two(arr[:i]+arr[i+1:], arr[i]):
            return True
    return False

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL():
    def __init__(self):
        self.head = None
    def append(self, data_in):
        new_node = Node(data_in)
        new_node.next = self.head
        self.head = new_node

def merge(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    merged_head = None
    if head1.data < head2.data:
        merged_head = head1
        merged_head.next = merge(head1.next, head2)
    else:
        merged_head = head2
        merged_head.next = merge(head1, head2.next)

class binary_tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data_in):
        if self.data:
            if self.data < data_in:
                if self.left:
                    self.left.append(data_in)
                else:
                    self.left = binary_tree(data_in)
            else:
                if self.right:
                    self.right.append(data_in)
                else:
                    self.right = binary_tree(data_in)
        else:
            self.data = binary_tree(data_in)
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
    root.left, root.right = inverse(root.left), inverse(root.right)
    return root

def combinations(lst, n):
    if n == 0:
        return [[]]
    combs = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[0:i] + lst[i + 1:]
        remainlst_combo = combinations(remLst, n-1)
        for p in remainlst_combo:
             combs.append([m, *p])      
    return combs
