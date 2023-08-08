'''
numbers = [ i for i in range(1,31)]
for _ in range(28):
    a = int(input())
    numbers.remove(a)
for i in range(len(numbers)):
    print(numbers[i])
    '''
'''
nums = [i for i in range(1, 31) if i not in [int(input()) for _ in range(28)]]
print(min(nums))
print(max(nums))
'''
nums = [i for i in range(1,31) if i not in [int(input()) for _ in range(1,29)]]
print(nums)