

def count_3(N):
    
    start_hour = [0]
    start_min = [min for min in range(0, 60)]
    start_second = [sec for sec in range(0, 60)]

    # 분 과 초는 동일하게 갈텐데
    # 0~9 :  1개
    # 10 ~ 19 : 1
    # 20 ~ 29 : 1
    # 30 ~ 39 : 10
    # 40 ~ 49 : 1
    # 50 ~ 59 : 1
    # 1분간 15개
    # 1초간 15개 => 1분 총 30개의 3이 등장 ..?
    
    # 시
    # 0시 30개
    # 1시2시 60개
    # 3시 30개
    for i in range(N):
        # 0,1,2,3,4
        

    
        
count_3(1)