import math
T = int(input())

for i in range(T):
    x1,y1,x2,y2 = list(map(int,input().split()))
    n = int(input())
    count = 0 #카운트를 안으로 해야 케이스 값이 따로 나옴
    for j in range(n):
        x,y,r = map(int,input().split())
        dis1 = math.sqrt(abs(x1 - x)**2 + abs(y1 - y)**2) #원과 출발점 사이의 거리
        dis2 = math.sqrt(abs(x2 - x)**2 + abs(y2 - y)**2) #원과 도착점 사이의 거리
        
        if r > dis1 and r > dis2: #두 점 모두 행성 안에 있을떄
            pass
        elif r > dis1: #그 외
            count += 1
        elif r > dis2:
            count += 1
    print(count)