#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

L = int(sys.stdin.readline())

eng = list(sys.stdin.readline().rstrip())
ascii = 96
r = 31
M = 1234567891
sum = 0

for i in range(L):
    sum += (ord(eng[i])-96)*(r**i)

print(sum%M)