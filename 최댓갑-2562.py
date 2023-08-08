numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i) #append로 순차적 숫자 넣음
print(max(numbers)) #최댓갑 찾기
print(numbers.index(max(numbers))+1) #index는 0부터 시작하니깐 +1 해야함