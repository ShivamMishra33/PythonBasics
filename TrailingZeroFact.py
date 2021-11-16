n =  int(input())
trailing_zeros1 = 1
count = 0
i = 1
while trailing_zeros1!=0:
    trailing_zeros1 = (n//((5)**i))
    
    i +=1
    count = count + trailing_zeros1

print(count)