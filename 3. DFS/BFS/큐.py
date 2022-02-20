# 먼저 들어온 데이터가 먼저 나가는 선입선출
# ex) 입구와 출구가 모두 뚫려있는 터널

# 큐문제는 deque 라이브러리를 사용하는게 더 효율적
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# queue = 5,2,3,7
queue.popleft()
# queue = 2,3,7
queue.append(1)
queue.append(4)
# queue = 2,3,7,1,4
queue.popleft()
# queue = 3,7,1,4

print(queue) # 먼저 들어온 순서대로 출력 => 3,7,1,4

queue.reverse()
print(queue) # 나중 들어온 원소부터 출력 => 4,1,7,3