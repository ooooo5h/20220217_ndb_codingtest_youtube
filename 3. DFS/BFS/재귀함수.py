# 재귀함수 : 자기 자신을 다시 호출하는 함수
# 재귀함수가 무한히 호출되지 않도록, 종료조건을 포함하는게 중요

def recursive_function(i):
    # 100번째 호출을 했을 때 종료되자
    if i == 100:
        return
    print(f'{i}번째 재귀함수에서 {i+1}번째 재귀함수를 호출함')
    recursive_function(i+1)
    print(f'{i}번째 재귀함수 종료')
    
recursive_function(1)

# 재귀함수 대표 예제
# 팩토리얼 n! = 1 x 2 x 3 x ... (n-1) x n
# 반복문으로 구현
def factorial_iterative(n):
    result = 1
    
    # 1부터 n까지 수 곱하기
    for i in range(1, n+1):
        result = result * i
    return result

# 재귀적으로
def factorial_recursive(n):
    if n <= 1 : 
        return 1 # n이 1 이하인 경우 ex) 0! 1!의 값은 1
    return n * factorial_recursive(n-1)

print('반복문', factorial_iterative(5))
print('재귀함수', factorial_recursive(5))