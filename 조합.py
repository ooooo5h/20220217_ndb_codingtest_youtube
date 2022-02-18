# 조합이란?
# 서로 다른 n개에서 순서 상관없이 서로 다른 r개를 선택하는 것. nCr
# ['A', 'B', 'C'] 에서 순서를 생각하지 말고 2개를 뽑아 나열하세요

from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)

# 결과값 : [('A', 'B'), ('A', 'C'), ('B', 'C')]