n,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort(reverse = True)
print(nums[k-1])