# 최소 이동칸의 갯수를 출력하는 거니까 BFS 사용
from collections import deque

# 가로 세로
n,m = map(int, input().split())

# 미로 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동할 네가지 방향을 정의(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    # 큐가 빌때까지
    while queue:
        x,y = queue.popleft()
        
        # 현재 위치에서 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 찾기 공간을 벗어났으면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 괴물인 경우도 무시
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문해야지만 최단거리 기록이 된다
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    # 가장 오른쪽 아래까지의 최단거리를 반환하기
    return graph[n-1][m-1]

print(bfs(0,0))
                



    

    
    