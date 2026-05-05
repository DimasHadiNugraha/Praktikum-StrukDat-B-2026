class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.left = Node('F')

    def traverse_preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)
    
    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data, end=' ')
            self.traverse_inorder(node.right)
    
    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=' ')

    def get_leaf_nodes(self, node, leaf_nodes):
        if node is not None:
            if node.left is None and node.right is None:
                leaf_nodes.append(node.data)
            self.get_leaf_nodes(node.left, leaf_nodes)
            self.get_leaf_nodes(node.right, leaf_nodes)

tree = BinaryTree()
tree.insert_manual()
print(' ')
print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print('==========================================')
print(' ')
print('[INFO]membangun struktur gudang')
print('[INFO]struktur berhasil dibuat')
print(' ')

print('HASIL AUDIT:')
print('1. Pre-order: ', end='')
tree.traverse_preorder(tree.root)
print('\n2. In-order: ', end='')
tree.traverse_inorder(tree.root)
print('\n3. Post-order: ', end='')
tree.traverse_postorder(tree.root)
print('\n[DATA] gudang ujung (leaf nodes): ', end='')
leaf_nodes = []
tree.get_leaf_nodes(tree.root, leaf_nodes)
print(', '.join(leaf_nodes))
print('===========================================')
print('Audit Selesai !')







        





