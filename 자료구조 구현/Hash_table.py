#
#Hash function: shift folding
#open addressing: linear probing
#

class HashOpenAddr:
	def __init__(self, size=10):
		self.size = size
		self.keys = [None]*self.size
		self.values = [None]*self.size

	def __str__(self):
		s = ""
		for k in self:
			if k == None:
				t = "{0:5s}|".format("")
			else:
				t = "{0:-5d}|".format(k)
			s = s + t
		return s

	def __iter__(self):
		for i in range(self.size):
			yield self.keys[i]
					
	def hash_function(self, key):
		# 이 과제에서는 단순한 함수 사용: h(key) = key % self.size
		return key % self.size
			
	def find_slot(self, key):
		i = self.hash_function(key)
		start = i
		while (self.keys[i] != key) and (self.keys[i] != None):
			i = (i+1)%self.size
			if(i==start):
				return None
		return i
        # key 값이 존재하는 경우: key가 저장된 슬롯 인덱스 리턴
        # key 값이 존재하지 않는 경우:
        #  1. 빈 슬롯이 없는 경우: None 리턴
        #  2. 빈 슬롯이 있는 경우: key 값이 저장될 슬롯 인덱스 리턴

	def set(self, key, value=0):
		i = self.find_slot(key)
		if i == None: return None
		self.keys[i] = key
		self.values[i] = value
		return True        
		# 빈 슬롯이 없으면 False 리턴, 아니면 True 리턴!

	def remove(self, key):
		i = self.find_slot(key)
		if self.keys[i] == None: return False
		self.keys[i] = self.values[i] = None
		i = (i+1)%self.size
		while self.keys[i]:
			x = self.find_slot(self.keys[i])
			if self.keys[x] == None:
				self.keys[x], self.keys[i] = self.keys[i], self.keys[x]
				self.values[x], self.values[i] = self.values[i], self.values[x]
			i = (i+1)%self.size
		return True
        # key 값이 없으면 False 리턴, 있으면 제거 후 True 리턴

	def search(self, key):
		i = self.find_slot(key)
		start = i
		while self.keys[i]:
			if self.keys[i] == key:
				i = (i+1) % self.size
			if start == i:
				break
		return None
        # key 값이 있으면 해당 value 값을 리턴하고, 없으면 None 리턴

	def __getitem__(self, key):
		return self.search(key)
	def __setitem__(self, key, value):
		self.set(key, value)

	def save_as_list(self):
		# 해시테이블 슬롯의 내용을 튜플 (key, value)의 리스트로 만들어 리턴
		return [(self.keys[i], self.values[i]) for i in range(self.size) if self.keys[i]]

if __name__ == "__main__":
	H = HashOpenAddr()
	while True:
		cmd = input().split()
		if cmd[0] == 'set':
			key = H.set(int(cmd[1]))
			if key == None: 
				print("* H is full!")
			else: 
				print("+ {0} is set into H".format(cmd[1]))
		elif cmd[0] == 'search':
			key = H.search(int(cmd[1]))
			if key == None: 
				print("* {0} is not found!".format(cmd[1]))
			else: 
				print(" * {0} is found!".format(cmd[1]))
		elif cmd[0] == 'remove':
			key = H.remove(int(cmd[1]))
			if key == None:
				print("- {0} is not found, so nothing happens".format(cmd[1]))
			else:
				print("- {0} is removed".format(cmd[1]))
		elif cmd[0] == 'print':
			print(H)
		elif cmd[0] == 'exit':
			print("Bye!")
			break
		else:
			print("* not allowed command. enter a proper command!")