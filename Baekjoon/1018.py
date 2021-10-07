#왜 틀렸는지 모르겠다(해결 : 문제를 잘못 읽음)
#하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다. << 요걸 못 읽었네
import sys

N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(input())
c=64

for a in range(N-8+1):
    for b in range(M-8+1):
        cnt = 0
        for j in range(8):
            for i in range(8):
                if 0==(j+a)%2:
                    if 0 == (i+b)%2 and 'W' != chess[j+a][i+b]:
                        #print('test1',chess[j+a][0][i+b], i+b, j+a) 
                        cnt+=1
                    if 0 != (i+b)%2 and 'B' != chess[j+a][i+b]:
                        #print('test2',chess[j+a][0][i+b],i+b,j+a) 
                        cnt+=1
                else:
                    if 0 == (i+b)%2 and 'B' != chess[j+a][i+b]:
                        #print('test3',chess[j+a][0][i+b],i+b,j+a) 
                        cnt+=1
                    if 0 != (i+b)%2 and 'W' != chess[j+a][i+b]:
                        #print('test4',chess[j+a][0][i+b],i+b,j+a)
                        cnt+=1
        #print(cnt)
        c = min(c, min(64-cnt, cnt))
        #c.append(cnt)
        #c.append(cnt2)


print(c)            
print(min(c))