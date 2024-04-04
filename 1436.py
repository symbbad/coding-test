n = int(input())
count = 0

std = 666

while True:
    if '666' in str(std):
        count += 1

    if count == n:
        print(std)
        break
    
    std += 1
    print(std)