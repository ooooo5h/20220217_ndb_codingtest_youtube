# 문자열 재정렬
from string import ascii_uppercase
import string

def make_beautiful(s):
    
    letters = list(s)
    
    num = ''
    alphabet = ''
    
    for letter in letters:
        if letter in str(list(range(0, 10))):
            num += letter
        elif letter in list(string.ascii_uppercase):
            alphabet += letter
    
    # print(num)
    # print(''.join(sorted(alphabet)))
    alphabet = ''.join(sorted(alphabet))
    
    # print(alphabet+num)
    return alphabet+num  # 어이 왜 리턴이 안되지..??

make_beautiful('K1KA5CB7')