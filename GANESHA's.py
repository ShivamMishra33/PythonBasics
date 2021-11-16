n =  int(input())
if n>5 and n<99:

    for j in range(n):
        if   (j == 0) :
            print('*' + (n - ((n+1)//2)-1)*" " + (((n+1) // 2)*'*'))
        
        elif j < (n - ((n+1)//2)) -1   and j>0:
            for i in range((n - ((n+1)//2)) - 1):
                print('*' + (n - ((n+1)//2)-1)*' '  + '*')

        elif j == (n+1)/2 :
            print( n*'*')
        
        elif j>(n+1)//2 and j<(n-1):
            for i in range((n - (n+1)//2)-1):
                print((n - ((n+1)//2))*' '  + '*' + ((n - (n+1)//2)-1)*' ' + '*')

        elif j==(n-1):
            print((((n+1) // 2)*'*') + (n - ((n+1)//2)-1)*" " + '*' )
