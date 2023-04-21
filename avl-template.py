import sys

class AVLTree:
    def __init__(self, root = None):
        self.root = root

    class AVLNode:
        def __init__(self, item, balance = 0, left = None, right = None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance

        def getBalance(self):
            return self.balance
        def setBalance(self, balance):
            self.balance = balance
        def __repr__(self):
            return f"AVLNode({repr(self.item)}, balance = {repr(self.balance)}, left = {repr(self.left)}, right = {repr(self.right)})"

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item

            if self.right != None:
                for elem in self.right:
                    yield elem
                    
        def _getLeaves(self):
            # trivial case
            if self == None:
                return
            ### WRITE YOUR CODE HERE ###

            #check if the current item is a leaf node itself
            if self.left is None and self.right is None:
                print(self.item, end=' ')
            
            
            #call recursively on left and right children
            #check on left
            if self.left is not None:
                self.left._getLeaves()
            # check on right
            if self.right is not None:
                self.right._getLeaves()

    def insert(self, item):

        def rotateRight(pivot):
            # pivot becomes right child of bad child
            # bad child's right child becomes pivot's left child

            # get pivot's left child node (bad child)
            leftChild = pivot.left

            #Check for none type
            if leftChild is None:
                return pivot

            #get the right subtree of the bad child
            right_subtree = leftChild.right

            #get the pivot the right child of the bad child
            leftChild.right = pivot

            #check for none type

            if right_subtree is None:
                pivot.left = None
            else:
                pivot.left = right_subtree

            #make the right subtree of the bad child the left child of the pivot
            pivot.left = right_subtree



            pivot.setBalance(pivot.getBalance() - 1 - max(right_subtree.getBalance(), 0))
            leftChild.setBalance(leftChild.getBalance() - 1 + min(pivot.getBalance(), 0))

            #update balances accordingly
            """if right_subtree != None:
                pivot.setBalance(pivot.getBalance() - 1 - max(right_subtree.getBalance(), 0))
            else:
                pivot.setBalance(pivot.getBalance() - 1)
        
            if leftChild != None:
                leftChild.setBalance(leftChild.getBalance() - 1 + min(pivot.getBalance(), 0))
            else:
                leftChild.setBalance(-1)"""
            
            # return bad child (node that is now root of the subtree)
            return leftChild
        
        def rotateLeft(pivot):
            # pivot becomes left child of bad child
            # bad child's left child becomes pivot's right child
            
            # get pivot's right child node (bad child)
            rightChild = pivot.right

            #Check for none type
            if rightChild is None:
                return pivot


            #get the left subtree of the bad child
            left_subtree = rightChild.left

            #make the pivot the left child of the bad child
            rightChild.left = pivot

            #check for none type
            if left_subtree is None:
                pivot.right = None
            else:
                pivot.right = left_subtree


            #amke the right subtree of the bad child the left child of the pivot 
            pivot.right = left_subtree

            #update balances acordingly
            pivot.setBalance(pivot.getBalance() + 1 - min(left_subtree.getBalance(), 0))
            rightChild.setBalance(rightChild.getBalance() + 1 + max(pivot.getBalance(), 0))

            """if left_subtree != None:
                pivot.setBalance(pivot.getBalance() + 1 - min(left_subtree.getBalance(), 0))
            else:
                pivot.setBalance(pivot.getBalance() + 1)

            if rightChild != None:
                rightChild.setBalance(rightChild.getBalance() + 1 + max(pivot.getBalance(), 0))
            else:
                rightChild.setBalance(1)"""

            # return bad child
            return rightChild

        def __insert(root, item):
            # if empty tree, create a node with given item
            if root == None:
                return AVLTree.AVLNode(item)


            # item to be inserted is smaller than root
            # inserting into left subtree with specific rules to handle
            if item < root.item:
                root.left = __insert(root.left, item)

                # handle Case 1 & Case 2 with no rotations
                ### WRITE YOUR CODE HERE ###
                if root.getBalance() == 0:
                    #adjust for left side
                    root.setBalance(-1)
                elif root.getBalance() == 1:
                    #adjust for right side
                    root.setBalance(0)
                else: #root.getbalnce() == -1 or -2 
                    # check for Case 3 when AVL is unbalanced
                    # Subcase A - Single Rotation
                    ### WRITE YOUR CODE HERE ###
                    # bad child must be left child, since we are in the left subtree
                    badChild = root.left
                    if badChild.getBalance() == -1:
                        root = rotateRight(root)
                        #balance should be 0 now
                        root.setBalance(0)
                        badChild.setBalance(0)

                    # Subcase B - Double Rotation
                    ### WRITE YOUR CODE HERE ###
                    else: #badChild.getBalance() == 1
                        badGrandChild = badChild.right
                        root.left = rotateLeft(badChild)
                        root = rotateRight(root)
                        # adjusting balances of pivot and bad child based on bad grandchild
                        # if value inserted at badGrandChild
                        # then pivot balance = 0, bad child balance = 0
                        ### WRITE YOUR CODE HERE ###
                        if badGrandChild.getBalance() == -1:
                            pivotBalance = 1
                            badChildBalance = 0
                        # if inserted value smaller than bad grandchild (left subtree)
                        # then pivot balance = 1, bad child balance = 0
                        ### WRITE YOUR CODE HERE ###
                        elif badChild.getBalance() == 0:
                            pivotBalance = 0
                            badChildBalance = 0
                        # if inserted value larger than bad grandchild (right subtree)
                        # then pivot balance = 0, bad child = -1
                        else:
                            pivotBalance = 0
                            badChildBalance = -1
                        root = rotateRight(root)
                        root.setBalance(pivotBalance)
                        badChild.setBalance(badChildBalance)
                        badGrandChild.setBalance(0)


                      
                        
                        
                        ### WRITE YOUR CODE HERE ###

            # item to be inserted is larger than root
            # inserting into right subtree with specific rules to handle
            elif item > root.item:
                root.right = __insert(root.right, item)

                # handle Case 1 & Case 2 with no rotations
                ### WRITE YOUR CODE HERE ###
                if root.getBalance() == 0:
                    #adjust for left side
                    root.setBalance(1)
                elif root.getBalance() == -1:
                    #adjust for right side
                    root.setBalance(0)
                else: #root.getbalnce() == -1 or -2 
                    # check for Case 3 when AVL is unbalanced
                    # Subcase A - Single Rotation
                    ### WRITE YOUR CODE HERE ###
                    # bad child must be left child, since we are in the left subtree
                    badChild = root.right
                    if badChild.getBalance() == -1:
                        root = rotateLeft(root)
                        #balance should be 0 now
                        root.setBalance(0)
                        badChild.setBalance(0)

                    # Subcase B - Double Rotation
                    ### WRITE YOUR CODE HERE ###
                    else: #badChild.getBalance() == 1
                        badGrandChild = badChild.left
                        root.right = rotateRight(badChild)
                        # adjusting balances of pivot and bad child based on bad grandchild
                        # if value inserted at badGrandChild
                        # then pivot balance = 0, bad child balance = 0
                        ### WRITE YOUR CODE HERE ###
                        if badGrandChild.getBalance() == -1:
                            pivotBalance = -1
                            badChildBalance = 0
                        # if inserted value smaller than bad grandchild (left subtree)
                        # then pivot balance = 1, bad child balance = 0
                        ### WRITE YOUR CODE HERE ###
                        elif badChild.getBalance() == -1:
                            pivotBalance = 0
                            badChildBalance = 1
                        # if inserted value larger than bad grandchild (right subtree)
                        # then pivot balance = 0, bad child = -1
                        else:
                            pivotBalance = 0
                            badChildBalance = 0
                        root = rotateLeft(root)
                        root.setBalance(pivotBalance)
                        badChild.setBalance(badChildBalance)
            
                        
            # check if inserting duplicated value
            else:
                print(f"Insering duplicated value... {item}")
                raise Exception("Duplicate value")

            # once done __inserting return root
            return root
        
        # once done inserting update pivotFound value
        # and assign root with __insert return
        self.pivotFound = False
        self.root = __insert(self.root, item)

    # repr on tree calls repr on root node
    def __repr__(self):
        return f"AVLTree: {repr(self.root)}"

    # iter on tree calls iter on root node
    def __iter__(self):
        return iter(self.root)

    def __lookup(node, item):
        # returns True if value is in tree and False otherwise
        if node is None:
            return False
        
        #if less than nodes value, search left subtree
        if item < node.item:
            return node.__lookup(node.left, item)
        
        #otherwise check right
        if item > node.item:
            return node.__lookup(node.right, item)


        # returns True or False
        return AVLTree.__lookup(node.left, item)

    def __contains__(self, item):
        # checks if item is in the tree
        # runs __lookup on the tree root
        return AVLTree.__lookup(self.root, item)

    def leaves(self):
        # finds tree leaves
        self.root._getLeaves()  

def main():
    tree = AVLTree()

    # get values from input file
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()

    print(f"Values to be inserted: {values}")
    print()
    
    # insert values into the AVL tree
    for v in values:
        tree.insert(int(v))
        print(f"Value {v} is inserted.")
    print()

    # print out the tree
    print(repr(tree))
    print()
    
    # print out tree in-order traversal
    print("In-order traversal: ", end = "")
    for node in tree:
        print(node, end = " ")    
    print()

    # print out tree leaves
    print("\nLeaves: ", end = "")
    tree.leaves()
    print()
    
    # check if given values are in the tree
    print()
    for val in [10, 17, 35, 38, 40]:
        if (val in tree):
            print(f"Value {val} is in tree")
        else:
            print(f"Value {val} is not in tree")  

main()
