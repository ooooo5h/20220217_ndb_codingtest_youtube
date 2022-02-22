# 정렬되어있는 n개의 원소를 포함한 수열에 등장하는 x의 횟수 

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# n: 데이터의 개수 , x : 찾고자 하는 값
n,x = map(int, input().split())
numbers = list(map(int, input().split()))

# x부터 x까지의 개수 => x의 총 갯수 구하기
count = count_by_range(numbers, x, x)

if count == 0:
    print(-1)
else:
    print(count)