N = str(input())

l1 = []
for i in N:
    l1.append(int(i))
    
l1.sort(reverse=True)

for i in l1:
    print(i, end="")