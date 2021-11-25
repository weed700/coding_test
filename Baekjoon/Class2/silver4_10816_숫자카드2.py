#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys
from collections import Counter

N= int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))


#Counter는 리스트의 원소들이 몇번 나왔는지 카운트 하여 딕셔너리 형태로 변환
count = Counter(card)

for i in range(M):
    if target[i] in count:
        print(count[target[i]], end=' ')
    else:
        print(0,end=' ')