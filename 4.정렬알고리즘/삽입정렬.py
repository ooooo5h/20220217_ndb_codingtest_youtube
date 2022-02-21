array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    
    # 삽입정렬은 왼쪽의 수와 비교해서 작다면 왼쪽으로, 크다면 오른쪽으로 이동시킴
    for j in range(i, 0, -1):
        # 한 칸씩 왼쪽으로 이동ㅇ시켜야함
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            # 나보다 작은 숫자를 만나면 스톱
            break
    
print(array)