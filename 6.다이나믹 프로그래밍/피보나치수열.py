# 피보나치 함수를 재귀함수로 구현하자
def fibo(x):
    
    # 1, 2, 3, 4, 5, ...
    # 1, 1, 2, 3, 5, ...
    
    # 피보나치 수열의 1,2번째는 1이다
    if x == 1 or x == 2:
        return 1
    
    # 그 외는 앞의 수를 더해준 값
    return fibo(x-1) + fibo(x-2)

print(fibo(2))