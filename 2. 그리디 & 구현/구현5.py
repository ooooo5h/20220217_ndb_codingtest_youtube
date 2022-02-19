# 문자열 재정렬
from string import ascii_uppercase
import string

def make_beautiful(s):
    
    letters = list(s)
    
    num = 0
    alphabet = ''
    
    for letter in letters:
        if letter in str(list(range(0, 10))):
            num += int(letter)
        elif letter in list(string.ascii_uppercase):
            alphabet += letter
    
    alphabet = ''.join(sorted(alphabet))

    return alphabet+str(num)  

print(make_beautiful('K1KA5CB7'))