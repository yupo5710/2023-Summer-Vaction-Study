T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    a2 = a % 10
    if a2 == 0:
        print(10)
    elif a2 == 1 or a2 == 5 or a2 == 6:
        print(a2)
    elif a2 == 4 or a2 == 9:
        b2 = b % 2
        if b2 == 0:
            print(a2*a2%10)
        else:
            print(a2)
    elif a2 == 3 or a2 == 7 or a2 == 8 or a2 == 2:
        b2 = b % 4
        if b2 == 0:
            print(a2**4%10)
        else:
            print(a2**b2%10)
        
