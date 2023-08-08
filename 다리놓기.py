def fact(n):
    num =  1
    for  _ in range(1,n+1):
        num += 1
    return
T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    result = fact(m) // (fact(n) * fact(m - n))
    print(result)