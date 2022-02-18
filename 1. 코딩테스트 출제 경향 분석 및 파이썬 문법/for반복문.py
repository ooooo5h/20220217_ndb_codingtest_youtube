# 학생들의 합격 여부 판단예제(특정 번호의 학생은 제외)
scores = [90,85,77,65,97]
cheating_student_list = {2,4}

for i in range(5):  # i = 0,1,2,3,4
    if i+1 in cheating_student_list:
        continue
    if scores[i] > 80 :
        print(i+1,'번 학생은 합격입니다.')