import time

def sumk(k):
    start = time.time()
    total = 0
    for i in range(k+1):
        total = total + i
    end = time.time()
    return total, end-start

def sumk2(k):
    start = time.time()
    total = (k*(k+1)//2)
    end = time.time()
    return total, end-start
