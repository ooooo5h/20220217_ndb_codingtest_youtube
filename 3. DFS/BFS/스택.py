# 스택 자료구조 : 선입후출( 입구와 출구가 동일한 형태 )
# ex)박스쌓기

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(4)
# stack = 5,2,3,7
stack.pop()
# stack = 5,2,3
stack.append(1)
stack.append(4)
# stack = 5,2,3,1,4
stack.pop()
# stack = 5,2,3,1
print(stack[::-1])  # 최상단부터 꺼내기 = > 1,3,2,5
print(stack)        # 최하단부터 꺼내기 => 5,2,3,1