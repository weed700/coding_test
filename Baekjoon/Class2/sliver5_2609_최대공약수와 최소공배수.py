import sys

#유클리드 호제법(최대 공약수 구하는법)
#N*M = 최대 공약수*최소
N, M = map(int, sys.stdin.readline().split())

A, B =N,M

while True:
    rem = A%B
    if 0 == rem:
        print(B)
        print(N*M//B)
        break
    A = B
    B = rem

    
