
import time  # imports time module for measuring time taken for the operations
import random  # imports random module for generating random numbers
import matplotlib.pyplot as plt  # imports matplotlib for plotting graphs

class TreeNode:  # My Node class for BST and AVL Tree
    def __init__(self, value):
        self.value = value  # Node value
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Node height, used in AVL Tree

class BinarySearchTree:  # my Binary Search Tree Implementation
    def __init__(self):
        self.root = None  # Roots node of the BST

    def insert(self, value):  # Inserts a value into the BST
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):  # the Helper method for BST insertion
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        # Duplicates are not inserted

    def delete(self, node, value):  # Deletes a value from the BST
        if not node:
            return node
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, node.value)
        return node

    def find_min(self, node):  # Finds the node with the minimum value in BST
        while node.left:
            node = node.left
        return node

class AVLTree(BinarySearchTree):  # my AVL Tree Implementation
    def insert(self, value):  # Inserts and balance the AVL Tree
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):  # Helper method for AVL insertion with balancing
        if not node:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Balancing the tree
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, node, value):  # Deletes a value from the AVL Tree and balance
        if not node:
            return node
        elif value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        if not node:  # if the tree had only one node
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node


    # My Additional AVL methods (left_rotate, right_rotate, get_height, get_balance)
    def left_rotate(self, node):
        #Perform left rotation on the given node.
        y = node.right
        T2 = y.left

        y.left = node
        node.right = T2

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, node):
        #Performs right rotation on the given node.
        y = node.left
        T3 = y.right

        y.right = node
        node.left = T3

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        #Returns the height of the node.
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        #Returns the balance factor of the node.
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)



    def measure_performance(tree_class, node_counts):  # Measures insertion and deletion times for given tree_class and node_counts
        insertion_times = []  # Lists to store insertion times
        deletion_times = []  # Lists to store deletion times
        for count in node_counts:  # For each node count
            tree = tree_class()  # Initializes tree
            nodes = random.sample(range(count * 10), count)  # Generates random nodes

        start_time = time.time()  # Records start time
        for node in nodes:  # Inserts nodes into the tree
            tree.insert(node)
        insertion_times.append(time.time() - start_time)  # Calculates time taken and store in list

        start_time = time.time()  # Records start time
        for node in nodes:  # Deletes nodes from the tree
            tree.delete(tree.root, node)  # Adjusts as per deletion method signature
        deletion_times.append(time.time() - start_time)  # Calculates time taken and store in list
        return insertion_times, deletion_times

def plot_performance(node_counts, bst_times, avl_times, operation="Insertion"):  # Plots performance comparison between BST and AVL
    bst_insertion, bst_deletion = bst_times
    avl_insertion, avl_deletion = avl_times

    plt.figure(figsize=(10, 5))  # Sets figure size
    plt.plot(node_counts, bst_insertion if operation == "Insertion" else bst_deletion, 'o-', label='BST')  # Plots BST performance
    plt.plot(node_counts, avl_insertion if operation == "Insertion" else avl_deletion, 'x-', label='AVL')  # Plots AVL performance
    plt.xlabel('Number of Nodes')  # Sets x-axis label
    plt.ylabel(f'Time taken for {operation} (seconds)')  # Set y-axis label
    plt.xscale('log')  # Sets x-axis scale to logarithmic
    plt.yscale('log')  # Sets y-axis scale to logarithmic
    plt.title(f'{operation} Performance: BST vs AVL')  # Set plot title
    plt.legend()  # Displays legend
    plt.grid(True)  # Displays grid
    plt.show()  # Displays plot


#the measure_performance function outside of the AVLTree class

def measure_performance(tree_class, node_counts):  # Measuring insertion and deletion times for given tree_class and node_counts
    insertion_times = []  # Lists to store insertion times
    deletion_times = []  # Lists to store deletion times
    for count in node_counts:  # For each node count
        tree = tree_class()  # Initializes tree
        nodes = random.sample(range(count * 10), count)  # Generates random nodes
        start_time = time.time()  # Records start time
        for node in nodes:  # Inserts nodes into the tree
            tree.insert(node)
        insertion_times.append(time.time() - start_time)  # Calculates time taken and store in list

        start_time = time.time()  # Records start time
        for node in nodes:  # Deletes nodes from the tree
            tree.delete(tree.root, node)  # Adjusts as per deletion method signature
        deletion_times.append(time.time() - start_time)  # Calculates time taken and store in list
    return insertion_times, deletion_times



if __name__ == '__main__':

    print("Welcome to the Tree Performance Comparison Tool!")
    print("This tool compares the performance of Binary Search Trees (BST) and AVL Trees.")
    print("We will measure and plot the time taken for insertion and deletion operations for both tree types.")
    print("Let's get started...\n")

    node_counts = [100, 1000, 10000, 100000]  # Listings of node counts to test
    print("Measuring performance... This may take a while for larger node counts.")

    # Measures BST performance
    print("\nMeasuring Binary Search Tree (BST) performance...")
    bst_times = measure_performance(BinarySearchTree, node_counts)

    # Measures AVL performance
    print("\nMeasuring AVL Tree performance...")
    avl_times = measure_performance(AVLTree, node_counts)

    # Plots insertion performance
    print("\nPlotting insertion performance comparison...")
    plot_performance(node_counts, bst_times, avl_times, "Insertion")

    # Plots deletion performance
    print("\nPlotting deletion performance comparison...")
    plot_performance(node_counts, bst_times, avl_times, "Deletion")

    print("\nThank you for using the Tree Performance Comparison Tool!")
    bst_times = measure_performance(BinarySearchTree, node_counts)  # Measures BST performance
    avl_times = measure_performance(AVLTree, node_counts)  # Measures AVL performance
    plot_performance(node_counts, bst_times, avl_times, "Insertion")  # Plots insertion performance
    plot_performance(node_counts, bst_times, avl_times, "Deletion")  # Plots deletion performance
