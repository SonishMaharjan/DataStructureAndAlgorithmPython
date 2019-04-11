class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self, rootData):
        self.root = Node(rootData)

    def insert(self, data, parent=None):

        if not parent:
            parent = self.root

        if data < parent.data:
            if parent.left:
                self.insert(data, parent.left)

            else:
                parent.left = Node(data)

        else:
            if parent.right:
                self.insert(data, parent.right)
            else:
                parent.right = Node(data)



    def printTree(self,currentNode=None):

        """this function automatically sorts and prints also a tree travesing"""
        #this is inorder traversal --> left --> root --> right
        if not currentNode:
            currentNode = self.root

        if currentNode.left:
            self.printTree(currentNode.left)

        print(currentNode.data)

        if currentNode.right:
            self.printTree(currentNode.right)



    def preOrderTraverse(self,parent=None):
        """root->left->right"""


        if not parent:
            parent = self.root

        print(parent.data)

        if parent.left:

            self.preOrderTraverse(parent.left)

        if parent.right:
            self.preOrderTraverse(parent.right)

    def postOrderTraverse(self, parent=None):
        """left->right->root"""


        if not parent:
            parent = self.root

        if parent.left:

            self.postOrderTraverse(parent.left)

        if parent.right:
            self.postOrderTraverse(parent.right)


        print(parent.data)











bt = BinaryTree(4)
bt.insert(2)
bt.insert(12)
bt.insert(31)
bt.insert(7)
bt.insert(16)


# bt.printTree()
# print("preorder traverse")
# bt.preOrderTraverse()
print("l right root")
bt.postOrderTraverse()