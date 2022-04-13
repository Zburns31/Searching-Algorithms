from collections import deque


# graph is in adjacency list form
# graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
graph = {
    "1": ["2", "3", "4"],
    "2": ["5", "6"],
    "5": ["9", "10"],
    "4": ["7", "8"],
    "7": ["11", "12"],
}


def backtrace(parent, start, end):
    """ Given a dictionary of parent nodes, backtrace from the end node to the start node

        Parameters:
            parent (dict): A dictionary of parent nodes
            start (str): The starting node
            end (str): The ending node
    """
    # Start with the end node
    path = [end]

    # While we backtrack through the graph, appent the parent node to the path
    while path[-1] != start:
        parent_node = parent[path[-1]]
        path.append(parent_node)

    path.reverse()

    return path


# TODO: Track depth of the Graph/Tree: https://stackoverflow.com/questions/31247634/how-to-keep-track-of-depth-in-breadth-first-search
def BFSearch(graph, start, end):
    """ Implement Breadth First Search

        Parameters:
            graph (dict): A graph represented as a dictionary
            s (str): The starting node
    """
    # Keep track of visited nodes
    visited = []
    parent = {}
    distance = 0

    # Create a queue and enqueue the starting node
    nodes = deque()
    nodes.append(start)

    visited.append(start)

    # Loop through nodes until no more in the queue
    while nodes:

        # Dequeue the first node
        current_node = nodes.popleft()  # Dequeue the first node
        # If we have reached the end, return backtrace from the end node to the start
        if current_node == end:
            return backtrace(parent, start, end)

        print(f"Visiting node: {current_node} with distance: {distance}")

        # For each adjacent node in the graph, if it has not been visited, enqueue it
        for adj_node in graph.get(current_node, []):
            if adj_node not in visited:
                parent[adj_node] = current_node
                nodes.append(adj_node)
                visited.append(adj_node)


BFSearch(graph, "1", "11")


# TODO: Shortest Path of a Weighted Graph
