#latihan1
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
        new = Node(data)

        #langkah 2
        if self.root == None:
            #jika iya
            self.root = new
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

def in_order(node):
    if node != None:
            in_order(node.left)
            print(node.data,end='-')
            in_order(node.right)

in_order(bst.root)
print(' ')
print('--------')

#latihan

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
tree.insert_root('F')
tree.insert_left(tree.root, 'B')
tree.insert_right(tree.root, 'G')
tree.insert_left(tree.root.left, 'A')
tree.insert_right(tree.root.left, 'D')
tree.insert_left(tree.root.left.right, 'C')
tree.insert_right(tree.root.left.right, 'E')
tree.insert_right(tree.root.right, 'I')
tree.insert_left(tree.root.right.right, 'H')


def in_order(node):
    if node != None:
            in_order(node.left)
            print(node.data,end='-')
            in_order(node.right)

in_order(tree.root)







