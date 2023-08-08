n,m = map(int,input().split())
basket =[0]*n #n개 까지의 바구니 생성

for _ in range(m):
    i,j,k = map(int,input().split())#i부터 j까지 공을 k번 넣음
    for a in range(i,j+1):
        basket[a-1] = k #바구니의 번호는 1번이지만 인덱스는 0번 부터시작 -1붙여줌
for b in range(n):
    print(basket[b],end = ' ')