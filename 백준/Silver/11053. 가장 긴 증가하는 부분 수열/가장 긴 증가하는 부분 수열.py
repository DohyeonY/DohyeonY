N = int(input())
arr = list(map(int, input().split()))

a = [1] * N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            a[i] = max(a[j] + 1, a[i])

print(max(a))