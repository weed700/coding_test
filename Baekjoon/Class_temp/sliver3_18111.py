#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

N,M,B = map(int,sys.stdin.readline().split())

ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
g_max = max(map(max, ground))
g_min = min(map(min, ground))

add_time = 1
remove_time = 2
time = 1e9 #int 범위 내에서 무한대 값

#최소값 부터 최대값 오름차순으로 반복
for i in range(g_min, g_max+1):
    temp = []
    block = 0
    #모든 요소의 값을 빼기 위한 리스트 만들기
    for a in range(N):
        for b in range(M):
            temp.append(i)
    
    #2차원 리스트를 1차원 리스트로 변경
    sum_g = sum(ground, [])
    #모든 요소의 값을 뺀 후 그 값을 더한 결과
    re=sum([x-y for x,y in zip(sum_g,temp)])

    #제거 후 인벤토리에 블럭 저장
    if 0 < re:
        sum_time = re*remove_time
        block += re

    #블럭을 추가 해야할 경우
    elif re <0:
        sum_time = abs(re*add_time)
    
    if B+block < abs(re):
        continue
    
    if sum_time <= time:
        time = sum_time
        height = i 

print(time, height)


