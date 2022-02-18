# 순열이란?
# 서로 다른 n개에서 서로 다른 r개를 일렬로 나열하는 것. nPr
# ['A', 'B', 'C'] 에서 3개를 선택하여 나열하세요

from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# 결과값 : [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]