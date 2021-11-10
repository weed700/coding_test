#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = list(map(int,sys.stdin.readline().split()))
    H = arr[0]
    W = arr[1]
    N = arr[2]
    wc_v = 0

    if 0 == N%H:
        f = H*100
        l = (N//H)
    else:
        f = (N%H)*100
        l = (N//H)+1
    print(f+l)
    