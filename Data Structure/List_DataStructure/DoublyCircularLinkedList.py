# Node class
class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = self
		self.prev = self
		
	def __str__(self):
		return str(self.key)
# DoublyLinkedList class

class DoublyLinkedList:
	def __init__(self):
		self.head = Node()
		self.index = self.head
	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	
	def print(self):
		if(self.index.next == self.index): return
		v = self.index
		while v.next != self.index:
			#if(v == self.head): continue
			print(v.key,end="")
			v = v.next
		print(v.key)
	
	def search(self, x):
		pass
	
	def splice(slef, a, b, x):
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

	def IR(self, key):
		x = Node(key)
		y = self.index
		self.splice(x, x, y)
		self.index = x  #다음 노드 지정
		
	def IL(self, key):
		x = Node(key)
		y = self.index.prev
		self.splice(x, x, y)
		self.index = x  #다음 노드 지정

# input 처리 부분
L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'IR':
		L.IR(cmd[1])
	elif cmd[0] == 'IL':
		L.IL(cmd[1])
	elif cmd[0] == 'L':
		pass
	elif cmd[0] == 'R':
		pass
	elif cmd[0] == 'D':
		pass
	elif cmd[0] == 'C':
		pass
	elif cmd[0] == 'P':
		L.print()
	elif cmd[0] == 'Q': # 수정하지 말 것!!
		print('Bye!')
		break
	else:
		print(f"Unknown command: {cmd[0]}")