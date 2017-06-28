import sys
sys.setrecursionlimit(10**9)
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def findMax(root):
    if not root:
        return -sys.maxint
    else:
        return max(root.data,findMax(roo.left),findMax(root.right))

def present(root,data):
    if not root:
        return False
    if root.data==data:
        return True
    return present(root.left) or present(root.right)

def insert(root,data):
    if not root:
        root = Node(data)
        return
    else:
        q = [root]
        while q:
            temp = q.pop()
            if not temp.left:
                temp.left = Node(data)
                return
            q.append(temp.left)
            if not temp.right:
                temp.right = Node(data)
                return
            q.append(temp.right)

def size(root):
    if not root:
        return 0
    return size(root.left)+size(root.right)+1

def height(root):
    if not root:
        return 0
    else:
        return max(height(root.elft),height(root.right))+1