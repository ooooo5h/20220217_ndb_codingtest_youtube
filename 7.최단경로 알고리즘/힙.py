import heapq

# 오름차순 힙 정렬(Heap sort)
def heapsort(iterable):
    h = []
    result = []
    
    # 모든 원소를 차례대로 힙에 넣기
    for value in iterable:
        heapq.heappush(h, value)
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내서 다시 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([9,5,6,2,8,4,0,7,1,3])
print(result)