# 최대공약수와 최소공배수
import math

def lcm(a,b):
    return a*b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14))  # 최대공약수구하는 함수 gcd()
print(lcm(a,b)) # 최소공배수 구하는 함수 lcm()