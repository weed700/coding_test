#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    s = sys.stdin.readline().split()

    if "push_front" == s[0]:
        arr.append(s[1])
    elif "push_back" == s[0]:
        arr.insert(0,s[1])
    else:
        if "front" == s[0]:
            if arr:
                print(int(arr[-1]))
            else:
                print(-1)
        elif "back" == s[0]:
            if arr:
                print(int(arr[0]))
            else:
                print(-1)
        elif "size" == s[0]:
            print(len(arr))
        elif "empty" == s[0]:
            if not arr:
                print(1)
            else:
                print(0)
        elif "pop_front" == s[0]:
            if arr:
                print(int(arr.pop()))
            else:
                print(-1)
        elif "pop_back" == s[0]:
            if arr:
                print(int(arr.pop(0)))
            else:
                print(-1)