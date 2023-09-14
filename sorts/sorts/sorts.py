from random import randint
import time

def bubbleSort(mas):
    length = len(mas)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]

def qsort(mas):
    if (len(mas) <= 1): 
        return mas

    pivot = mas[0]

    less = [i for i in mas if i < pivot]
    equal = [i for i in mas if i == pivot]
    bigger = [i for i in mas if i > pivot]

    return qsort(less) + equal + qsort(bigger)

def genRandList(n):
    return [randint(1, 1000) for _ in range(n)]

def test(n):
    randListB = genRandList(n)
    randListQ = randListB.copy()
    
    s = time.time()
    bubbleSort(randListB)
    f = time.time()
    print(f"Bubble: {n} elems = " + str(f - s))
    
    s = time.time()
    qsort(randListQ)
    f = time.time()
    print(f"qsort: {n} elems = " + str(f - s))
    


test(100)
test(1_000)
test(10_000)