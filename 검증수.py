nums = list(map(int,input().split()))
z = []
for i in range(len(nums)):
    a = nums[i] ** 2
    z.append(a)
b = sum(z) % 10
print(b)