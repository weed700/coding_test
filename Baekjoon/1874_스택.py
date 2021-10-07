import sys

n = int(input())

arr = [int(sys.stdin.readline()) for _ in range(n)]

stack = 0
flag = 0
s = []
re = []


for a in range(n):
    while stack < arr[a]:
        stack+=1
        re.append('+')
        s.append(stack)
   
    if s[-1] == arr[a]:
        s.pop()
        re.append('-') 
    else:
        flag = 1
        break
    
if 1 == flag:
    print('NO')
else:
    print("\n".join(re))