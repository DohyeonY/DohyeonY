N = int(input())

arr = []

for i in range(N) :
    arr.append(input())
    
setArr = list(set(arr))

list = []
for i in setArr:
    list.append((len(i), i))
    
sortedList = sorted(list)

result = []
for i, j in sortedList :
    result.append(j)
    
for k in result :
    print(k)