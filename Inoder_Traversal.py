class Binary_Search_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data< self.data:
            if self.left is None:
                self.left = Binary_Search_Tree_Node(data)
            else:
                self.left.add_child(data)
        elif data> self.data:
            if self.right is None:
                self.right = Binary_Search_Tree_Node(data)
            else:
                self.right.add_child(data)
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements
def Build_Tree(elements):
    root = Binary_Search_Tree_Node(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root
if __name__ == '__main__':
    numbers = [67,1,3,14,82,91,31,52]
    bst = Build_Tree(numbers)
    print("Inorder Traversal of the BST:", bst.inorder_traversal())
