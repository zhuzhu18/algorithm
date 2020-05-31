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
中序遍历结果应为 bdaec
'''
node_a.left = node_b
node_a.right = node_c
node_b.right = node_d
node_c.left = node_e

def inOrderTraversal(tree: Node):
    T = tree
    stack = []
    while T is not None or len(stack) > 0:
        while T is not None:
            stack.append(T)
            T = T.left
        if len(stack) > 0:
            visit_node = stack.pop()
            print('%-4c' % visit_node.val, end='')
            T = visit_node.right
    print()

def preOrderTraversal(tree):
    T = tree
    stack = []
    while T or stack:
        while T:
            stack.append(T)
            visit_node = T
            print('%-4c'%visit_node.val, end='')
            T = visit_node.left
        if stack:
            temp = stack.pop()
            T = temp.right
    print()

def postOrderTraversal(tree):
    T = tree
    stack = []
    P = None       # 定义一个前一次已访问的节点
    while stack or T:
        while T:
            stack.append(T)
            T = T.left
        if stack:
            temp_node = stack.pop()    # 把左子树为空的节点弹出来，当右子树也为空时访问它，否则还要放回栈
            if temp_node.right and temp_node.right != P:
                stack.append(temp_node)
                T = temp_node.right
            else:
                if not stack or stack[-1].right != P:     # 当栈为空，即弹出前只剩一个节点或弹出后栈顶的节点不等于上一次访问的节点时
                    print('%-4c' % temp_node.val, end='')
                    T = None
                    P = temp_node
    print()

inOrderTraversal(node_a)
preOrderTraversal(node_a)
postOrderTraversal(node_a)
