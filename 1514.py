
def create_weighted_adjacency_list(edges, weights, n):
    adjacency_list = [[] for _ in range(n)]
    for (a, b), weight in zip(edges, weights):
        adjacency_list[a].append([b, weight])
        adjacency_list[b].append([a, weight])
    return adjacency_list


edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]]
weights = [0.5, 0.1, 0.5, 0.5, 0.9]
n = 4

weighted_adjacency_list = create_weighted_adjacency_list(edges, weights, n)

for i, neighbors in enumerate(weighted_adjacency_list):
    print(f"Node {i}: {neighbors}")
