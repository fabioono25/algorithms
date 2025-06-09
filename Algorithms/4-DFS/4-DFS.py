# Algorithms/4-DFS/4-DFS.py

# Graph representation: Adjacency List (dictionary where keys are nodes and values are lists of neighbors)
# Example graph:
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

# --- Simple Solution (Recursive DFS) ---
def dfs_simple_recursive(graph, start_node, visited=None):
    """
    Simple recursive Depth First Search.
    Explores as far as possible along each branch before backtracking.

    Args:
        graph (dict): Adjacency list representation of the graph.
        start_node: The node to begin traversal from.
        visited (set, optional): A set to keep track of visited nodes.
                                 Initialized to None for the first call.

    Returns:
        list: A list of nodes in DFS traversal order.
    """
    if visited is None:
        visited = set()

    path = []
    # Only proceed if start_node is a valid node in the graph
    if start_node in graph: # Check if node exists in graph keys
        if start_node not in visited:
            visited.add(start_node)
            path.append(start_node)
            # If start_node is confirmed to be in graph, graph[start_node] should be safe.
            # Using graph.get still adds robustness if a node could exist as a key
            # but its value (list of neighbors) is missing, though that's unusual for adjacency lists.
            for neighbor in graph.get(start_node, []):
                # Recursive calls will correctly handle if a neighbor isn't a key in the graph
                # (it will result in an empty path extension from that recursive call).
                if neighbor not in visited: # This check is vital
                    path.extend(dfs_simple_recursive(graph, neighbor, visited))
    # If start_node is not in graph (e.g., 'X' or graph is {}), path remains empty.
    return path

# --- Robust Solution (Handling Disconnected Graphs, Cycle Detection Aid) ---
def dfs_robust_iterative_all_nodes(graph):
    """
    More robust DFS that handles disconnected graphs by iterating through all nodes.
    Uses an iterative approach with an explicit stack.
    Can be adapted to detect cycles by tracking nodes currently in the recursion stack (path_stack).

    Args:
        graph (dict): Adjacency list representation of the graph.

    Returns:
        dict: A dictionary where keys are start nodes of DFS traversals
              and values are lists of nodes in DFS order for that component.
              Also includes a 'visited_nodes' key with a set of all visited nodes.
    """
    visited_overall = set()
    paths_from_components = {}

    for node in graph:
        if node not in visited_overall:
            # Start a new DFS traversal for an unvisited component
            path_component = []
            stack = [(node, iter(graph.get(node, [])))] # (node, iterator for its neighbors)
            visited_component = set() # Visited nodes in the current DFS tree

            visited_overall.add(node)
            visited_component.add(node)
            path_component.append(node)

            # path_stack for cycle detection (nodes currently in recursion path for this traversal)
            # For cycle detection: if we encounter a node in path_stack, it's a back edge -> cycle.
            # This example focuses on traversal, so cycle detection logic is commented but can be added.
            # path_stack = {node}

            while stack:
                current_node, children_iter = stack[-1]

                try:
                    child = next(children_iter)
                    if child not in visited_overall:
                        visited_overall.add(child)
                        visited_component.add(child)
                        path_component.append(child)
                        # path_stack.add(child)
                        stack.append((child, iter(graph.get(child, []))))
                    # elif child in path_stack:
                    #     print(f"Cycle detected: back edge from {current_node} to {child}")

                except StopIteration:
                    # path_stack.remove(current_node) # Remove when backtracking
                    stack.pop()
            paths_from_components[node] = path_component

    return {"traversals": paths_from_components, "visited_nodes": visited_overall}

# --- Jedi Solution (Applications and Iterative DFS with Discovery/Finish Times) ---
# Iterative DFS that also calculates discovery and finish times.
# Useful for applications like topological sorting or finding strongly connected components.

time_dfs = 0 # Global timer for discovery/finish times
discovery_time = {}
finish_time = {}
parent_dfs = {}

def dfs_jedi_iterative_with_times(graph):
    """
    Iterative DFS that calculates discovery and finish times for each node.
    Handles disconnected graphs.

    Args:
        graph (dict): Adjacency list.

    Returns:
        tuple: (discovery_time_map, finish_time_map, parent_map)
    """
    # Declare global variables before any assignment or use within this function's scope
    global time_dfs, discovery_time, finish_time, parent_dfs

    time_dfs = 0 # Initialize global timer
    # Initialize global dictionaries for results specific to this call
    discovery_time = {node: 0 for node in graph}
    finish_time = {node: 0 for node in graph}
    parent_dfs = {node: None for node in graph}
    visited_jedi = set()

    all_nodes = list(graph.keys()) # Iterate in a fixed order for predictability if needed

    for node_start_component in all_nodes:
        if node_start_component not in visited_jedi:
            # Stack stores tuples: (vertex, state)
            # state = 0 means just discovered, process neighbors
            # state = 1 means all neighbors processed, finishing
            stack = [(node_start_component, 0)]
            visited_jedi.add(node_start_component)

            time_dfs += 1 # time_dfs is already global
            discovery_time[node_start_component] = time_dfs

            while stack:
                u, state = stack[-1]

                if state == 0: # Just discovered u, process its neighbors
                    # Change state to 1, so next time we see it, we finish it
                    stack[-1] = (u, 1)

                    # Process neighbors in reverse order to mimic recursion closely if desired
                    # for v in reversed(graph.get(u, [])):
                    for v in graph.get(u, []):
                        if v not in visited_jedi:
                            visited_jedi.add(v)
                            parent_dfs[v] = u
                            time_dfs += 1
                            discovery_time[v] = time_dfs
                            stack.append((v, 0))
                else: # state == 1, finished processing u's children
                    stack.pop()
                    time_dfs += 1
                    finish_time[u] = time_dfs

    return discovery_time, finish_time, parent_dfs

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Simple Recursive DFS ---")
    # Test with a connected component
    path_simple_A = dfs_simple_recursive(graph_example, 'A')
    print(f"DFS from 'A': {path_simple_A}")
    # Test with another component to show it only traverses connected part
    path_simple_G = dfs_simple_recursive(graph_example, 'G')
    print(f"DFS from 'G': {path_simple_G}")
    # Test with a non-existent node
    path_simple_X = dfs_simple_recursive(graph_example, 'X')
    print(f"DFS from 'X' (non-existent): {path_simple_X}")
    # Test with an empty graph
    print(f"DFS on empty graph: {dfs_simple_recursive({}, 'A')}")

    print("\n--- Robust Iterative DFS (All Nodes) ---")
    robust_result = dfs_robust_iterative_all_nodes(graph_example)
    print("Traversal Paths:")
    for start_node, path in robust_result["traversals"].items():
        print(f"  Starting from {start_node}: {path}")
    print(f"All visited nodes: {robust_result['visited_nodes']}")
    # Test with an empty graph
    print(f"Robust DFS on empty graph: {dfs_robust_iterative_all_nodes({})}")

    print("\n--- Jedi Iterative DFS with Discovery/Finish Times ---")
    # Reset global state for Jedi DFS if running multiple times (important for testing)
    time_dfs = 0
    discovery_time = {}
    finish_time = {}
    parent_dfs = {}
    d_times, f_times, p_map = dfs_jedi_iterative_with_times(graph_example)
    print("Discovery Times:", dict(sorted(d_times.items())))
    print("Finish Times:", dict(sorted(f_times.items())))
    print("Parent Map:", dict(sorted(p_map.items())))

    print("\nApplications of DFS (Conceptual - based on Jedi DFS):")
    print("1. Topological Sort (for a DAG): Nodes sorted by decreasing finish times.")
    # Example: if graph_example was a DAG, list nodes by f_times in reverse.
    # For a general graph, this isn't a valid topo sort if cycles exist.
    # A proper topo sort would also require cycle detection.

    # Create a DAG for topological sort example
    dag_example = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    time_dfs = 0; discovery_time = {}; finish_time = {}; parent_dfs = {} # Reset
    dt_dag, ft_dag, p_dag = dfs_jedi_iterative_with_times(dag_example)
    # Sort nodes by finish times in descending order for topological sort
    topological_order = sorted(ft_dag.keys(), key=lambda node: ft_dag[node], reverse=True)
    # Filter out nodes with finish time 0 if graph was disconnected and only part processed
    topological_order_filtered = [node for node in topological_order if ft_dag[node] > 0]
    print(f"Topological Sort of DAG ({dag_example}): {topological_order_filtered}")

    print("2. Finding Connected Components: Each DFS traversal from the main loop in dfs_robust_iterative_all_nodes or dfs_jedi_iterative_with_times identifies a component.")
    print("3. Cycle Detection: Can be added to iterative DFS by checking if a neighbor is in the current 'recursion' stack (path_stack).")
