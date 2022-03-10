class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
def inorder(node):
    if (not node):
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)
def MergeTrees(t1, t2):
    if (not t1):
        return t2
    if (not t2):
        return t1
    t1.data += t2.data
    t1.left = MergeTrees(t1.left, t2.left)
    t1.right = MergeTrees(t1.right, t2.right)
    return t1
if __name__ == '__main__':
    root1 = newNode(1)
    root1.left = newNode(2)
    root1.right = newNode(3)
    root1.left.left = newNode(4)
    root1.left.right = newNode(5)
    root1.right.right = newNode(6)

    root2 = newNode(4)
    root2.left = newNode(1)
    root2.right = newNode(7)
    root2.left.left = newNode(3)
    root2.right.left = newNode(2)
    root2.right.right = newNode(6)

    print("Binary tree 1:")
    inorder(root1)
    print("\nBinary tree 2:")
    inorder(root2)

    root3 = MergeTrees(root1, root2)
    print("\nThe Merged Binary Tree is:")
    inorder(root3)
