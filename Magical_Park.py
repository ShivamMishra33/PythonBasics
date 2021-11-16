def magic_park(M,N,K,S):
    ip_magic_park(M,N,K,S)
    flag = True
    for i in range(M):
        for j in range(N):
            
            if (S<K):
                flag = False
                break
            elif char[i][j] == '*':
                S += 5
            elif char[i][j] == '.':
                S -= 2
            elif char[i][j] == '#':
                break
            elif (j != (N-1)):
                S-1

    if flag == True:
        print('Yes')
        print ( S )

    if flag == False:
        print('No')


        
def ip_magic_park(M,N,K,S):
    char = []
    for i in range(M):
        list1 = []
        for j in range(N):
            list1.append(input())
        char.append(list1)
    return char[i][j]     


M = int(input())
N = int(input())
K = int(input())
S = int(input())


magic_park(N,M,K,S)


