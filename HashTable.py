#to open result of mid term exam
#
#Hash function: shift folding
#open addressing: linear probing
#
#

class Slot:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

def hash_func(key):
    # key = 학번 (정수)
    s = 0
    for i in range(4):# shift folding -> 202202976 -> (2+02+20+29+76)%100 -> 29
        s += key % 100
        key //= 100
    return (s+key)%100

def set(table, slot):
    i = find_loc(table, slot.key)
    if i == None:
        return None
    if(table[i].value != None):
        table[i].value = slot.key
    else:
        table[i].key = slot.key 
        table[i].value = slot.value
    return slot.key

def find_loc(table, key):
    i = hash_func(key)
    start = i
    while(table[i].key != None) and (table[i].key != key) :
        i = (i+1)%100
        if i == start:
            return None
    return i


id = open("student_id.txt")
grade = open("mid_grade.txt")

id_list = []
while(True):
    L = id.readline()
    if(L == ''):
        break
    L = int(L[0:9])
    id_list.append(L)
id.close()

MyHash = [Slot() for i in range(100)] # HashTable
for i in range(len(id_list)):
    set(MyHash, Slot(id_list[i]))



#for i in range(100):
#    print(MyHash[i].key)

'''
MyNum = 202202976
for i in range(100):
    L = grade.readline()
    if(MyHash[i].key == MyNum):
        print(i, L)
'''

sco = []
for i in range(100):
    L = grade.readline()
    L = L[0:-1]
    if(L == 'None'):    continue
    else: L=float(L)
    sco.append(L)

sco.sort()
print(sco)