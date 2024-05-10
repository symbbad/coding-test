a, b, c = map(int, input().split())
nums = [a, b, c]

if max(nums) >= sum(nums) - max(nums):
    print(2*(sum(nums) - max(nums)) - 1)
else:
    print(a + b + c)