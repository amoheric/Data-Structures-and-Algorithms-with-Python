
import time  # Importing the time module to measure performance
import random  # Importing the random module to generate random keys for insertion/deletion
import memory_profiler  # Importing the memory_profiler module to measure memory usage
import matplotlib.pyplot as plt  # imports matplotlib for plotting graphs

class Node:
    # Creating my Node class for AVL Tree nodes
    def __init__(self, key, value):
        self.value = value  # Node value
        self.key = key  # my Node's key
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.height = 1  # Height of the node in the tree

class BinarySearchTree:  # my Binary Search Tree Implementation
    def __init__(self):
        self.root = None  # Roots node of the BST

    def insert(self, key):  # Inserts a value into the BST
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):  # the Helper method for BST insertion
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = Node(value)
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

class AVLTree:
    #Creating my AVL Tree class
    def __init__(self):
        self.root = None  # Initializing the root of the AVL tree

    def Insert(self, key):
        # The Public method to insert a key into the AVL tree
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # My helper method to recursively insert a key into the tree
        if not node:
            return Node(key)  # Creating a new node if we reach a leaf

        # Recursive insertion into the left or right subtree
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            # Keys are unique, so we do not insert duplicates
            return node

        # Updates the height of the ancestor node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Getting the balance factor to check for imbalance
        balance = self._get_balance(node)

        # The performance rotations to balance the tree if necessary
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node  # Returns the (possibly unchanged) node pointer

    def Delete(self, key):
        # My public method to delete a key from the AVL tree
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # Helper method to recursively delete a key from the tree
        if not node:
            return node  # Key not found, return the node

        # Recursive deletion from the left or right subtree
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with the key found, handle deletion
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            # Node with two children, get the in-order successor (smallest in the right subtree)
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        if not node:
            return node  # In case the tree had only one node

        # Update the height of the current node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Rebalance the node if necessary
        balance = self._get_balance(node)
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node  # Return the (possibly changed) node pointer

    def Maximum(self):
        # Public method to find the maximum value (key) in the AVL tree
        if not self.root:
            return None  # Tree is empty

        current = self.root
        while current.right:
            current = current.right  # Traverse to the rightmost node

        return current.key  # Return the key of the rightmost node

    def Traverse(self, order='inorder'):
        # Public method to traverse the tree in a specified order
        if not self.root:
            return []  # Tree is empty, return an empty list

        # Call the appropriate private method based on the traversal order
        if order == 'inorder':
            return self._inorder(self.root, [])
        elif order == 'preorder':
            return self._preorder(self.root, [])
        elif order == 'postorder':
            return self._postorder(self.root, [])
        else:
            raise ValueError('Invalid traversal order')  # Raise an error for invalid order

    def _inorder(self, node, result):
        # Helper method for in-order traversal
        if node.left:
            self._inorder(node.left, result)  # Traverse the left subtree

        result.append(node.key)  # Visit the node

        if node.right:
            self._inorder(node.right, result)  # Traverse the right subtree

        return result  # Return the traversal result

    def _preorder(self, node, result):
        # Helper method for pre-order traversal
        result.append(node.key)  # Visit the node

        if node.left:
            self._preorder(node.left, result)  # Traverse the left subtree

        if node.right:
            self._preorder(node.right, result)  # Traverse the right subtree

        return result  # Return the traversal result

    def _postorder(self, node, result):
        # Helper method for post-order traversal
        if node.left:
            self._postorder(node.left, result)  # Traverse the left subtree

        if node.right:
            self._postorder(node.right, result)  # Traverse the right subtree

        result.append(node.key)  # Visit the node

        return result  # Return the traversal result

    def _get_height(self, node):
        # Helper method to get the height of a node
        if not node:
            return 0  # If the node is None, its height is 0

        return node.height  # Return the height stored in the node

    def _get_balance(self, node):
        # Helper method to get the balance factor of a node
        if not node:
            return 0  # If the node is None, its balance factor is 0

        return self._get_height(node.left) - self._get_height(node.right)  # Left height - right height

    def _rotate_left(self, node):
        # Helper method for left rotation
        right_node = node.right
        left_subtree = right_node.left

        right_node.left = node  # Make `node` the left child of `right_node`
        node.right = left_subtree  # Move `left_subtree` as the right child of `node`

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        right_node.height = 1 + max(self._get_height(right_node.left), self._get_height(right_node.right))

        return right_node  # Return the new root after rotation

    def _rotate_right(self, node):
        # Helper method for right rotation
        left_node = node.left
        right_subtree = left_node.right

        left_node.right = node  # Make `node` the right child of `left_node`
        node.left = right_subtree  # Move `right_subtree` as the left child of `node`

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        left_node.height = 1 + max(self._get_height(left_node.left), self._get_height(left_node.right))

        return left_node  # Return the new root after rotation

    def _get_min_value_node(self, node):
        # Helper method to find the node with the minimum key in the subtree rooted at `node`
        current = node
        while current.left is not None:
            current = current.left  # Keep moving to the left child

        return current  # Return the leftmost node

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

# Test and performance measurement functions follow similar logic and are corrected for AVL use.
def test_avl(num_nodes):
    """
    Test function to measure the performance of AVL tree insertions and deletions.

    Parameters:
    - num_nodes: The number of nodes to insert and then delete in the AVL tree.

    Returns:
    A tuple containing the time taken to insert all nodes, the time taken to delete all nodes, and the memory usage after the operations.
    """
    # Generate a list of random keys to insert into the AVL tree
    keys = random.sample(range(num_nodes * 10), num_nodes)

    # Create an instance of the AVLTree class
    avl = AVLTree()

    # Measure the time taken to insert all keys into the AVL tree
    start_time = time.time()
    for key in keys:
        avl.Insert(key)
    insert_time = time.time() - start_time

    # Measure the time taken to delete all keys from the AVL tree
    start_time = time.time()
    for key in keys:
        avl.Delete(key)
    delete_time = time.time() - start_time

    # Measure the memory usage of the AVL tree operations
    mem_usage = memory_profiler.memory_usage()[0]

    return insert_time, delete_time, mem_usage

def run_tests_avl():
    """
    Runs the AVL tree performance tests for different numbers of nodes and prints the results.
    """
    # Define the number of nodes for which the tests will be run
    num_nodes = [100, 1000, 10000, 100000]

    print('AVL Tree Performance:')
    print('---------------------')
    print('| Num Nodes | Insert Time | Delete Time | Memory Usage |')
    print('|-----------|-------------|-------------|--------------|')

    # Iterate over each test case (number of nodes)
    for n in num_nodes:
        total_insert_time = 0
        total_delete_time = 0
        total_mem_usage = 0

        # Run the test multiple times to get average metrics
        for i in range(5):
            insert_time, delete_time, mem_usage = test_avl(n)
            total_insert_time += insert_time
            total_delete_time += delete_time
            total_mem_usage += mem_usage

        # Calculate average metrics
        avg_insert_time = total_insert_time / 5
        avg_delete_time = total_delete_time / 5
        avg_mem_usage = total_mem_usage / 5

        # Print the performance metrics for the current number of nodes
        print(f'| {n:9d} | {avg_insert_time:.6f} | {avg_delete_time:.6f} | {avg_mem_usage:10.4f} |')

    print()

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
    # Entry point of the script: run the AVL tree performance tests
    run_tests_avl()  # Runs AVL tree performance tests

