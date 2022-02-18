# 모험가 길드

def group(N, scared_score):
     
    # 공포도가 낮은 순서대로 정렬하기
    sorted_scared_score = sorted(scared_score)
    # print(sorted_scared_score)
    
    result = 0 # 총 그룹의 수
    count = 0  # 현재 그룹에 포함된 모험가의 수
    
    for x in sorted_scared_score:
        # 그룹에 모험가를 포함시키기
        count += 1
        if count >= x:
            # 그룹에 포함시킨 모험가의 수가 공포도보다 크거나 같다면 그룹 결성
            result += 1
            count = 0 # 그룹의 수를 측정했으면 다시 0명으로 리셋해줘야함
    
    return result        
    
print(group(5, [2,3,1,2,2]))