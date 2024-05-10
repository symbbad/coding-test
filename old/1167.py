from collections import deque

V = int(input())

graph = [[] for _ in range(V+1)]


for _ in range(V):
    input_data = list(map(int, input().split()))
    head_idx = input_data[0]

    for i in range(1, len(input_data), 2):
        tail_idx = input_data[i]
        weight = input_data[i+1]
        temp = (tail_idx, weight)
        graph[head_idx].append(temp)

        if input_data[i+2] == -1:
            break

def bfs(start_node):
    visited = [-1 for _ in range(V+1)]
    que = deque()
    que.append(start_node)
    visited[start_node] = 0
    _max = [0, 0]

    while que:
        idx = que.popleft()

        for next_node, w in graph[idx]:
            if visited[next_node] == -1:
                visited[next_node] = visited[idx] + w
                que.append(next_node)
                if _max[0] < visited[next_node]:
                    _max = visited[next_node], next_node

    return _max

_, max_node = bfs(1)
max_distance, _ = bfs(max_node)

print(max_distance)