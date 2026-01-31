# We are creating a tree to represent electronic products
class Tree_Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def Add_child(self, child):
        child.parent = self
        self.children.append(child)
def build_product_tree():
    root = Tree_Node("Electronics")
    laptop = Tree_Node("Laptop")
    cellphone = Tree_Node("Cellphone")
    tv = Tree_Node("TV")
    tablet = Tree_Node("Tablet")
    desktop = Tree_Node("Desktop")
    camera = Tree_Node("Camera")
    # Add children to root
    root.Add_child(laptop)
    root.Add_child(cellphone)
    root.Add_child(tv)
    root.Add_child(tablet)
    root.Add_child(desktop)
    root.Add_child(camera)
    return root
if __name__ == "__main__":
    product_tree = build_product_tree()
    print("Root:", product_tree.data)
    print("Children:", [child.data for child in product_tree.children])
