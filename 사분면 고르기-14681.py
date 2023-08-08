x = int(input("x좌표를 입력해주새요"))
y = int(input("y좌표를 입력하세요"))

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')
