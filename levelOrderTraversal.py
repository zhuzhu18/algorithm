class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')

'''
构造一棵二叉树，形状如下：
               a
             /   \ 
            b     c
             \   /
              d e
'''
node_a.left = node_b
node_a.right = node_c
node_b.right = node_d
node_c.left = node_e

def levelOrderTraversal(tree):
    T = tree
    queue = []
    queue.append(T)
    while queue:
        visit_node = queue.pop(0)
        print('%-4c' % visit_node.val, end='')
        if visit_node.left:
            queue.append(visit_node.left)
        if visit_node.right:
            queue.append(visit_node.right)

levelOrderTraversal(node_a)
