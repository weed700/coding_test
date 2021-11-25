#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

N,K = map(int,sys.stdin.readline().split())

def factorial(n):
    ret = 1

    for i in range(1, n+1):
        ret*=i
    
    return ret

re = factorial(N)/(factorial(K)*factorial(N-K))

print(int(re))
