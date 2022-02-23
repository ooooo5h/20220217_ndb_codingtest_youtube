# 병사 배치하기..
# 다이나믹 프로그래밍 문제 다 못풀었다 ㅠ_ ㅠ 어려워라

n = int(input())
array = list(map(int, input().split()))

# 순서를 뒤집어서 최장 증가하는 부분 수열 문제로 변환시키기
array.reverse()

dp = [1]*n
# 가장 긴 증가하는 부분 수열 알고리즘 작성
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
# 최소 수 출력
print(n - max(dp))