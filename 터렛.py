import math #모듈
T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split()))
    dis = math.sqrt((x1 - x2)**2 - (y1 - y2)**2) #math.sqrt 는 제곱근 가져오기
    if dis == 0:
        if r1 == r2:
            print(-1) #두 원이 같을때
        else:
            print(0) #한쪽 원이 작음
    else:
        if r1 + r2 == dis or abs(r2 -r1) == dis: #두 원이 접하거나 내부의 원이 접할때
            print(1)
        elif (abs(r2 - r1) < dis) and ((r2 + r1) > dis): #두 원이 만날때
            print(2)
        else:
            print(0) #혹시 모름

