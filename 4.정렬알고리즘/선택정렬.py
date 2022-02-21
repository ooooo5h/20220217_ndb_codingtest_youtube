array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    
    # 가장 작은 원소의 인덱스
    min_index = i
    
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            
            # 더 작은 인덱스값으로 변경
            min_index = j
    
    # 자리 바꾸기
    array[i], array[min_index] = array[min_index], array[i]

print(array)