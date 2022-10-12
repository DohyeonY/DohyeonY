import sys
from itertools import combinations_with_replacement
n , m = map(int, sys.stdin.readline().split(" "))
stack = list(map(int , sys.stdin.readline().split(" ")))
stack.sort()
ans = list(combinations_with_replacement(stack, m))
ans = list(set(ans))
ans.sort()
if m == 1:
    for t in range(0, len(ans)):
        s = list(ans[t])
        print(s[0])
else:
    for t in range(0,len(ans)):
        s = list(ans[t])
        for u in range(0,len(s)-1):
            print(s[u],end=" ")
        print(s[len(s)-1])