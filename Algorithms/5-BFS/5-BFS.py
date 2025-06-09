# Algorithms/5-BFS/5-BFS.py
from collections import deque

# Example graph (same as DFS for consistency in examples)
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['H'], # Another component
    'H': ['G']
}

# --- Simple Solution (Iterative BFS using a queue) ---
def bfs_simple_iterative(graph, start_node):
    """
    Simple iterative Breadth First Search.
    Explores the graph layer by layer.

    Args:
        graph (dict): Adjacency list representation of the graph.
        start_node: The node to begin traversal from.

    Returns:
        list: A list of nodes in BFS traversal order from the start_node.
              Returns an empty list if start_node is not in graph.
    """
    if not graph or start_node not in graph:
        return []

    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    path = []

    while queue:
        current_node = queue.popleft()
        path.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return path

# --- Robust Solution (Handles Disconnected Graphs, Path Finding) ---
def bfs_robust_all_nodes_with_paths(graph):
    """
    More robust BFS that handles disconnected graphs by iterating through all nodes.
    Also reconstructs the shortest path from a start node to all other nodes
    in its connected component and records distances.

    Args:
        graph (dict): Adjacency list.

    Returns:
        dict: Contains 'traversals' (dict of component_start_node: bfs_path),
              'paths_and_distances' (dict of component_start_node: {node: (path_to_node, distance)}),
              and 'visited_nodes' (set of all visited nodes).
    """
    visited_overall = set()
    results = {
        "traversals": {},
        "paths_and_distances": {},
        "visited_nodes": set()
    }

    for node in graph:
        if node not in visited_overall:
            # Start a new BFS for an unvisited component
            component_bfs_path = []
            component_paths_dist = {}

            queue = deque([(node, [node], 0)]) # (current_node, path_to_current_node, distance)
            visited_component = {node} # Visited nodes in the current BFS tree

            visited_overall.add(node)
            component_paths_dist[node] = ([node], 0)

            while queue:
                current_node, path_so_far, dist_so_far = queue.popleft()
                component_bfs_path.append(current_node)

                for neighbor in graph.get(current_node, []):
                    if neighbor not in visited_component:
                        visited_component.add(neighbor)
                        visited_overall.add(neighbor)
                        new_path = path_so_far + [neighbor]
                        component_paths_dist[neighbor] = (new_path, dist_so_far + 1)
                        queue.append((neighbor, new_path, dist_so_far + 1))

                results["traversals"][node] = component_bfs_path
                results["paths_and_distances"][node] = component_paths_dist

    results["visited_nodes"] = visited_overall
    return results

# --- Jedi Solution (Bidirectional BFS for Shortest Path, Applications) ---
# Bidirectional BFS is typically used for finding the shortest path between two specific nodes.
# It runs BFS from both start and end nodes simultaneously.
def bidirectional_bfs_shortest_path(graph, start_node, end_node):
    """
    Finds the shortest path between start_node and end_node using Bidirectional BFS.

    Args:
        graph (dict): Adjacency list.
        start_node: The starting node.
        end_node: The target node.

    Returns:
        list: The shortest path from start_node to end_node.
              Returns None if no path exists or nodes are invalid.
    """
    if start_node not in graph or end_node not in graph:
        return None
    if start_node == end_node:
        return [start_node]

    # Queue and visited set for BFS starting from start_node
    q_start = deque([(start_node, [start_node])]) # (node, path)
    visited_start = {start_node: [start_node]}  # node -> path

    # Queue and visited set for BFS starting from end_node
    q_end = deque([(end_node, [end_node])]) # (node, path)
    visited_end = {end_node: [end_node]}    # node -> path (path is reversed from end)

    while q_start and q_end:
        # Expand from start_node's BFS
        if q_start: # Check if queue is not empty before pop
            current_s, path_s = q_start.popleft()
            for neighbor_s in graph.get(current_s, []):
                if neighbor_s not in visited_start:
                    new_path_s = path_s + [neighbor_s]
                    visited_start[neighbor_s] = new_path_s
                    q_start.append((neighbor_s, new_path_s))
                    # Check for intersection
                    if neighbor_s in visited_end:
                        path_e_reversed = visited_end[neighbor_s]
                        return new_path_s + path_e_reversed[-2::-1] # Combine paths

        # Expand from end_node's BFS
        if q_end: # Check if queue is not empty before pop
            current_e, path_e = q_end.popleft() # path_e is reversed
            for neighbor_e in graph.get(current_e, []):
                if neighbor_e not in visited_end:
                    new_path_e = path_e + [neighbor_e]
                    visited_end[neighbor_e] = new_path_e
                    q_end.append((neighbor_e, new_path_e))
                    # Check for intersection
                    if neighbor_e in visited_start:
                        path_s_direct = visited_start[neighbor_e]
                        return path_s_direct + new_path_e[-2::-1] # Combine paths
    return None # No path found

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Simple Iterative BFS ---")
    path_simple_A = bfs_simple_iterative(graph_example, 'A')
    print(f"BFS from 'A': {path_simple_A}")
    path_simple_G = bfs_simple_iterative(graph_example, 'G')
    print(f"BFS from 'G': {path_simple_G}")
    print(f"BFS from 'X' (non-existent): {bfs_simple_iterative(graph_example, 'X')}")
    print(f"BFS on empty graph: {bfs_simple_iterative({}, 'A')}")

    print("\n--- Robust BFS (All Nodes, Paths & Distances) ---")
    robust_results = bfs_robust_all_nodes_with_paths(graph_example)
    print("Component Traversals:")
    for start_n, path_r in robust_results["traversals"].items():
        print(f"  BFS from {start_n}: {path_r}")
    print("Paths and Distances from component start nodes:")
    for start_n, data in robust_results["paths_and_distances"].items():
        print(f"  For component starting at {start_n}:")
        for target_n, (p, d) in data.items():
            print(f"    To {target_n}: path={p}, distance={d}")
    print(f"Robust BFS on empty graph: {bfs_robust_all_nodes_with_paths({})}")


    print("\n--- Jedi Bidirectional BFS (Shortest Path) ---")
    # Path from A to F
    shortest_A_F = bidirectional_bfs_shortest_path(graph_example, 'A', 'F')
    print(f"Shortest path from A to F: {shortest_A_F}") # Expected: ['A', 'C', 'F'] or ['A', 'B', 'E', 'F']

    # Path from A to D
    shortest_A_D = bidirectional_bfs_shortest_path(graph_example, 'A', 'D')
    print(f"Shortest path from A to D: {shortest_A_D}") # Expected: ['A', 'B', 'D']

    # Path within another component G to H
    shortest_G_H = bidirectional_bfs_shortest_path(graph_example, 'G', 'H')
    print(f"Shortest path from G to H: {shortest_G_H}") # Expected: ['G', 'H']

    # No path (A to G are disconnected)
    shortest_A_G = bidirectional_bfs_shortest_path(graph_example, 'A', 'G')
    print(f"Shortest path from A to G (disconnected): {shortest_A_G}") # Expected: None

    # Start node equals end node
    shortest_A_A = bidirectional_bfs_shortest_path(graph_example, 'A', 'A')
    print(f"Shortest path from A to A: {shortest_A_A}") # Expected: ['A']

    # Non-existent node
    shortest_A_X = bidirectional_bfs_shortest_path(graph_example, 'A', 'X')
    print(f"Shortest path from A to X (X non-existent): {shortest_A_X}") # Expected: None

    print("\nApplications of BFS (Conceptual):")
    print("1. Shortest Path in Unweighted Graphs: BFS is guaranteed to find the shortest path in terms of number of edges.")
    print("2. Finding Connected Components: Similar to DFS, iterating BFS from unvisited nodes finds all components.")
    print("3. Level Order Traversal of a Tree: BFS naturally traverses a tree level by level.")
    print("4. Network Broadcasting: Simulating packet propagation in a network.")
