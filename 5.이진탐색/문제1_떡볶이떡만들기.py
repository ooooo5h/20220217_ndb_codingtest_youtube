# 떡볶이 떡 만들기
# 떡의 개수 n, 떡의 길이 m

def Count(len):
    cnt = 0
    for x in rices:
        if x <= len:
            cnt += 0
        else:
            cnt += x-len
    return cnt


n, m = map(int, input().split())   # 4 6
rices = list(map(int, input().split()))   # 19 15 10 17

# 적어도 m만큼의 떡을 집에 가져가기 위해
# 설정할 수 있는 높이의 최댓값은?    # 정답은 15

lt = 0
rt = max(rices)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
