import time
import random
import matplotlib.pyplot as plt
import memory_profiler

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
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

    def delete(self, node, value):
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

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

class AVLTree(BinarySearchTree):
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
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

    def delete(self, node, value):
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

        if not node:
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

    def left_rotate(self, node):
        y = node.right
        T2 = y.left

        y.left = node
        node.right = T2

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, node):
        y = node.left
        T3 = y.right

        y.right = node
        node.left = T3

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

def measure_performance(tree_class, node_counts):
    insertion_times = []
    deletion_times = []
    for count in node_counts:
        tree = tree_class()
        nodes = random.sample(range(count * 10), count)
        start_time = time.time()
        for node in nodes:
            tree.insert(node)
        insertion_times.append(time.time() - start_time)

        start_time = time.time()
        for node in nodes:
            tree.delete(tree.root, node)
        deletion_times.append(time.time() - start_time)
    return (insertion_times, deletion_times)

def plot_performance(node_counts, bst_times, avl_times, operation="Insertion"):
    plt.figure(figsize=(10, 5))
    if operation == "Insertion":
        plt.plot(node_counts, bst_times[0], 'o-', label='BST')
        plt.plot(node_counts, avl_times[0], 'x-', label='AVL')
    else:
        plt.plot(node_counts, bst_times[1], 'o-', label='BST')
        plt.plot(node_counts, avl_times[1], 'x-', label='AVL')
    plt.xlabel('Number of Nodes')
    plt.ylabel(f'Time taken for {operation} (seconds)')
    plt.xscale('log')
    plt.yscale('log')
    plt.title(f'{operation} Performance: BST vs AVL')
    plt.legend()
    plt.grid(True)
    plt.show()

def test_avl(n):
    keys = random.sample(range(n * 10), n)
    avl = AVLTree()
    start_time = time.time()
    for key in keys:
        avl.insert(key)
    insert_time = time.time() - start_time

    start_time = time.time()
    for key in keys:
        avl.delete(avl.root, key)
    delete_time = time.time() - start_time

    mem_usage = memory_profiler.memory_usage()[0]

    return insert_time, delete_time, mem_usage

def run_tests_avl():
    node_counts = [100, 1000, 10000, 100000]
    print("Measuring performance... This may take a while for larger node counts.")

if __name__ == '__main__':
    print("Welcome to the Tree Performance Comparison Tool!\n")
    print("This tool compares the performance of Binary Search Trees (BST) and AVL Trees.\n")
    print("We will measure and plot the time taken for insertion and deletion operations for both tree types.\n")
    print("Let's get started...\n")

    node_counts = [100, 1000, 10000, 100000]  # Listings of node counts to test
    print("Measuring performance... This may take a while for larger node counts.\n")

    print("Please wait...\n")

    print('AVL Tree Performance:')
    print('---------------------\n')
    print('| Num Nodes | Insert Time | Delete Time | Memory Usage |')
    print('|-----------|-------------|-------------|--------------|')

    for n in node_counts:
        total_insert_time = 0
        total_delete_time = 0
        total_mem_usage = 0
        for i in range(10):
            insert_time, delete_time, mem_usage = test_avl(n)
            total_insert_time += insert_time
            total_delete_time += delete_time
            total_mem_usage += mem_usage
        #insert_time, delete_time, mem_usage = test_avl(n)

        # Calculate average metrics
        avg_insert_time = total_insert_time / 5
        avg_delete_time = total_delete_time / 5
        avg_mem_usage = total_mem_usage / 5

        # Print the performance metrics for the current number of nodes
        print(f'| {n:9d} | {insert_time:.6f} | {delete_time:.6f} | {mem_usage:10.4f} |')
        print()
        
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
    plot_performance(node_counts, bst_times, avl_times, "Insertion")
    plot_performance(node_counts, bst_times, avl_times, "Deletion")
    run_tests_avl()

    print("\nThank you for using the Tree Performance Comparison Tool!")
    print("For any questions or feedback, please contact the developer.")