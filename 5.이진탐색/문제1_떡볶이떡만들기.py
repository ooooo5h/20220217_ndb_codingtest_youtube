# 떡볶이 떡 만들기
# 떡의 개수 n, 떡의 길이 m
n, m = map(int, input().split())
rices = list(map(int, input().split()))

start = 0
end = max(rices)
result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in rices:
        if x > mid:
            total += x - mid

    if total < m:
        # 길이를 줄여야지
        end = mid-1
    else:   # 크거나 같다
        result = mid
        start = mid + 1

print(result)
