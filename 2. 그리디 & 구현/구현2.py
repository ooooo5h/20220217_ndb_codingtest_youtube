# 상하좌우
# 이동 후 여행자의 위치값은?
def current_location(N, plan):
    
    plan = list(plan)
        
    # 시작점
    x, y = 1, 1

    # LRUD
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for letter in plan:
        
        # 크기를 벗어나는 움직임은 무시해야한다.
        if not ((1 <= x <= N) or (1 <= y <= N)):
            pass            
        
        # 이동해야하는 설명서의 길이만큼 이동시키기           
        if letter == 'L':
            x = x + dx[0]
            y = y + dy[0]
        elif letter == 'R':
            x = x + dx[1]
            y = y + dy[1]
        elif letter == 'U':
            x = x + dx[2]
            y = y + dy[2]
        elif letter == 'D':
            x = x + dx[3]
            y = y + dy[3]
    
    return x,y      

print(current_location(5, 'RRRUDD'))
        