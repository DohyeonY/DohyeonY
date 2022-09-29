N, K = input().split()
M = len(N) #전체 자릿수
K = int(K)
cache =[[False for i in range(11)] for i in range(1000001)]
q=[]
q.append([[ch for ch in N],0])
cache[int(N)][0]=True

def swap(N, idx1, idx2):
    temp = N[idx1]
    N[idx1] = N[idx2]
    N[idx2] = temp

answer = -1
while q:
    n, depth = q.pop(0)

    if depth == K: 
        answer = max(answer, int(''.join(n)))
        continue
       
    for i in range(M): 
        for j in range(i+1,M):
            if i ==0 and n[j] =='0': 
                continue

            swap(n, i, j)
            n_int = int(''.join(n))
            if not cache[n_int][depth+1]:
                cache[n_int][depth+1] = True 
                q.append([n.copy(), depth+1])
            swap(n, i, j)

print(answer)