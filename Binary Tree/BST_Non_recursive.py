class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            temp = self.root
            while True:
                if val < temp.data:
                    if temp.left is None:
                        temp.left = Node(val)
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Node(val)
                        break
                    else:
                        temp = temp.right
                        
    def preorder(self,node):
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
            
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
            
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.data,end=" ")
            
        
if __name__ == '__main__':
    bst = BST()
    bst.insert(55)
    bst.insert(40)
    bst.insert(34)
    bst.insert(28)
    bst.insert(38)
    bst.insert(80)
    bst.insert(60)
    bst.insert(90)
    
    print("Preorder  : ",end="")
    bst.preorder(bst.root)
    print("\nInorder   : ",end="")
    bst.inorder(bst.root)
    print("\nPostorder  : ",end="")
    bst.inorder(bst.root)
    
    
    
    
    
    