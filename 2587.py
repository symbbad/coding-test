array = []

for i in range(5):
    array.append(int(input()))

array.sort()

print(int(sum(array)/len(array)))
print(array[2])