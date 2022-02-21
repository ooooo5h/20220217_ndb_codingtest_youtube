# 음료수 얼려먹기
# N, M을 공백 기준으로 구분해서 입력받기
n,m = map(int, input().split())

# 2차원 리스트의 맵 정보를 입력받기
graph = []
for i in range(n):  # N이 가로니까 가로 왼쪽에서 부터 값 입력하기
    graph.append(list(map(int, input())))
    

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문하는 함수 생성
def dfs(x,y) :
    
    # 주어진 범위를 벗어나는 경우 즉시 종료시키기
    # 어떤 범위를 벗어난다는 거지...?
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드 방문하지 않았다면 찾아가서 방문처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1, y)  # 상
        dfs(x+1, y)  # 하
        dfs(x, y-1)  # 좌
        dfs(x, y+1)  # 우의 위치들도 재귀적으로 호출하여 방문처리
        return True
    
    return False  # 결과값을 트루, 펄스로...?왜?



# 모든 노드에 대하여 음료수를 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:   # 트루면 왜 1을 체크하는거지..?
            result += 1
            
print(result)
