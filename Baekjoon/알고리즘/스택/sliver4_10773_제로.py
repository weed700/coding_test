#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

K = int(sys.stdin.readline())
s = []

for _ in range(K):    
    num = int(sys.stdin.readline())

    if 0 != num:
        s.append(num)
    else:
        s.pop()

print(sum(s))        