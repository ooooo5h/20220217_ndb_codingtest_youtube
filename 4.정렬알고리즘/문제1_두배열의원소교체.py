n,k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()   # a의 작은수를 b의 큰수와 바꾸면 되기 때문에 a는 작은수대로 정렬하고, b는 큰수대로 정렬
b.sort(reverse=True)

# 첫번째 인덱스부터 확인해나가면서 두배열의 원소를 k번까지 비교해야함
for i in range(k):
    # a의 원소가 b원소보다 작으면 교환
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
        
    # a의 원소가 b원소보다 크거나 같으면 반복문 탈출
    else:
        break
    
print(sum(a))