# 왕실의 나이트

def count_cases(current_location):

    # a1, c2처럼 문자로 들어옴
    y = int(current_location[1])
    
    alphabet = ['a','b','c','d','e','f','g','h']
    x = alphabet.index(current_location[0])+1
    
    steps = [(1,2),(1,-2),(2,-1),(2,1),(-2,-1),(-2,1),(-1,-2),(-1,2)]
    
    count = 0
    
    for step in steps:
        next_x = x + step[0]
        next_y = y + step[1]
        
        if 1 <= next_x <= 8 and 1 <= next_y <= 8 :
            count += 1
    
    return count
            
print(count_cases('c2'))
