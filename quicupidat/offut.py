def create_adjacency_list(edges):
    adjacency_list = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in adjacency_list:
            adjacency_list[node1] = []
        if node2 not in adjacency_list:
            adjacency_list[node2] = []
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)
    return adjacency_list
