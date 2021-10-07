#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
#from collections import Counter
import sys

N = int(sys.stdin.readline())
arr = list(int(input()) for _ in range(N))

def pivot_find(arr, left, right):
    #가장 왼쪽에 있는것
    pivot = arr[left]
    low = left
    high = right
    
    while low < high:
        while low <= right and arr[low] < pivot:
            low +=1
        while left <= high and pivot < arr[high]:
            high -=1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    return high


def quick_sort(arr, left, right):
    
    if left < right:
        pivot_num = pivot_find(arr, left, right)
    
        quick_sort(arr, left, pivot_num-1)
        quick_sort(arr, pivot_num+1, right)
    
quick_sort(arr,0, len(arr)-1)   

for i in arr:
    print(i)