# NAME: Eric Amoh Adjei
# Date: 02/10/2024
# Assignment:    Dijkstra's Graph Algorithm Implementation for Shortest Path

# I'm importing the networkx library as nx so I can use it to create and manipulate graph data structures easily.
import networkx as nx
# matplotlib.pyplot as plt is imported for plotting graphs visually, making it easier to understand their structure.
import matplotlib.pyplot as plt


# Here, I'm creating an empty graph G. This serves as the foundation upon which I'll add nodes and edges.
G = nx.Graph()


# This loop adds nodes to the graph. I'm adding 20 nodes in total, numbered 1 through 20.
for i in range(1, 21):
    G.add_node(i)


# I define a list of tuples, where each tuple represents an edge between two nodes.
edges = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
    (6, 7), (7, 8), (8, 9), (9, 10), (10, 11),
    (11, 12), (12, 13), (13, 14), (14, 15), (15, 16),
    (16, 17), (17, 18), (18, 19), (19, 20), (20, 1),
    (1, 11), (2, 12), (3, 13), (4, 14), (5, 15)
]

# Using the add_edges_from method, I add all the defined edges to the graph. This connects the nodes as specified.
G.add_edges_from(edges)


# To visualize the graph, I set up a plot with a specific figure size.
plt.figure(figsize=(10, 10))

# Then, I draw the graph with labels on the nodes and bold font weights for better visibility.
nx.draw(G, with_labels=True, font_weight='bold')

# I add a title to the plot for clarity on what is being visualized.
plt.title("A Graph Implementation with more than 20 vertices and 20 edges")

# This command displays the graph as a plot.
plt.show()


# To find the shortest path from node 1 to node 20, I use Dijkstra's algorithm provided by networkx.
shortest_path_length, shortest_path = nx.single_source_dijkstra(G, source=1, target=20)

# Then, I print the shortest path and its length to understand how these two nodes are connected in the most efficient way.
print("Shortest path from 1 to 20:", shortest_path)
print("Shortest path length:", shortest_path_length)


# For finding the Minimum Spanning Tree (MST) of the graph, I use Prim’s algorithm, again utilizing networkx's functionality.
MST = nx.minimum_spanning_tree(G)

# I set up another figure to visualize the MST, making it clear and distinct from the original graph.
plt.figure(figsize=(10, 10))

# The MST is then drawn with labels and bold fonts, just like the original graph.
nx.draw(MST, with_labels=True, font_weight='bold')

# I add a title to the plot for clarity on what is being visualized.
plt.title("Minimum Spanning Tree By Eric")

# And show the plot to display the MST.
plt.show()

# To traverse the graph using Breadth-First Search starting from node 1, I use the bfs_edges function from networkx.
bfs_order = list(nx.bfs_edges(G, 1))

# Finally, I print the order of edges visited during the BFS to show how the algorithm explores the graph.
print("BFS order starting from node 1:", bfs_order)
