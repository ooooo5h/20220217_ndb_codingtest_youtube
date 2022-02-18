# 그리디 알고리즘 : 현재 상황에서 지금 당장 좋은것만 고르는 방법

# 문제 : 1이 될 때 까지 수행해야하는 횟수의 최솟값은?

def until_one(n, k):
    
    count = 0
    
    while n != 1 : 
        
        if n % k == 0:
            n = n // k
        else:
            n = n - 1
            
        count += 1 
    
    return count
    
print(until_one(17,4))
    