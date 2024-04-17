import Inventory

#Zainub Siddiqui
#This file will include the class implementations of the Node and Red Black Tree

class Node():
    def __init__(self, data: Inventory.Item):
        self.__data = data
        self.__list = [] #store duplicates
        self.__left = None
        self.__right = None
        self.__parent = None
        self.__color = "Red"

    def getLeft(self):
        return self.__left
    def setLeft(self, node):
        self.__left = node
    def getRight(self):
        return self.__right
    def setRight(self, node):
        self.__right = node
    def getParent(self):
        return self.__parent
    def setParent(self, node):
        self.__parent = node
    def getGParent(self):
        if self.__parent is not None:
            return self.__parent.__parent
        return None
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color
    def getData(self):
        return self.__data
    def displayNode(self):
        self.__data.display()
        # Display list of duplicates
        print("----------------------------------------------")
        print("List of Items:")
        for item in self.__list:
            item.display()
        print(f"Number of {self.__data.getName()}'s: {len(self.__list)}")
        print("----------------------------------------------")
    def ItemCount(self):
        return len(self.__list)
    def appendItem(self, data):
        self.__list.append(data)
    def decrementItem(self, item):
         name = item.getName()
         try:
             self.__list.remove(item)
             #print(f"{name} removed successfully.")
         except ValueError:
             print(f"{name} does not exist in the list!")

class RBTree():
    def __init__(self):
        self.__root = None
    
    #decrement item in list - wrapper
    def decrementItem(self, data):
        if self.__root == None:
            return 0
        return self.__decrementItem(self.__root, data)
    
    #decrement item in list - recursive
    def __decrementItem(self, root, data):
        if root is None:
            return 0
        
        if root.getData() == data:
            root.decrementItem(data)
            return 1
        
        if data < root.getData():
            return self.__decrementItem(root.getLeft(), data)
        else:
            return self.__decrementItem(root.getRight(), data)
    
    #find and count duplicates for particular item - wrapper
    def getItemCount(self, data):
        if self.__root == None:
            return 0
        return self.__getItemCount(self.__root, data)
    
    #find and count duplicates for particular item - recursive
    def __getItemCount(self, root, data):
        if root is None:
            return 0
        
        if root.getData() == data:
            # count how many 
            return root.ItemCount()
        
        if data < root.getData():
            return self.__getItemCount(root.getLeft(), data)
        else:
            return self.__getItemCount(root.getRight(), data)

    #search for duplicate and append to list
    def __searchItem(self, root: Node, data: Inventory.Item):
        if root is None:
            return False 
        
        if root.getData() == data:
            # Append to the list of duplicates
            root.appendItem(data)
            #print("Data found and appended to the list of duplicates!")
            return True
        
        if data < root.getData():
            return self.__searchItem(root.getLeft(), data)
        else:
            return self.__searchItem(root.getRight(), data)

    #insert into red black tree
    def insert(self, data: Inventory.Item):
        #first search if item already exists - if so, append to list
        flag = self.__searchItem(self.__root, data)
        #print(f"flag is {flag}")
        if flag:
            return 1

        # if not, set up node
        newNode = Node(data) #data is class object - type Item?
        newNode.setParent(None)
        newNode.setLeft(None)
        newNode.setRight(None)
        newNode.setColor("Red")
        newNode.appendItem(data)

        root = self.__root   #original root
        root_p = None        #root's parent

        #find position to insert
        while root != None:
            root_p = root
            if (newNode.getData() < root.getData()):
                root = root.getLeft()
            else:
                root = root.getRight()
        
        newNode.setParent(root_p)
        if root_p == None:
            self.__root = newNode
        elif newNode.getData() < root_p.getData():
            root_p.setLeft(newNode)
        else:
            root_p.setRight(newNode)

        #check if newNode is root - if so, make black
        if newNode.getParent() == None:
            newNode.setColor("Black")
            return
        
        if newNode.getGParent() == None:
            return
        
        #fix violations
        self.fixViolations(newNode)

    # left rotation
    def LeftRotation(self, node: Node):
        Rchild = node.getRight()
        node.setRight(Rchild.getLeft())
        if Rchild.getLeft() != None:
            Rchild.getLeft().setParent(node)

        Rchild.setParent(node.getParent())
        if node.getParent() == None:
            self.__root = Rchild
        elif node == node.getParent().getLeft():
            node.getParent().setLeft(Rchild)
        else:
            node.getParent().setRight(Rchild)
        Rchild.setLeft(node)
        node.setParent(Rchild)

    # right rotation 
    def RightRotation(self, node: Node):
        if node == None:
            return
        
        Lchild = node.getLeft()
        if Lchild == None:
            return
        node.setLeft(Lchild.getRight())
        if Lchild.getRight() != None:
            Lchild.getRight().setParent(node)
        
        Lchild.setParent(node.getParent())
        if node.getParent() == None:
            self.__root = Lchild
        elif node == node.getParent().getRight():
            node.getParent().setRight(Lchild)
        else:
            node.getParent().setLeft(Lchild)
        Lchild.setRight(node)
        node.setParent(Lchild)
    
    #display RBTree wrapper
    def display(self):
        if self.__root == None:
            return 0
        return self.__display(self.__root)

    #display RBTree recursive
    def __display(self, root: Node):
        if root == None:
            return 1
        
        self.__display(root.getLeft())
        root.displayNode()
        self.__display(root.getRight())
    
    #count number of items in tree - wrapper
    def getCount(self):
        if self.__root == None:
            return 0
        return self.__getCount(self.__root)
    
    #count number of items in tree - recursive
    def __getCount(self, root):
        if root == None:
            return 0
        
        return 1 + self.__getCount(root.getLeft()) + self.__getCount(root.getRight())
    
    #fix violations for red black tree!
    def fixViolations(self, node):
        while node.getParent() and node.getParent().getColor() == "Red":  # While parent is red and exists
            if node.getParent() == node.getGParent().getRight():  # if parent is right child of its parent
                uncle = node.getGParent().getLeft()  
                if uncle and uncle.getColor() == "Red":  
                    uncle.setColor("Black")  
                    node.getParent().setColor("Black")
                    node.getGParent().setColor("Red")  
                    node = node.getGParent()  
                else:
                    if node == node.getParent().getLeft():  # If node is left child of its parent
                        node = node.getParent()
                        self.RightRotation(node)  # do right rotation

                    if node.getParent():
                        node.getParent().setColor("Black")
                    if node.getParent() and node.getGParent():
                        node.getGParent().setColor("Red")
                        self.LeftRotation(node.getGParent())


            else:  # if parent is left child of its parent
                uncle = node.getGParent().getRight()  
                if uncle and uncle.getColor() == "Red":  
                    uncle.setColor("Black")  # Set color of childs as black
                    if node.getParent():
                        node.getParent().setColor("Black")
                    if node.getParent() and node.getGParent():
                        node.getGParent().setColor("Red")  # set color of grandparent as Red
                    node = node.getGParent()  
                else:
                    if node == node.getParent().getRight():  # if node is right child of its parent
                        node = node.getParent()
                        self.LeftRotation(node)  # do left rotate on parent of node
                    if node.getParent():
                        node.getParent().setColor("Black")
                    if node.getParent() and node.getGParent():
                        node.getGParent().setColor("Red")
                        self.RightRotation(node.getGParent())  # do right rotate on grandparent
            if node == self.__root:  
                break
        if self.__root:  
            self.__root.setColor("Black")  # Set color of root as black