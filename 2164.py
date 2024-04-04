N = int(input())
_list = list(range(1,N+1))

while (len(_list)>1):
    _list.pop(0)
    temp = _list.pop(0)
    _list.append(temp)

print(_list.pop(0))