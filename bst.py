
#bst tree 구조 잠깐 만들어보기
class Node :
    def __init__(self, num):
        self.data = num
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,num):
        self.root = None
    
    def Node_insert(self, num):
        if self.root == None:
            self.root = Node(num)
        else:
            self.curr = self.root
            while True:
                if num<self.curr.data:
                    if self.curr.left ==None:
                        self.curr.left = Node(num)
                        break
                    else:
                        self.curr = self.curr.left
                else:
                    if self.curr.right == None:
                        self.curr.right=Node(num)
                        break
                    else:
                        self.curr = self.curr.right

print("구조체로 구현한 이진 탐색 트리\n")
Binary = BinaryTree()
Binary.Node_insert(6)
Binary.Node_insert(3)


