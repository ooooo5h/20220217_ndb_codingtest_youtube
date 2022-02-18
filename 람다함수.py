# 홍길동, 이순신, 아무개를 점수순으로 정렬하세요
## 일반 함수 사용
from unittest import result


array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def sort_by_score(x):
    return x[1]

# sorted(정렬할 데이터, key파라미터)  : 어떤 것을 기준으로 데이터를 정렬할건지
print(sorted(array, key=sort_by_score))  
# array를 sort_by_score의 결과값인 x[1]값 기준으로 정렬하겠다
# 출력값 : [('이순신', 32), ('홍길동', 50), ('아무개', 74)]


## 람다 함수 사용
print(sorted(array, key=lambda x:x[1]))
# 튜플이나 리스트와 같은 원소의 두번째 원소를 기준으로 정렬하겠다.
# 출력값 : [('이순신', 32), ('홍길동', 50), ('아무개', 74)]


# 두 개의 리스트를 합한 값을 구해주세요.
lista = [1,2,3,4,5]
listb = [6,7,8,9,10]

result = map(lambda a,b : a+b, lista, listb)
print(list(result))
# 출력값 : [7, 9, 11, 13, 15]