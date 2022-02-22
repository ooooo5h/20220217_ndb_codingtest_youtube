# bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))


# 이를 활용할 수 있음
# bisect라이브러리를 활용하여 값이 특정 범위에 해당하는 데이터 개수 구하는 함수 
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    return right_index - left_index

b = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(b, 4,4))

# 값이 -1 ~ 3 사이의 데이터 개수 출력
print(count_by_range(b, -1,3))