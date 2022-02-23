# 정수 n입력
n = int(input())

# 식량 정보 입력받기
array = list(map(int, input().split()))

# 계산된 결과를 저장하기 위한 DP테이블 0으로 초기화
d = [0] * 100

# 바텀업 다이나믹 프로그래밍 진행
d[0] = array[0]
d[1] = max(array[0], array[1])  # d[1]은 한개의 값만 골라야 함! 중복 노노

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])
    
print(d[n-1])