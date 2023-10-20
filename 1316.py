N = int(input()) 

result = 0

for _ in range(N):
    word = input()

    s = set()
    prev_char = ''

    for char in word:
        if char in s and char != prev_char:
            break
        s.add(char)
        prev_char = char
    else:
        result += 1

print(result)



'''
N = int(input())
count = 0 

for i in range(N):
    word = input()
    error = 0
    for j in set(word): # 중복글자 없게
        nb = word.count(j) # word에 j가 등장하는 곳 
        a = j * nb
        
        if a not in word:
            error = 1
            break
    
    if error == 0:
        count += 1
print(count)
'''