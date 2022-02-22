# 정렬되어있는 n개의 원소를 포함한 수열에 등장하는 x의 횟수 

from bisect import bisect_left, bisect_right

# array에서 x부터 y까지의 개수를 세는 함수
def count_by_range(array, x, y):
    count_right = bisect_right(array, x)
    count_left = bisect_left(array, y)
    return count_right - count_left

n, x = map(int, input().split())
list = list(map(int, input().split()))

count = count_by_range(list, x, x)

if count == 0:
    print(-1)
else:
    print(count)