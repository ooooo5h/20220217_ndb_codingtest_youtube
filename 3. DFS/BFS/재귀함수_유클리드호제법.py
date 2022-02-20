# 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘이 유클리드 호제법
# 유클리드 호제법? 
# 두 자연수 A>B에 대하여 A를 B로 나눈 나머지를 R이라고 할 때, B와 R의 최대공약수 = A와 B의 최대공약수

def gcd(a, b):
    # a가 b의 배수라면 b가 그대로 리턴
    if a % b == 0:
        return b 
    else :
        return gcd(b, a%b)

print(gcd(192, 162))   # 정답 6