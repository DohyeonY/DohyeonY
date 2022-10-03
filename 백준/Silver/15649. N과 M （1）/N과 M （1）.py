from itertools import permutations

N, M = map(int, input().split())
lst = []
for i in range(1, N+1) :
    lst.append(str(i))
# lst = map(str, range(1, N+1))
# print(permutations(lst, M))
# print(lst)
print('\n'.join(list(map(' '.join, permutations(lst, M)))))