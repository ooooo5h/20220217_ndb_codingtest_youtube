# 문자열 재정렬
from string import ascii_uppercase
import string
from unittest import result

def make_beautiful(s):

    result = []
    num = 0
    
    # 문자 하나씩 확인하기
    for x in s:
        # 알파벳이면 리스트에 넣기
        if x.isalpha():
            result.append(x)
        
        # 숫자면 더하기
        else:
            num += int(x)
    
    result.sort()
    
    # 숫자가 하나라도 있었다면 뒤에 붙이기
    if num != 0:
        result.append(str(num))
    
    return ''.join(result)   # ''.join(문자열)  => 문자열합치기

print(make_beautiful('K1KA5CB7'))