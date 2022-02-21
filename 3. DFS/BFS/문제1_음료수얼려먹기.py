# 음료수 얼려먹기
n, m = map(int, input('N,M 입력: ').split(' '))

ice_frame = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

def count_icecream(n, m, ice_frame):
    
    find_zero = 0
    count = 0
    
    
    for x in ice_frame:
        for i in x:
            if i == 0:
                find_zero += 1
            else:
                if find_zero >= 1 :
                    count += 1
                find_zero = 0
    
    print(count)          
        
count_icecream(n,m,ice_frame)