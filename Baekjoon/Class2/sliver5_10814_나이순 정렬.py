#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

N = int(sys.stdin.readline())

age_name = [list(sys.stdin.readline().split()) for _ in range(N)]

#나이 int 형 변환
for i in range(N):
    age_name[i][0] = int(age_name[i][0])

re_age_name = sorted(age_name, key=lambda x: x[0])

for re in re_age_name:
    print(re[0],re[1])