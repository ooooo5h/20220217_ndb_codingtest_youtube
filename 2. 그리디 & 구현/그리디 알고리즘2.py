# 곱하기 혹은 더해서 만들 수 있는 가장 큰 수
# 모든 연산은 왼쪽에서부터 오른쪽으로 

def add_or_multiply(S):
    
    a = list(map(int, S))
    
    result = 0
    
    for i in range(len(S)):
        if a[i-1] == 0:
            result += a[i]
        else:
            result *= a[i]
    
    return result
    

print(add_or_multiply('567'))
# 틀린 코드
# 02984는 제대로 정답이 나오지만
# 567이면 0 * 5 = 0. 정답이 0으로 계속 리턴이 된다.