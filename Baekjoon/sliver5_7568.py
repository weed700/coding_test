#브루트포스 알고리즘

import sys

N = int(sys.stdin.readline())
arr_xy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

re = []
for i in range(len(arr_xy)):
    count = 1
    for j in range(len(arr_xy)):
        if (arr_xy[i][0] < arr_xy[j][0]) and (arr_xy[i][1] < arr_xy[j][1]):
            count +=1
    re.append(count)

print(" ".join(map(str,re)))