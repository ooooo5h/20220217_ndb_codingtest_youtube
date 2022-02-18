# 총합 : sum()
a = [1,2,3,4,5]
result = sum(a)
print(result)

# 최소값, 최대값 : min(), max()
b = [7,3,5,2]
min_result = min(b)
max_result = max(b)
print(min_result, max_result)

# eval() ? => 파이썬에서 실행 가능한 문자열이(expression) 매개변수로 들어오면, 문자열로 들어온 그 expression을 파이썬이 실행해주는 함수
# " " 안의 파라미터가 문자임에도 불구하고 계산된 56이 리턴됨
result_eval = eval("(3+5)*7")
print(result_eval)

# sorted()
result_sorted = sorted([9,1,8,5,4])
print(result_sorted)
# 출력값 : [1, 4, 5, 8, 9]

# sorted() 역순
reverse_result = sorted([9,1,8,5,4], reverse=True)  
print(reverse_result)
# 출력값 : [9, 8, 5, 4, 1]