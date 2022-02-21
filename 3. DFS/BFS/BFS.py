# Breath First Search, 너비 우선 탐색으로 그래프에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 큐 자료구조를 이용

# BFS 메소드 정의(큐의 구현은 deque 라이브러리를 사용할것)
from collections import deque

def bfs(graph, start, visited):
    
    # deque? : double ended que 큐의 앞/뒤에서 삽입/삭제가 가능한 큐 
    queue = deque([start])
    
    # 현재 노드 방문처리
    visited[start] = True
    
    # 큐가 빌때까지 반복하자
    while queue:
        # 큐에서 하나씩 원소를 뽑아서 출력해보기
        v = queue.popleft()
        print(v, end='')
        
        # 아직 방문안한 인접한 원소들은 큐에 삽입해야함
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    
# 각 노드가 연결된 정보를 2차원 리스트로 표현하기
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#  각 노드가 방문된 정보를 1차원 리스트로 표현하기
visited = [False] * 9


bfs(graph, 1, visited)

