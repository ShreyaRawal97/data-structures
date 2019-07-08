## Define a node
class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    #getter
    def get_value(self):
        return self.value

    #setter
    def set_value(self, value):
        return self.value

    #setters and getters for left and right node

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

## check

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")
