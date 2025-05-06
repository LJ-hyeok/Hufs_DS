class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        def __str__(self):
            return str(self.key)
	
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def printList(self,title=''): # 변경없이 사용할 것!
        if title:
            print(title)
        v = self.head
        print(" [", end="")
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None]")
  
    def pushFront(self, key):  
        newNode = Node(key)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def pushBack(self, key):
        newNode = Node(key)
        v = self.head
        if v == None:
            newNode.next = self.head
            self.head = newNode
        else:
            while(v):
                lastNode = v
                v = v.next
            newNode.next = lastNode.next
            lastNode.next = newNode
        self.size += 1
    
    def popFront(self): 
        if(self.size == 0):    return None
        frontNode = self.head
        x = frontNode.key
        self.head = frontNode.next
        self.size -= 1
        return x
    
    def popBack(self):
        if(self.size == 0): return None
        u = self
        v = self.head
        for i in range(self.size-1):
            u = v
            v = v.next
        x = v.key
        if(u == self): self.head = None
        else: u.next = None
        self.size -= 1
        return x
        
    def search(self, key):
        v = self.head
        while(v):
            if (v.key == key):
                return v
            v = v.next
        return None
    
    def removeKey(self, key):
        x = self.search(key)
        if (x == None): return False
        u = self
        v = self.head
        while(v):
            if(v == x):
                if(u==self): self.head = v.next
                else: u.next = v.next
            u = v
            v = v.next
        self.size -= 1
        return True

    def reverse(self, key):
        x = self.search(key)
        if x == None: return
        
        left = u = self
        v = self.head
        flag = False
        l = []
        while(v):
            if(x == v): flag = True
            if(flag): l.append(v.key)
            else: left = v #left 는 결과적으로 x 바로 앞 노드
            u = v 
            v = v.next 
        for i in range(len(l)): #리스트를 역순으로 pushBack
            self.pushBack(l.pop())
            if(i==0): #left 다음 노드를 u.next 노드(= 새롭게 pushBack하는 노드들) 로 연결
                if(left == self):    self.head = u.next
                else:    left.next = u.next
        v = self.head        
        cnt = 0
        while(v):	#self.size 다시 구함
            v = v.next
            cnt += 1
        self.size = cnt
        
    def findMax(self):
        if(self.size == 0): return None
        v = self.head
        M = v.key
        while(v):
            if(M < v.key): M = v.key
            v = v.next
        return M
        
    def deleteMax(self):
        if(self.size == 0): return None
        x = u = self
        y = v = self.head
        M = v.key
        while(v):
            if(M < v.key): 
                M = v.key
                x = u
                y = v
            u = v
            v = v.next
        if(x == self): self.head = y.next
        else: x.next = y.next
        self.size -= 1
        return M
    
    def insertAfter(self, key, x):
        if(x == None): self.pushFront(key)
        else:
            newNode = Node(key)
            newNode.next = x.next
            x.next = newNode
            self.size += 1
    
    def sort(self):	
        newList = SinglyLinkedList()
        while(self.size != 0):
            newList.pushFront(int(self.deleteMax()))
        return newList
    
    def size(self): # 리스트의 노드 갯수 리턴
        return self.size
	
# 아래 코드는 수정하지 마세요!
if __name__ == '__main__':
	L = SinglyLinkedList()
	while True:
		cmd = input('> ').split()
		if cmd[0] == "pushFront":
			L.pushFront(int(cmd[1]))
			print(f" + {cmd[1]} is pushed at front.")
		elif cmd[0] == "pushBack":
			L.pushBack(int(cmd[1]))
			print(f" + {cmd[1]} is pushed at back.")
		elif cmd[0] == "popFront":
			x = L.popFront()
			if x == None:
				print(" # List is empty.")
			else:
				print(f" - {x} is popped from front.")
		elif cmd[0] == "popBack":
			x = L.popBack()
			if x == None:
				print(" # List is empty.")
			else:
				print(f" - {x} is popped from back.")
		elif cmd[0] == "search":
			x = L.search(int(cmd[1]))
			if x == None:
				print(f" * {cmd[1]} is not found!")
			else:
				print(f" * {cmd[1]} is found!")
		elif cmd[0] == "removeKey":
			if L.removeKey(int(cmd[1])):
				print(f" - {cmd[1]} is removed.")
			else:
				print(f" - {cmd[1]} is not in the list.")
		elif cmd[0] == "reverse":
			L.printList(f" * Before reversing from {cmd[1]}:")
			L.reverse(int(cmd[1]))
			L.printList(f" * After reversing from {cmd[1]}:")
		elif cmd[0] == "sort":
			L.printList(f" * Before sorting:")
			L = L.sort()
			L.printList(f" * After sorting:")
		elif cmd[0] == "findMax":
			m = L.findMax()
			if m == None:
				print(" # Empty list!")
			else:
				print(f" * Max key is {m}.")
		elif cmd[0] == "deleteMax":
			m = L.deleteMax()
			if m == None:
				print(" # Empty list!")
			else:
				print(f" - Max key {m} is deleted.")
		elif cmd[0] == "insertAfter":
			# insertAfter nkey xkey 형식으로 입력받음
			new_key = int(cmd[1])
			x_key = int(cmd[2])
			x = L.search(x_key)
			L.insertAfter(new_key, x) # x가 None이면 head에 삽입되어야 함!
			print(f" + {new_key} is inserted after {x_key}.")
		elif cmd[0] == "print":
			L.printList()
		elif cmd[0] == "size":
			print(f" * Size of the list is {L.size}.")
		elif cmd[0] == "exit" or cmd[0] == "quit":
			print(" * Bye!")
			break
		else:
			print(f" # Unknown command: {cmd[0]}")