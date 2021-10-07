#멍청한 짓 했군 리스트 sort() 안먹히는게 아니라 출력할때 리턴값이 None으로 뜨는거네
import sys
import itertools
from collections import Counter

N = int(input())

arr = list(sys.stdin.readline().split() for _ in range(N))

word = list(itertools.chain(*arr))

#단어 길이가 짧은 것부터
short_word = []
dic = {}
for w in word:
    dic[w] = len(w)

#키 값을 기준으로 정렬
temp = sorted(dic, key=lambda x : dic[x])
#키 값만 뽑기
num = sorted(dic.values())

#길이가 같을 때 사전 순으로 정렬
list1 = []

for i in set(num):
    list2 = []
    for t in temp:
        if i == len(t):
            list2.append(t)
    list1.append(sorted(list2))

#출력
for a in list1:
    for b in a:
        print(b)
