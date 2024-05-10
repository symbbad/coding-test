nums = [int(input()) for _ in range(3)]

if sum(nums) > 180:
    print("Error")
elif len(set(nums)) == 1:
    print("Equilateral")
elif len(set(nums)) == 2:
    print("Isosceles")
else:
    print("Scalene")