import time

def isPrime(num):
    if (num == 0 or num == 1): return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    else:
        return 1

def isPrimeMass(n):
    mas = [i for i in range(n + 1)]
    for i in range(n):
        if not(isPrime(mas[i])): mas[i] = 0

def erat(n):
    mas = [i for i in range(n + 1)]
    
    mas[1] = 0
    i = 2
    while i <= n:
        if mas[i] != 0:
            j = 2 * i
            while j <= n:
                mas[j] = 0
                j = j + i
        i += 1

t0 = time.time()
isPrimeMass(10)
t1 = time.time() - t0
print(t1)

t0 = time.time()
erat(10)
t1 = time.time() - t0
print(t1)

t0 = time.time()
isPrimeMass(100)
t1 = time.time() - t0
print(t1)

t0 = time.time()
erat(100)
t1 = time.time() - t0
print(t1)

t0 = time.time()
isPrimeMass(10000000)
t1 = time.time() - t0
print(t1)

t0 = time.time()
erat(10000000)
t1 = time.time() - t0
print(t1)
