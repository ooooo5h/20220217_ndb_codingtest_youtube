# 음료수 얼려먹기
n, m = map(int, input('N,M 입력: ').split(' '))

# 일단 아이스프레임도 이 값이 고정이 아니라 변경되어야함
ice_frame = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

# 모르겠는 부분
# n,m을 어떻게 활용해야하는지
# 위아래로 붙은 0들을 어떻게 연결..?ㅎㄷㄷ
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