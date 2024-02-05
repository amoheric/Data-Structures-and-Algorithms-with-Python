#
# NAME:
# DATE:
# DESC:
#


# Import necessary libraries for performance measurement, random number generation, plotting, and memory profiling.

import time  # imports time module for measuring time taken for the operations
import random  # imports random module for generating random numbers
import matplotlib.pyplot as plt  # imports matplotlib for plotting graphs
import memory_profiler  # Importing the memory_profiler module to measure memory usage


# Class for the tree node, My Node class for BST and AVL Tree
class TreeNode:
    
    
    def __init__(self, value):
        self.value = value  # Node value
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Node height, used in AVL Tree


# Class for the Binary Search Tree
class BinarySearchTree:  # my Binary Search Tree Implementation
    
    
    def __init__(self): # Constructor
        
        self.root = None  # Roots node of the BST
        


    def insert(self, value): # Inserts a value into the BST
        
        
        if not self.root: # If the tree is empty, create a new node and set it as the root
            
            self.root = TreeNode(value) # Create a new node and set it as the root
            
            
        else: # If the tree is not empty, call the recursive insert method
            
            self._insert_recursive(self.root, value) # Calls the recursive insert method
            


    def _insert_recursive(self, node, value): # Recursive insert method
        
        if value < node.value: # If the value is less than the current node value
            
            
            if not node.left: # If the left child is empty, create a new node and set it as the left child
                
                node.left = TreeNode(value) # Create a new node and set it as the left child
                
                
            else: # If the left child is not empty, call the recursive insert method
                
                self._insert_recursive(node.left, value) # Calls the recursive insert method
                
                
        elif value > node.value: # If the value is greater than the current node value
            
            
            if not node.right: # If the right child is empty, create a new node and set it as the right child
                
                node.right = TreeNode(value) # Create a new node and set it as the right child
                
                
            else: # If the right child is not empty, call the recursive insert method
                
                self._insert_recursive(node.right, value) # Call the recursive insert method
                
                # Duplicates are not inserted



    def delete(self, node, value): # Deletes a value from the BST
        
        if not node: # If the node is empty, return the node
            
            return node # Returns the node
        
        
        if value < node.value: # If the value is less than the current node value
            
            node.left = self.delete(node.left, value) # Calls the recursive delete method on the left child
            
            
        elif value > node.value: # If the value is greater than the current node value
            
            node.right = self.delete(node.right, value) # Calls the recursive delete method on the right child
            
            
        else: # If the value is equal to the current node value
            
            if not node.left: # If the left child is empty
                
                return node.right # Returns the right child
            
            elif not node.right: # If the right child is empty
                
                return node.left # Returns the left child
            
            
            temp = self.find_min(node.right) # Finds the minimum value in the right subtree
            
            node.value = temp.value # Sets the current node value to the minimum value
            
            node.right = self.delete(node.right, node.value) # Calls the recursive delete method on the right child
            
            
        return node # Returns the node
    

    def find_min(self, node): # Finds the minimum value in the BST
        
        while node.left: # While the left child is not empty
            
            node = node.left # Sets the left child as the current node
            
        return node # Returns the current node

class AVLTree(BinarySearchTree): # My AVL Tree Implementation
    
    def insert(self, value): # Inserts a value into the AVL Tree
        
        self.root = self._insert_recursive(self.root, value) # Calls the recursive insert method
        
        

    def _insert_recursive(self, node, value): # Recursive insert method
        
        if not node: # If the node is empty, create a new node and set it as the root
            
            return TreeNode(value) # Creates a new node and set it as the root
        
        if value < node.value: # If the value is less than the current node value
            
            node.left = self._insert_recursive(node.left, value)   # Calls the recursive insert method on the left child
            
        elif value > node.value: # If the value is greater than the current node value
            
            node.right = self._insert_recursive(node.right, value) # Calls the recursive insert method on the right child
            
        else: # If the value is equal to the current node value
            
            return node # Return the node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)) # Updates the height of the current node
        
        balance = self.get_balance(node) # Get the balance factor of the current node
        

        if balance > 1 and value < node.left.value: # Left Left Case
            
            return self.right_rotate(node) # Performs a right rotation
        
        
        if balance < -1 and value > node.right.value: # Right Right Case
            
            return self.left_rotate(node) # Performs a left rotation
        
        
        if balance > 1 and value > node.left.value: # Left Right Case
            
            node.left = self.left_rotate(node.left) # Performs a left rotation on the left child
            
            return self.right_rotate(node) # Performs a right rotation
        
        
        if balance < -1 and value < node.right.value: # Right Left Case
            
            node.right = self.right_rotate(node.right) # Performs a right rotation on the right child
            
            
            return self.left_rotate(node) # Performs a left rotation
        

        return node # Returns the node
    

    def delete(self, node, value): # Deletes a value from the AVL Tree
        
        
        if not node: # If the node is empty, return the node
            
            return node # If the node is empty, return the node
        
        
        elif value < node.value: # If the value is less than the current node value
            
            node.left = self.delete(node.left, value) # Calls the recursive delete method on the left child
            
            
        elif value > node.value: # If the value is greater than the current node value
            
            node.right = self.delete(node.right, value) # Calls the recursive delete method on the right child
            
            
        else: # If the value is equal to the current node value
            
            
            if not node.left: # If the left child is empty
                
                temp = node.right # Sets the right child as the temporary node
                
                node = None # Sets the current node as None
                
                
                return temp # Returns the temporary node
            
            
            elif not node.right: # If the right child is empty
                
                temp = node.left # Sets the left child as the temporary node
                
                node = None # Sets the current node as None 
                
                return temp # Returns the temporary node
            

            temp = self.find_min(node.right) # Finds the minimum value in the right subtree
            
            node.value = temp.value # Sets the current node value to the minimum value
            
            node.right = self.delete(node.right, temp.value) # Call the recursive delete method on the right child
            

        if not node: # If the node is empty, return the node
            
            return node # Returns the node
        

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)) # Updates the height of the current node
        
        balance = self.get_balance(node) # Gets the balance factor of the current node
        

        if balance > 1 and self.get_balance(node.left) >= 0: # Left Left Case
            
            return self.right_rotate(node) # Performs a right rotation
        

        if balance < -1 and self.get_balance(node.right) <= 0: # Right Right Case
            
            return self.left_rotate(node) # Performs a left rotation
        

        if balance > 1 and self.get_balance(node.left) < 0: # Left Right Case
            
            node.left = self.left_rotate(node.left) # Performs a left rotation on the left child
            
            return self.right_rotate(node) # Performs a right rotation
        

        if balance < -1 and self.get_balance(node.right) > 0: # Right Left Case
            
            node.right = self.right_rotate(node.right) # Performs a right rotation on the right child
            
            return self.left_rotate(node) # Performs a left rotation
        

        return node # Returns the node
    


    def left_rotate(self, node): # Left rotation method
        
        y = node.right # Sets the right child as y
        
        T2 = y.left    

        y.left = node # Sets the current node as the left child of y
        
        node.right = T2 # Sets T2 as the right child of the current node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)) # Updates the height of the current node
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right)) # Updates the height of y

        return y # Returns y
    
    

    def right_rotate(self, node): # Right rotation method
        
        y = node.left # Sets the left child as y
        
        T3 = y.right # Sets the right child of y as T3

        y.right = node # Sets the current node as the right child of y
        
        node.left = T3 # Sets T3 as the left child of the current node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)) # Updates the height of the current node
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right)) # Updates the height of y

        return y # Returns y
    
    

    def get_height(self, node): # Gets the height of a node
        
        if not node: # If the node is empty, return 0
            
            return 0 # Returns 0
        
        return node.height # Returns the height of the node
    


    def get_balance(self, node): # Gets the balance factor of a node
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right) # Returns the balance factor of the node
    
    

def measure_performance(tree_class, node_counts): # Measures the performance of the BST and AVL Tree
    
    insertion_times = [] # List to store the insertion times
    
    deletion_times = [] # List to store the deletion times
    
    
    for count in node_counts: # For each number of nodes
        
        tree = tree_class() # Create a new tree
        
        nodes = random.sample(range(count * 10), count) # Generate a list of random numbers
        
        start_time = time.time() # Start the timer
        
        
        for node in nodes: # For each node
            
            tree.insert(node) # Inserts the node into the tree
            
        insertion_times.append(time.time() - start_time) # Appends the time taken to the insertion times list
        
        start_time = time.time() # Starts the timer
        
        
        for node in nodes: # For each node
            
            tree.delete(tree.root, node) # Deletes the node from the tree
            
        deletion_times.append(time.time() - start_time) # Appending the time taken to the deletion times list
        
    return (insertion_times, deletion_times) # Returns the insertion and deletion times



def plot_performance(node_counts, bst_times, avl_times, operation="Insertion"): # Plots the performance of the BST and AVL Tree
    
    plt.figure(figsize=(10, 5)) # Sets the figure size
    

    if operation == "Insertion": # If the operation is insertion
        
        plt.plot(node_counts, bst_times[0], 'o-', label='BST') # Plots the BST insertion times
        
        plt.plot(node_counts, avl_times[0], 'x-', label='AVL') # Plots the AVL insertion times
        
    else:
        plt.plot(node_counts, bst_times[1], 'o-', label='BST') # Plots the BST deletion times
        
        plt.plot(node_counts, avl_times[1], 'x-', label='AVL') # Plots the AVL deletion times
        
    plt.xlabel('Number of Nodes') # Sets the x-axis label
    
    plt.ylabel(f'Time taken for {operation} (seconds)') # Sets the y-axis label
    
    plt.xscale('log') # Sets the x-axis scale to logarithmic
    
    plt.yscale('log') # Sets the y-axis scale to logarithmic
    
    plt.title(f'{operation} Performance: BST vs AVL (Author: Amoh Eric)' ) # Sets the title
    
    plt.legend() # Shows the legend
    
    plt.grid(True) # Shows the grid
    
    plt.show() # Shows the plot
    


def test_avl(n): # Tests the AVL Tree
    
    keys = random.sample(range(n * 10), n) # Generates a list of random numbers
    
    avl = AVLTree() # Creates a new AVL Tree
    
    start_time = time.time() # Starts the timer
    
    
    for key in keys: # For each key
        
        avl.insert(key) # Inserts the key into the AVL Tree
        
    insert_time = time.time() - start_time # Calculates the time taken for insertion

    start_time = time.time() # Starts the timer
    
    
    for key in keys: # For each key
        
        avl.delete(avl.root, key) # Deletes the key from the AVL Tree
        
    delete_time = time.time() - start_time # Calculates the time taken for deletion

    mem_usage = memory_profiler.memory_usage()[0] # Measures the memory usage

    return insert_time, delete_time, mem_usage # Returns the time taken for insertion, deletion, and memory usage



def run_tests_avl(): # Runs tests for the AVL Tree
    
    node_counts = [100, 1000, 10000, 100000] # Listings of node counts to test
    
    print("Measuring performance... This may take a while for larger node counts.") # Prints a message
    
print("Please wait...") # Prints a message


if __name__ == '__main__': # My Main function
    
    print("Welcome to the Tree Performance Comparison Tool!\n") # Prints a welcome message
    
    print("This tool compares the performance of Binary Search Trees (BST) and AVL Trees.\n") # Prints a description of the tool
    
    print("We will measure and plot the time taken for insertion and deletion operations for both tree types.\n") # Prints a description of the tool
    
    print("Let's get started...\n") # Prints a message

    node_counts = [100, 1000, 10000, 100000]  # Listings of node counts to test # List of node counts to test
    
    print("Measuring performance... This may take a while for larger node counts.\n") # Print a message

    print("Please wait...\n") # Prints a message

    print('AVL Tree Performance:') # Prints a message
    
    print('---------------------\n') # Prints a message
    
    print('| Num Nodes | Insert Time | Delete Time | Memory Usage |') # Prints a message
    
    print('|-----------|-------------|-------------|--------------|') # Prints a message
    

    for n in node_counts: # For each number of nodes
        
        total_insert_time = 0 # Sets the total insertion time to 0
        
        total_delete_time = 0 # Sets the total deletion time to 0
        
        total_mem_usage = 0 # Sets the total memory usage to 0
        

        for i in range(10): # For each iteration
            
            insert_time, delete_time, mem_usage = test_avl(n) # Measures the performance of the AVL Tree
            
            total_insert_time += insert_time # Adding the insertion time to the total insertion time
            
            total_delete_time += delete_time # Adds the deletion time to the total deletion time
            
            total_mem_usage += mem_usage # Adds the memory usage to the total memory usage
            

        # inserting_time, delete_time, mem_usage = test_avl(n)
        # Calculates average metrics
        avg_insert_time = total_insert_time / 5 # Calculates the average insertion time
        
        avg_delete_time = total_delete_time / 5 # Calculates the average deletion time
        
        avg_mem_usage = total_mem_usage / 5 # Calculates the average memory usage
        

        # Prints the performance metrics for the current number of nodes
        print(f'| {n:9d} | {insert_time:.6f} | {delete_time:.6f} | {mem_usage:10.4f} |') # Print the performance metrics for the current number of nodes
        
        print() # Print a new line
        
        
    # Measures BST performance
    print("\nMeasuring Binary Search Tree (BST) performance...") # Print a message
    
    bst_times = measure_performance(BinarySearchTree, node_counts) # Measures BST performance
    

    # Measures AVL performance
    print("\nMeasuring AVL Tree performance...") # Print a message
    
    avl_times = measure_performance(AVLTree, node_counts) # Measures AVL performance
    

    # Plots insertion performance
    print("\nPlotting insertion performance comparison...") # Print a message
    
    plot_performance(node_counts, bst_times, avl_times, "Insertion") # Plots the performance of the BST and AVL Tree
    

    # Plots deletion performance
    print("\nPlotting deletion performance comparison...") # Print a message
    
    plot_performance(node_counts, bst_times, avl_times, "Deletion") # Plots the performance of the BST and AVL Tree
    
    plot_performance(node_counts, bst_times, avl_times, "Insertion") # Plots the performance of the BST and AVL Tree
    
    plot_performance(node_counts, bst_times, avl_times, "Deletion") # Plots the performance of the BST and AVL Tree
    
    run_tests_avl() # Runs tests for the AVL Tree

    print("\nThank you for using the Tree Performance Comparison Tool!") # Prints a message
    
    print("For any questions or feedback, please contact the developer.") # Prints a message
