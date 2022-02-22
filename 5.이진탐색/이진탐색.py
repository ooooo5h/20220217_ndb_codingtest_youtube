# 이진 탐색 : 정렬되어 있는 리스트에서 시작점/끝점/중간점을 이용하여 탐색범위를 절반씩 좁혀가며 탐색하는 방법

# 재귀함수를 이용하여 이진 탐색 소스 코드 구현
def binarry_search(array, target, start, end):
    if start > end :
        return None
    
    # 중간점은 소수점 날리기
    mid = (start+end)//2
    
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작으면 끝점을 왼쪽으로 옮겨주고
    elif array[mid] > target:
        return binarry_search(array, target, start, mid-1)
    
    # 중간점의 값보다 찾고자 하는 값이 크면 시작점을 오른쪽으로 이동
    else :
        return binarry_search(array, target, mid+1, end)
    
    

# 반복문 이용하여 이진 탐색 소스 코드 구현
def binarry_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        
        # 중간점의 값보다 찾는 값이 작으면 오른쪽 버리기
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid+1
    return None    

#n(원소의 개수)과 target(찾고자 하는 값)을 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

result = binarry_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)