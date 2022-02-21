n,k = map(int, input().split())

a = []
a.append(list(map(int, input().split())))

b = []
b.append(list(map(int, input().split())))


def change_num(a, b):
    
    for i in range(0, n+1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    
    print(a)
                
change_num(a,b)