while True:
    a, b, c = map(int, input().split())
    nums = [a, b, c]

    if sum(nums) == 0:
        break

    if max(nums) >= sum(nums)-max(nums):
        print("Invalid")

    elif len(set(nums)) == 1:
        print("Equilateral")
    elif len(set(nums)) == 2:
        print("Isosceles")
    else:
        print("Scalene")