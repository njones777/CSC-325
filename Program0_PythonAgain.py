##################################################
###Noah Jones
###CSC-325
###Date: 3/8/2023
###Program 0 Python Again
##################################################

#Import necessary packages for random number generation for node values
from random import randint


#Node Class
class Node:

    #Node Init method
    def __init__(self):
        #Generate random number from 0 to 100 for node value
        self.value=randint(0,100)
        #Set the next node to empty as that will have to implemented in run time
        self.next_node=None
        
    #Mutator for value
    #@value.setter
    def set_node_val(self, value):
        self.value=value

    #Accessor for value
    #@property
    def get_val(self):
        return self.value
    
    #Mutator for next node
    #@node.setter
    def set_next(self, node):
        self.next_node=node

    #Accessor for next node
    #@property
    def next(self):
        return self.next_node
    

#Linked list class
class LinkedList:
    def __init__(self, length):
        #Check for edge cases
        if length < 0:
            raise Exception("invalid list length")
        else:
            self.list_length=length
        #Head will be assigned in next seciton
        self.head=Node()

        #Populate list with nodes
        #Keep temp node for better data manipulation
        temp = self.head
        for i in range(length):
            node = Node()
            if temp == None:
                pass
            else:
                temp.set_next(node)
            temp = node

        
    #Head accessor
    def get_head(self):
        return self.head
    
    #Tail accessor
    def get_tail(self):

        #Start at head node
        temp = self.head

        #Traverse list until we get to the end
        for i in range(self.list_length-1):
            if temp.next() == None:
                break
            else:
                temp = temp.next()
        #Return last value before we reached the end of the list
        return temp.get_val() 



    #Print out list
    def print_list(self):
        current = self.head
        while True:
            if current.next() == None:
                break
            else:
                print(current.get_val(), end=" ")
                current=current.next()

    #Swap function
    def swap(self,node, node_to_swap):
        temp_val = node.get_val()
        node.set_node_val(node_to_swap.get_val())
        node_to_swap.set_node_val(temp_val)


    #Selection Sort for linked list
    def Ssort(self):
        #start at head with both the node object and the value inside 
        start_node = self.get_head()
        start_min = start_node.get_val()
       
        #Traverse list
        #For loop to analyse one item agains the rest of the remaining unsorted list
        for i in range(self.list_length):
            new_min=start_min
            new_min_node=start_node
            #variable to hold our new minimum value if we find one
            
            #Iterate to the first node we will compare our starting node with
            current_node=start_node.next()

            #Check for edge case if the first node is less than the second node 
            if start_min < current_node.get_val():
                new_min=start_min
                new_min_node=start_node

            #Compare 
            for j in range(i+1,self.list_length):
                    
                if new_min > current_node.get_val():
                    new_min=current_node.get_val()
                    new_min_node=current_node
                if current_node.next() == None:
                    break
                else:
                    current_node = current_node.next()

            #if we found a new minimum value replace it with the value in the node we started from
            if (new_min != None):
                #Swap the node values, NOT the object
                self.swap(start_node, new_min_node)
        
            #Increment the starting position
            start_node=start_node.next()
            start_min=start_node.get_val()
            
            



################################
#MAIN
################################

#Get number of nodes from user input
start=int(input("Please, enter the number of nodes: "))

#Unsorted
my_list = LinkedList(start)
print("\n")
print("Unsorted list:", end=" ")
my_list.print_list()
print("\nHead Data: " , my_list.get_head().get_val(), end=" ")
print("\nTail Data: " , my_list.get_tail(), end=" ")
print("\n")


#Sorted
my_list.Ssort()
print("\nSorted List: ", end=" ")
my_list.print_list()
print("\nHead Data: " , my_list.get_head().get_val(), end=" ")
print("\nTail Data: " , my_list.get_tail(), end=" ")
print("\n")

