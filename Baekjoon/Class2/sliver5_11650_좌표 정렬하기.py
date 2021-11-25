#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

N = int(sys.stdin.readline())

comp = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    comp.append([x,y])

# x좌표 정렬 후 y좌표 정렬
comp.sort(key=lambda x:(x[0], x[1]))


for re in comp:
    print(re[0], re[1])

