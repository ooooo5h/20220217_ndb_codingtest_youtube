# 떡볶이 떡 만들기
# n은 떡의 개수, m은 요청한 떡의 길이
n, m = list(map(int,input().split()))

# 각 떡의 개별 높이 입력
array = list(map(int,input().split()))

start = 0   # 시작점
end = max(array)  # 끝점은 떡 중 제일 긴 떡의 값으로 설정
result = 0  # m의 떡을 주기 위한 떡높이의 최대값

while start<= end:  # 시작점이 끝점보다 작을때만 코드 실행!
    total = 0  # m에 달성했는지 확인해줄 값
    mid = (start+end)//2  # 소수점을 날려준 중간값 설정
    
    for x in array:   # 떡을 하나 씩 꺼내면서 비교하기
        if x > mid:   # 꺼낸 떡의 길이가 중간값(커팅값)보다 크다면 떡이 잘리게됨.
            total += x-mid   # 꺼낸 떡을 자르고난 나머지를 손님이 가져가므로, 토탈에 합산해주기
            
    if total < m:  # 이제까지 자른 떡의 총 합이, 손님이 요청한 값 보다 작다면 더 많이 잘라야하기 때문에 끝점을 이동시켜서 더 자르기
        end = mid-1
        
    else:      # 떡의 총합이 요청한 떡 길이보다 같거나 크다면
        result = mid   # 충족했으므로 중간값을 최대값에 대입해주고
        start = mid+1  # 시작점을 좁혀나가주기
        
print(result)