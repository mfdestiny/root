import time

def timetrials(func, n, trials = 10):
    totaltime = 0
    #start = time.time()
    for i in range(trials):
        start = time.time() # it should be here
        func(list(range(n)))
        totaltime += time.time() - start
    print("average =%10.7f for n = %d" % (totaltime/trials, n))

#for n in [50, 100, 200, 400, 800, 1600, 3200]:
    #timetrials(duplicatesN, n)
#
#def duplicates2(L):
#    n = len(L)
#    for i in range(1,n):
#        for j in range(i):
#            if L[i] == L[j]:
#                return True
#    return False

#def duplicates6(L):
#    s = set()
#    for e in L:
#        if e in s:
#            return True
#            s.add(e)
#    return False

#sorting list and checking against set seems to be the fastest method as n increases
