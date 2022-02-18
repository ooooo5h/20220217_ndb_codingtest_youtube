# 모험가 길드

def group(N, scared_score):
    
    # 낮은 공포도 순으로 정렬하면..
    # 1,2,2,2,3 => 1은 패스, 2는2명이니까 2개 카운트, 그다음 냅두기
    sorted_scared_score = sorted(scared_score)
    
    # 그룹수
    count = 0
    
    # 횟수
    result = 0
    
    for x in sorted_scared_score:
        # 한명씩 꺼낼 때 마다 그룹수에 추가하기
        count += 1
        
        # 그룹멤버수가 공포도 x와 같거나 크다면 횟수 카운트
        if count >= x:
            result += 1
            # 횟수로 세고나면 다시 처음부터 그룹수를 세야하므로 초기화
            count = 0
            
    return result
    
print(group(5, [2,3,1,2,2]))