n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a의 작은 수들을 b의 큰수로 바꿔주면 됨. 
# 정렬이 필요하다. a는 작은수대로, b는 큰수부터
a.sort()  
b.sort(reverse=True)

# k번만큼만 바꿀 수 있음
for i in range(k):
    # a가 더 작으면 바꾸고
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    # 같거나 크면 안바꾸기
    else:
        break

print(sum(a))