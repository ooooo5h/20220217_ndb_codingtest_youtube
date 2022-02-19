# 왕실의 나이트

def count_cases(current_location):
    
    h = ['a','b','c','d','e','f','g','h']
    알파벳좌표로 = h.index(current_location[0])+1
    
    count = 0
    
    # R,L,U, P
    a = [0,0,-2,2]
    b = [2,-2,0,0]

    for i in range(1,9):
        for j in range(1,9):
            
            # RLUP도 반복문을 계속 돌아야 할거 같은데.. ㅠㅠ
            
            
count_cases('c2')
