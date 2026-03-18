def height(root):
    if root is None:
        return -1
    Left=height(root.left)
    Right=height(root.right)
    return 1+max(Left,Right)
        
