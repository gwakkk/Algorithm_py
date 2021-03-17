from collections import deque

n, m = map(int, input("n과 m을 입력 : ").split())

graph = []

for i in range(n):
    graph.append(list(map(int, input("미로 정보 입력 : "))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간을 벗어나는 경우
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            # 벽인 경우에는 무시한다
            if(graph[nx][ny] == 0):
                continue 
            # 처음 방문하는 노드의 경우 최단거리 기록
            if (graph[nx][ny] == 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))