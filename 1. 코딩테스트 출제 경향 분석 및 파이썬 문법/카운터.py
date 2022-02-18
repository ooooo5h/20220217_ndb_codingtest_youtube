# 파이썬 collections라이브러리의 Counter는 등장 횟수를 세는 기능
# 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을때 내부의 원소가 몇번 등장하는지 알려줌

from collections import Counter

counter = Counter(['red','green','blue','green','blue','red','red','green' ])

print(counter['blue'])
print(dict(counter))
# 출력값 : {'red': 3, 'green': 3, 'blue': 2}와 같이 딕셔너리형으로 변환