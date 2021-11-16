'''brute force
n = int(input('enter the no...'))
for i in range(2, n - 1):
    if n % i == 0:
        print("not prime")
        break
    else:
        print('prime')
        break'''

'''another method
for i in range(2, round(n**0.5)):
    if n % i == 0:
        print("not prime")
        break
    else:
        print('prime')
        break'''

'''# prime sieve
n = int(input('enter the number...'))
p = [i for i in range(0, n + 1)]
print(p)
for i in range(1, n + 1):
    for j in range(2, 10):
        if i % j == 0 and i > j:
            p[i] = 0

print(p)'''

'''# n using Sieve of Eratosthenes

n = int(input("Enter the number..."))
# Create a boolean array "prime[0..n]" and initialize
#  all entries it as true. A value in prime[i] will
# finally be false if i is Not a prime, else true.
prime = [1 for i in range(n + 1)]
p = 2
while p * p <= n:

    # If prime[p] is not changed, then it is a prime
    if prime[p] == 1:

        # Update all multiples of p
        for i in range(p * p, n + 1, p):
            prime[i] = 0
            p += 1

print(prime)'''

# prime sieve
n = int(input('Enter the last value'))
p = [0 for i in range(0, n + 1)]
for i in range(3, n + 1, 2):
    p[i] = 1
for i in range(3, n + 1, 2):
    if p[i] == 1:
        j = i ** 2
        while j < n:
            p[j] = 0
            j = j + i
p[2] = 1
print(p)
a = int(input('enter the lower limit'))
b = int(input('enter the uppr limit'))
print(p[a:b])
