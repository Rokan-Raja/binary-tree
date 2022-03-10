class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def maxheight(temp):
    if temp is None:
        return -1
    else:
        r =maxheight(temp.left)
        l =maxheight(temp.right)
        if r > l:
            return r+1
        else:
            return l+1
def insert(temp,data):
    if not temp:
        root=node(data)
        return
    q=[]
    q.append(temp)
    while(len(q)):
        temp=q[0]
        q.pop(0)
        if not temp.left:
            temp.left=node(data)
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=node(data)
        else:
            q.append(temp.right)
if __name__ == "__main__":
    root = node(10)
    root.left = node(11)
    root.left.left = node(7)
    root.right = node(9)
    root.right.left = node(15)
    root.right.right = node(8)
    root.right.left.right=node(19)
    print("Binary Tree Height is:%d"%maxheight(root))