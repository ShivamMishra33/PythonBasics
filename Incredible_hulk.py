t = int(input())
count_list = []
for i in range(t):
    n =  int(input())
    count = 0
    while(n!=0):
        if n%2 != 0:
            count += 1
            n = n//2
        else:
            n = n//2
    count_list.append(count)

for i in range(t):
    print(count_list[i])
    