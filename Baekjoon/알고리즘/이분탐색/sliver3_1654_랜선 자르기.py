import sys

K, N = list(map(int,sys.stdin.readline().split()))

arr = [int(sys.stdin.readline()) for _ in range(K)]

start,end = 1, max(arr)

while start <= end: 
    mid = (start+end)//2

    sum = 0
    for num in arr:    
        sum += num//mid
    
    print(mid, sum)
    if N <= sum:
        start = mid+1
    else:
        end = mid-1 

print(end)