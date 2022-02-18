# 상하좌우
# 이동 후 여행자의 위치값은?
def current_location(N, plans):
    
    plans = list(plans)
        
    # 시작점
    x, y = 1, 1

    # LRUD
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L','R','U','D']
    
    # 이동계획을 하나씩 꺼내서
    for plan in plans:
        
        for i in range(len(move_types)):
            # 이동법은 4가지임
            # 이동계획과 이동법의 i번째와 동일하다면
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                   
        # 크기를 벗어나는 움직임은 무시해야한다.
        if not ((1 <= nx <= N) and (1 <= ny <= N)):
            continue   # 반복문에서 continue는 continue아래의 코드는 무시하고 지나감
        
        # 이동시키기
        x,y = nx, ny
    
    return x,y      

print(current_location(5, 'RRRUDD'))
        