import sys
input = sys.stdin.readline
INF = int(1e9)
# 무한을 의미하는 값으로 10억으로 설정

n, m = map(int,input("n과 m을 입력 : ").split())
# 노드의 개수, 간선의 개수 입력
start = int(input("시작 노드 번호 입력 : "))

graph = [[] for i in range(n+1)]
# 각 노드에 연결되어 있는 노드정보 리스트 생성
visited = [False] * (n+1)
# 방문체크 리스트 생성
distance = [INF] * (n+1)
#최단 거리 테이블 초기화

for _ in range(m):
    #모든간선정보 입력
    a,b,c = map(int,input().split())
    # node a 에서 node b 로 가는 비용이 c
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    #가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if(distance[i] < min_value and not visited[i]):
            min_value = distance[i]
            index = i
    return index
    