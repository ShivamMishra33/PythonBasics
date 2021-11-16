def GCD(a,b):
    print (a) if b==0 else GCD(b,a%b)
    


a = int(input())
b = int(input())
GCD(a,b)