# 상하좌우
# 이동 후 여행자의 위치값은?
def current_location(N, plans):

    plans = list(plans)
    
    x,y = 1,1
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    directions = ['L', 'R', 'U', 'D']
    
    for plan in plans:
        for i in range(len(directions)):
            if plan == directions[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if not (1<=nx<=5 and 1<=ny<=5):
            continue
        x,y = nx, ny
    return x, y

print(current_location(5, 'RRRUDD'))
        