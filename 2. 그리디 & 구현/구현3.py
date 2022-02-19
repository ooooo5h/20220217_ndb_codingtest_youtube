# 시각

def count_3(N):
    
    # 3의 갯수 카운트
    count = 0
    
    for h in range(N+1):
        # N+1인 이유 : 
        # 5를 입력했으면, 0시 1시 .. 5시까지 돌아가며 3을 세야하니까
        for m in range(60):
            for s in range(60):
                # 속해있는 모든 3의 개수를 세야하기 때문에
                # 문자형이 편하다
                # 반복문 중첩을 통해, 횟수를 돌때마다 3이 있다면 더해주면 해결
                if '3' in str(h) + str(m) + str(s):
                    count += 1
    
    return count
        
print(count_3(1))