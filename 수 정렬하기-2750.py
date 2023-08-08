n = int(input())
a = [] #a라는 정렬 칸 만들기
for i in range (n):
    a.append(int(input())) #append로 순차적으로 숫자 입력 받기
a.sort() #sort로 수 정렬
for i in range(len(a)): #정렬된 a칸 범위 설정
    print(a[i]) #다시 정렬 및 출력