# 순열이란?
# 서로 다른 n개에서 서로 다른 r개를 일렬로 나열하는 것. nPr
# ['A', 'B', 'C'] 에서 3개를 선택하여 나열하세요

from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# 결과값 : [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]


# 중복 순열
# 3개를 뽑아 모든 순열 구하기(중복허용)
from itertools import product
data_a = ['A', 'B', 'C']
result_a = list(product(data_a, repeat=2))
print(result_a)

# 결과값 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]