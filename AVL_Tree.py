class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.ht = 0 
def height(root):
    if root is None:
        return -1
    return root.ht
def get_balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)
def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.ht = 1 + max(height(y.left), height(y.right))
    x.ht = 1 + max(height(x.left), height(x.right))
    return x
def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.ht = 1 + max(height(x.left), height(x.right))
    y.ht = 1 + max(height(y.left), height(y.right))
    return y
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        return root
    root.ht = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)
    if balance > 1 and value < root.left.value:
        return right_rotate(root)
    if balance < -1 and value > root.right.value:
        return left_rotate(root)
    if balance > 1 and value > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and value < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [f"{root.value}(BF={get_balance(root)})"] + inorder(root.right)
def preorder(root):
    if root is None:
        return []
    return [f"{root.value}(BF={get_balance(root)})"] + preorder(root.left) + preorder(root.right)
if __name__ == "__main__":
    n = int(input()) 
    arr = list(map(int, input().split()))
    value = int(input())  
    root = None
    for num in arr:
        root = insert(root, num)
    root = insert(root, value)
    print(" ".join(inorder(root)))
    print(" ".join(preorder(root)))
