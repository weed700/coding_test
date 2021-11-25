while True:
    temp = input()
    flag = 1

    if '0' == temp:
        break
    else:
        l = list(range(len(temp)-1,0,-1))
        
        for i,j in zip(range(len(temp)), l):
            if temp[i] == temp[j]:
                if i == j:
                    break
            else:
                flag = 0
                break
        
        if 1 == flag:
            print('yes')
        else:
            print('no')