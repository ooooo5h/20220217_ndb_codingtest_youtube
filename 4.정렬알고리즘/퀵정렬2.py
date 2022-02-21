array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1 :
        return array
    
    # 첫번째 원소를 피벗으로 설정
    pivot = array[0]
    # 피벗 제외한 리스트를 테일로 설정
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]  # 왼쪽 부분에서 피벗보다 작다면
    right_side = [x for x in tail if x > pivot]  # 오른쪽 부분
    
    # 왼쪽과 오른쪽에서 각각 정렬을 수행한 뒤에, 전체 리스트를 리턴
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array)) 