# 컴퓨터 수 받기 - com_num
# 그래프 간선 수 받기 - n

# 그래프 맵 만들기 - graph / size n + 1 (idx = 0은 제외, 0이라는 노드는 없다고 치고 1부터 시작한다 생각해야함)
# 방문 확인 맵 만들기 - visited / size = n + 1
# 방문 횟수 변수 선언

# for n:
#     이어져 있는 노드 받기 - a, b
#     graph[a] += b
#     graph[b] += a

# def bfs:
#     que 선언
#     que에 1을 넣음
#     while que:
#         노드 1과 연결된 노드를 리스트 형식으로 que에 넣는다.
#         if 방문하지 않았으면 방문 횟수 증가
#     return 방문 횟수         


# def dfs:
#     노드 1에서 시작, 1은 방문했다고 침


from collections import deque

com_num = int(input())
n = int(input())
graph = [[] for _ in range(com_num+1)]
visited = [0]*(com_num+1)
visited[1] = 1

for _ in range(n):
    x, y = map(int, input().split())
    graph[x]+=[y]
    graph[y]+=[x]

que = deque()
que.append(1)


def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

dfs(1)
cnt = sum(visited) - 1
print(cnt)

while que:
    i = que.popleft()
    for node in graph[i]:
        if visited[node] == 0:
            que.append(node)
            visited[node] = 1
            cnt += 1

print(cnt)