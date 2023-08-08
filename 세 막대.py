
arr = sorted(list(map(int,input().split())))
a = arr[2]
b = arr[1]
c = arr[0]
if b + c > a:
    print(sum(arr))
else:
    print((b + c)*2 -1)
    
'''
    if a + b > c:
        print(sum(a+b+c))
'''