class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self
    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # size 필드가 없음에 유의.

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return " -> ".join(str(v.key) for v in self)

    def printList(self, title=''):
        if title: print(title)
        v = self.head.next
        print(" [h -> ", end="")
        while v != self.head:
            print(str(v.key)+" -> ", end="")
            v = v.next
        print("h]")
        
    def splice(self,a,b,x):
        if a==None or b==None or x==None:
            return
        ap = a.prev
        bn = b.next
        #cut
        ap.next = bn
        bn.prev = ap
        #paste
        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a
  
    def search(self, key):
        v = self.head.next
        while(v != self.head):
            if(v.key == key):
                return v
            v = v.next
        return None
        
    def moveAfter(self, a, b):#다시
        if(a.prev == b): return
        self.splice(a,a,b)
    
    def moveBefore(self, a, b):#다시
        if(a.next == b): return
        self.splice(a,a,b.prev)
        
    def insertAfter(self, key, x): #moveAfter(Node(key), x) == splice(Node(a), Node(a), x)
        newNode = Node(key)
        if(type(x)==int):
            x = self.search(x)
        self.moveAfter(newNode,x)
    
    def insertBefore(self, key, x):
        newNode = Node(key)
        if(type(x)==int):
            x = self.search(x)
        self.moveBefore(newNode,x)

    def pushFront(self, key): #insertAfter(key, self.head)
        self.insertAfter(key, self.head)
        
    def pushBack(self, key):
        self.insertBefore(key, self.head)

    def remove(self, x):
        if(x == None): return False
        x.prev.next = x.next
        x.next.prev = x.prev
        return x

    def popFront(self):
        return self.remove(self.first()).key

    def popBack(self):
        return self.remove(self.last()).key

    def isEmpty(self):
        if(self.head.next == self.head): return True
        return False

    def first(self):
        return self.head.next

    def last(self):
        return self.head.prev

    def findMax(self):
        if (self.isEmpty()): return None
        v = M = self.head.next
        while(v != self.head):
            if M.key < v.key : 
                M = v
            v = v.next
        return M
    
    def deleteMax(self):
        m = self.findMax()
        if m == None:
            return None
        return self.remove(m)

    def sort(self):
        sortedList = DoublyLinkedList()
        while(self.head.next != self.head):
            sortedList.pushFront(self.deleteMax().key)
        return sortedList
    
if __name__ == '__main__':
    L = DoublyLinkedList()
    while True:
        cmd = input('> ').split()
        if cmd[0] == 'moveA': # moveAfter
            a = L.search(int(cmd[1]))
            x = L.search(int(cmd[2]))
            if a == None: print(f" # a_key {cmd[1]} is not found")
            elif x == None: print(f" # x_key {cmd[2]} is not found")
            elif a == x: print(f" # a_key {cmd[1]} is same as x_key {cmd[2]}")
            else:
                L.moveAfter(a, x)
                print(f" + {cmd[2]} is moved After {cmd[1]}")
        elif cmd[0] == 'moveB': # moveBefore
            a = L.search(int(cmd[1]))
            x = L.search(int(cmd[2]))
            if a == None: print(f" # a_key {cmd[1]} is not found")
            elif x == None: print(f" # x_key {cmd[2]} is not found")
            else:
                L.moveBefore(a, x)
                print(f" + {cmd[2]} is moved Before {cmd[1]}")
        elif cmd[0] == 'pushF':
            L.pushFront(int(cmd[1]))
            print(f" + {cmd[1]} is pushed at Front")
        elif cmd[0] == 'pushB':
            L.pushBack(int(cmd[1]))
            print(f" + {cmd[1]} is pushed at Back")
        elif cmd[0] == 'popF':
            key = L.popFront()
            if key == None:
                print(" # List is empty")
            else:
                print(f" - {key} is popped from Front")
        elif cmd[0] == 'popB':
            key = L.popBack()
            if key == None:
                print(" # List is empty")
            else:
                print(f" - {key} is popped from Back")
        elif cmd[0] == 'search':
            v = L.search(int(cmd[1]))
            if v == None: 
                print(f" # {cmd[1]} is not found!")
            else:
                print(f" * {cmd[1]} is found!")    
        elif cmd[0] == 'insertA':
                # insertA new_key x_key : new_key의 새 노드를 x_key 노드 뒤에 삽입
            x = L.search(int(cmd[2]))
            if x == None: print(f" # x_key {cmd[2]} is not found")
            else:
                L.insertAfter(int(cmd[1]), x)
                print(f" + {cmd[1]} is inserted After {cmd[2]}")
        elif cmd[0] == 'insertB':
            # inserta new_key x key : key의 새 노드를 x_key를 갖는 노드 앞에 삽입
            x = L.search(int(cmd[2]))
            if x == None: print(f" # x_key {cmd[2]} is not found")
            else:
                L.insertBefore(int(cmd[1]), x)
                print(f" + {cmd[1]} is inserted Before {cmd[2]}")
        elif cmd[0] == 'removeK':
            x = L.search(int(cmd[1]))
            if L.remove(x):
                print(f" - {cmd[1]} is successfully removed")
            else:
                print(f" # {cmd[1]} is not in the list")    
        elif cmd[0] == "first":
            if L.isEmpty():
                print(f" # Empty list!")
            else:
                print(f" * {L.first()} is the front key")
        elif cmd[0] == "last":
            if L.isEmpty():
                print(f" # Empty list!")
            else:
                print(f" * {L.last()} is the last key")
        elif cmd[0] == "findMax":
            m = L.findMax()
            if m == None:
                print(f" # Empty list!")
            else:
                print(f" * Max key is {m}")
        elif cmd[0] == "deleteMax":
            m = L.deleteMax()
            if m == None:
                print(f" # Empty list!")
            else:
                print(f" - Max key {m} is deleted")
        elif cmd[0] == 'sort':
            L.printList(" * Before sorting:")
            L = L.sort()
            L.printList(" * After sorting:")
        elif cmd[0] == 'print':
            L.printList()
        elif cmd[0] == 'exit':
            break
        else:
            print("* not allowed command.")

