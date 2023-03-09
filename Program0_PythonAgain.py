##################################################
###Noah Jones
###CSC-325
###Date: 3/8/2023
###Program 0 Python Again
##################################################

###Description: Simple python linked list implemented with node class along with a selection sort algorithm for the list

#Import necessary packages for random number generation for node values
from random import randint


#Node Class
class Node:

    #Node Init method
    def __init__(self, value):
        self._value=value
        #Set the next node to empty as that will have to implemented in run time
        self.next_node=None
        

    #Accessor for value
    @property
    def value(self):
        return self._value

    #Mutator for value
    @value.setter
    def set_node_val(self, integer):
        self._value=integer

    
    #Accessor for next node
    @property
    def next(self):
        return self.next_node

    #Mutator for next node
    @next.setter
    def set_next(self, node):
        self.next_node=node

    
    

#Linked list class
class LinkedList:
    def __init__(self, length):
        #Check for edge cases
        if length < 0:
            raise Exception("invalid list length")
        else:
            self.list_length=length
        #Head will be assigned in next seciton
        self.head=Node(randint(0,100))

        #Populate list with nodes
        #Keep temp node for better data manipulation
        temp = self.head
        for i in range(length):
            node = Node(randint(0,100))
            if temp == None:
                pass
            else:
                temp.set_next=node
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
            if temp.next == None:
                break
            else:
                temp = temp.next
        #Return last value before we reached the end of the list
        return temp.value 



    #Print out list
    def print_list(self):
        current = self.head
        while True:
            if current.next == None:
                break
            else:
                print(current.value, end=" ")
                current=current.next

    #Swap function
    def swap(self,node, node_to_swap):
        #Keep temporoaty variable to 1st node
        temp_val = node.value
        #Set 1st node to value of 2nd 
        node.set_node_val=node_to_swap.value
        #Set value of 2nd node to the original value of the 1st node
        node_to_swap.set_node_val=temp_val


    #Selection Sort for linked list
    def Ssort(self):
        #start at head with both the node object and the value inside 
        start_node = self.get_head()
        start_min = start_node.value
       
        #Traverse list
        #For loop to analyse one item agains the rest of the remaining unsorted list
        for i in range(self.list_length):
            new_min=start_min
            new_min_node=start_node
            #variable to hold our new minimum value if we find one
            
            #Iterate to the first node we will compare our starting node with
            current_node=start_node.next

            #Check for edge case if the first node is less than the second node 
            if start_min < current_node.value:
                new_min=start_min
                new_min_node=start_node

            #Compare 
            for j in range(i+1,self.list_length):
                    
                if new_min > current_node.value:
                    new_min=current_node.value
                    new_min_node=current_node
                if current_node.next == None:
                    break
                else:
                    current_node = current_node.next

            #if we found a new minimum value replace it with the value in the node we started from
            if (new_min != None):
                #Swap the node values, NOT the object
                self.swap(start_node, new_min_node)
        
            #Increment the starting position
            start_node=start_node.next
            start_min=start_node.value
            
            



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
print("\nHead Data: " , my_list.get_head().value, end=" ")
print("\nTail Data: " , my_list.get_tail(), end=" ")
print("\n")


#Sorted
my_list.Ssort()
print("\nSorted List: ", end=" ")
my_list.print_list()
print("\nHead Data: " , my_list.get_head().value, end=" ")
print("\nTail Data: " , my_list.get_tail(), end=" ")
print("\n")

