# 곱하기 혹은 더해서 만들 수 있는 가장 큰 수
# 모든 연산은 왼쪽에서부터 오른쪽으로 

def add_or_multiply(S):
    
    # 결과값을 무조건 0으로 대입하지않고, 문자열의 첫번째수를 변경하여 대입해두자    
    result = int(S[0])
    
    for i in range(1, len(S)):
        
        num = int(S[i])
        
        # 두번,세번째 숫자가 0이나 1. 혹은 result가 0혹은 1이라면 더하기를 하는 게 최적의 해!!
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    
    return result

print(add_or_multiply('567'))