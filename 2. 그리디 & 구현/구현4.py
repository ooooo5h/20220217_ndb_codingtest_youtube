# 왕실의 나이트

def count_cases(current_location):
    
    h = ['a','b','c','d','e','f','g','h']
    
    row = int(current_location[1])
    column = h.index(current_location[0])+1
    
    # R,L,U,D
    # 이동할 수 있는 8가지 방향을 한줄로 정리해도 된다
    steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1)]
        
    count = 0
    
    # 현재 위치를 이동할 수 있는 방향으로 이동시키기
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        
        # 범위 안에 들어온다면 카운트 해주면 됨
        if 1 <= next_row <= 8 and 1 <=next_column <= 8:
            count += 1

    return count
            
print(count_cases('a1'))
