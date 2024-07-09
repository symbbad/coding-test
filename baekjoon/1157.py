N = input().lower()

result = {}
s = set()

for char in N:
    if char not in result:
        result[char] = 1
    else:
        result[char] += 1

max_value = max(result.values())

for key, value in result.items():
    if value == max_value:
        s.add(key)

if len(s) > 1:
    print("?")
else:
    print(s.pop().upper())



'''
word = input().upper()
abc = list(set(word))
# set 사용 : 중복방지, 입력받은 애들만 확인용

b = []

for i in abc:
    b.append(word.count(i))
    
if b.count(max(b)) != 1:
    print('?')
else:
    print(abc[b.index(max(b))])
'''