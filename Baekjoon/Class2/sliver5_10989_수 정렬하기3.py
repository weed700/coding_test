#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

N=int(sys.stdin.readline())
arr = [0]*10001

for i in range(N):
    arr[int(sys.stdin.readline())]+=1

for i in range(10001):
    if 0 != arr[i]:
        for j in range(arr[i]): 
            print(i)