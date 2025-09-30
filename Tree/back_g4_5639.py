import sys
sys.setrecursionlimit(10**6)  # 제일 위에 넣기
#다시 풀기 

pre = [] 

while True:
    s = sys.stdin.readline().strip()
    if not s:
        break
    else:
        pre.append(int(s))

def postorder2(x,y):
    if x>y:
        return
    root = pre[x]
    mid = y+1
    for i in range(x+1,y+1):
        if root<pre[i]:
            mid = i
            break
    
    postorder2(x+1,mid-1)
    postorder2(mid,y)
    print(root , end= '\n')
    
    pass

postorder2(0,len(pre)-1)

exit()


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def postorder(node): # 재귀 형식 말고
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

def postorder_iter(root):
    stack = []
    last_visited = None
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left

        else:
            node = stack[-1]
            if node.right and last_visited is not node.right:
                cur = node.right
            else:
                print(node.data)
                last_visited = stack.pop()
    pass

class BST:
    def __init__(self):
        self.root = None


    def insert_Node(self, num):
        if self.root == None:
            self.root = Node(num)
        else:
            self.cur = self.root
            while(True):
                if num<self.cur.data:
                    if self.cur.left == None:
                        self.cur.left = Node(num)
                        break
                    else:
                        self.cur = self.cur.left
                    pass

                else :
                    if self.cur.right == None:
                        self.cur.right = Node(num)
                        break
                    else:
                        self.cur = self.cur.right
                    
                    pass

#print("1"if sys.stdin.readline()=="\n" else "2")
BST = BST()
while(True):
    x =sys.stdin.readline()
    if not x or x=='\n':
        break
    BST.insert_Node(int(x))

postorder_iter(BST.root)