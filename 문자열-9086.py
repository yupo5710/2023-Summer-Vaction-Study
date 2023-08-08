n = int(input())

for _ in range(n):
    string = input() 
    print(string[0],string[-1],sep = '')# sep = '' 는 띄어쓰기 없애줌
    # [0],[-1]은 문자열의 순번:양수는 첫자리부터,음수는 뒷자리부터