#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

N, K = map(int,sys.stdin.readline().split())

arr = []
re = []

for i in range(1,N+1):
    arr.append(i)

for _ in range(N):
    for i in range(1,K+1):

        if i == K:
            re.append(arr.pop(0))
        else:
            arr.append(arr.pop(0))
 
print("<", end='')
for i in range(len(re)):
    if 0 == i:
        print(re[i],end='')
    else:
        print(',',re[i], end='')
print(">")