#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
#from collections import Counter


import sys

#입력
N,M = map(int,sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

def solution(N, M, tree):
    start = 1
    end = max(tree)

    #이분 탐색 알고리즘 2805 백준
    while start <= end:
        mid = (start+end)//2

        tree_sum =0 #자른 나무의 합
        for t in tree:
            #mid 보다 위인 나무만 잘라서 합한다.
            if mid <= t:
                tree_sum += (t - mid)
        
        #자른 나무른 이분 탐색으로 찾는다
        if M <= tree_sum:
            start = mid + 1
        else:
            end = mid - 1
    
    return end

print(solution(N, M, tree))

