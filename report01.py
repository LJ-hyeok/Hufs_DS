import time
import random

def sol_1():  #O(n^2)
    arr = randArr.copy()
    sum = 0
    for i in range(n):
        for j in range(n):
            if (i==j):  continue
            if(arr[i] == arr[j]):
                arr[i] = None
        if(arr[i] != None):
           sum += 1
    print(sum)
    return

def sol_2(): #O(nlogn)
    arr = randArr.copy()
    arr.sort()
    sum = 1
    for i in range(1,n):
        if(arr[i] != arr[i-1]):
            sum += 1
    print(sum)
    return

def sol_3():  #O(n)
    arr = randArr.copy()
    D = {}
    sum = 0
    for i in range(n):
        if not arr[i] in D:
            sum += 1
            D[arr[i]] = True
    print(sum)
    return

def sol_4():  #O(n)
    arr = randArr.copy()
    tempArr = [0] * (n*2+1)
    sum = 0
    for i in range(n):
        tempArr[arr[i]+n] += 1
    for i in range(n*2+1):
        if(tempArr[i] != 0):
            sum += 1
    print(sum)
    return

def timeChk(func):
    before = time.process_time()
    func()
    after = time.process_time()
    print(after - before)
    return

n = int(input())
randArr = list(range(0,n))
for i in range(n):
    randArr[i] = random.randrange(-n, n+1)


#print(randArr)
#timeChk(sol_1)
timeChk(sol_2)
timeChk(sol_3)
timeChk(sol_4)
