# 개미전사 풀이 재구현

n = int(input('n개의 창고'))
k_array = list(map(int, input('n개의 식량 개수 입력').split()))

d = [0] * 100 # 100개까지 n이 가능함

d[0] = k_array[0]   
d[1] = max(k_array[0], k_array[1])    # 두번째 창고를 터느냐 마느냐를 위해 두 값의 최대값 구하기

for i in range(2, n):  
    d[i] = max(d[i-1], d[i-2]+k_array[i])     # 바로 앞에서 터는 양과 현재 창고까지 더한 값 중 큰값을 대입하면 된다
    
print(d[n-1])