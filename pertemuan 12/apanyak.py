'''tree'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self,data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node is not None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = self.root
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node is not None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = self.root
            parent_node.right = new_node

tree = BinaryTree()
tree.insert_root(10)
tree.insert_left(tree.root, 5)
tree.insert_right(tree.root, 15)
tree.insert_left(tree.root.left, 3)
tree.insert_right(tree.root.left, 7)
print(tree.root.data)  # Output: 10
print(tree.root.left.data)  # Output: 5
print(tree.root.right.data)  # Output: 15
print(tree.root.left.left.data)  # Output: 3
print(tree.root.left.right.data)  # Output: 7


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_root(self,data):
        #langkah 1 
        nodeBaru = Node(data)

        #langkah 2
        if self.root == None:
            #jika iya
            self.root = nodeBaru
            return
        
        #jika tidak
        #langkah 3
        P = self.root
        Q = self.root

        #langkah 4
        while Q != None and new.data != P.data:
            #langkah 5
            P = Q
            #langkah 6
            if new.data < P.data:
                Q = P.left
            #jika tidak
            else:
                Q = P.right

        #langkah 7
        if new.data == P.data:
        #jika iya
            print('datanya sama ni')
            return
    
        #jika tidak
        #langkah 8
        if new.data < P.data:
            P.left = new
        #jika tidak
        else:
            P.right = new
        
        #selesai

bst = BinaryTree()
bst.insert_root(10)
bst.insert_root(5)
bst.insert_root(15)
bst.insert_root(3)





        