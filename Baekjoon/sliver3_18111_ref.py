#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys
from collections import defaultdict

N,M,B = map(int,sys.stdin.readline().split())

ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
g_max = max(map(max, ground))
g_min = min(map(min, ground))

Ltime = 1e9


#딕셔너리 값이 없을 때 기본 값 추가
dic = defaultdict(lambda:0)

for a in range(N):
    for b in range(M):
        dic[ground[a][b]] += 1

for i in range(g_min,g_max+1):
    plus = 0
    inven = 0
    
    for j in dic.keys():
        if i < j:
            inven+=dic[j]*abs(i-j)
        elif j < i:
            plus += dic[j]*abs(i-j) 

    if plus <= inven+B:
        time = inven*2 + plus

        if time < Ltime:
            Ltime = time
            resultHeight = i
        elif Ltime == time and resultHeight < i:
            resultHeight = i
    
print(Ltime, resultHeight)

