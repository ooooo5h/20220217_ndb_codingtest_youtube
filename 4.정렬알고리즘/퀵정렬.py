array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    
    # 첫번째 원소를 피벗으로 설정
    pivot = start
    left = start+1  # 오른쪽 원소 중 가장 왼쪽은 start+1
    right = end     # 오른쪽 원소 중 가장 끝은 end
    
    # 찾는 값이 엇갈리기 전(왼쪽값이 왼쪽에 있을 때까지)까지 무한반복 돌면서
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을때까지 또 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        
        if left>right: # 엇갈린 경우 작은 값과 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else : # 안엇갈리면 작은데이터 큰거 교체해야함
            array[left], array[right] = array[right], array[left]
            
    # 다 나누고 난 뒤에는 각 왼쪽 오른쪽에서 또 정렬해야함
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1)
print(array)
        