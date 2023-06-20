### Breadth first strategy(BFS) ###

graph = {
    '5': ['3', '7', '8'],
    '3': ['2', '4'],
    '7': [],
    '2': [],
    '4': ['8'],
    '8': []
    }

# list for visited nods
visited = []

# initialize a queue
queue = []

# PFS function
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    # create loop to visit each node
    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Driver code
print("Following is the Breadth-First Search")

# function calling
bfs(visited, graph, '5')