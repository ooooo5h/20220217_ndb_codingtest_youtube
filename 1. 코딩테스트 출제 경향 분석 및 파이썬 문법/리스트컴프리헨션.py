# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
# 1. 일반 코드
a = []

for i in range(20):
    if i % 2 == 1:
        a.append(i)
print('일반', a)        

# 2. 리스트 컴프리헨션
a_list = [i for i in range(0, 20) if i % 2 == 1]
print('홀수', a_list)


# 1부터 9까지의 수들의 제곱값을 포함하는 리스트
b_list = [i*i for i in range(1, 10)]
print('제곱값', b_list)

