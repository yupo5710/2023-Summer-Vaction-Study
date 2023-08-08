numbers = []

for i in range(5):
    n = int(input()) #숫자 입력
    numbers.append(n) #numbers칸에 숫자들 입력
    
numbers.sort()
print(int(sum(numbers)/5)) #평균값 출력
print(int(numbers[2])) #중앙값 출력