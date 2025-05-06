import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# Oenaddressing - linear probing 과제에서 작성한 해시테이블 클래스 작성할 것!
class HashOpenAddr:
	def __init__(self, size=200):
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
					
	def hash_function(self, key): # Universal hash
		h = 0
		a = 31
		for i in range(len(key)):
			h = (h*a + ord(key[i])) % self.size
		return h % self.size
			
	def find_slot(self, key):
		i = self.hash_function(key)
		start = i
		while (self.keys[i] != key) and (self.keys[i] != None):
			i = (i+1)%self.size
			if(i==start):
				return None
		return i

	def set(self, key, value=0):
		i = self.find_slot(key)
		if i == None: return False
		self.keys[i] = key
		self.values[i] = value
		return True        
		# 빈 슬롯이 없으면 False 리턴, 아니면 True 리턴!

	def search(self, key): 
		for i in range(self.size):
			if(self.keys[i] == key):
				return key
		return None
        # key 값이 있으면 해당 value 값을 리턴하고, 없으면 None 리턴

	def __getitem__(self, key):
		return self.search(key)
	def __setitem__(self, key, value):
		self.set(key, value)

	def save_as_dict(self):
		# 해시테이블 슬롯의 내용을 튜플 (key: value)의 딕셔너리로 만들어 리턴
		return {self.keys[i] : self.values[i] for i in range(self.size) if self.keys[i]}

# 텍스트 파일 읽기
def read_file(filename: str) -> str:
	with open(filename, 'r', encoding='utf-8') as file:
		text = file.read().lower()
	return text

# 텍스트 전처리 (특수문자, 구두점 등 불필요한 심볼 제거)
def preprocess_text(text: str) -> list[str]:
	translator = str.maketrans('', '', string.punctuation)
	return text.translate(translator).split()

# 단어 빈도 계산 (작성할 것!)
def count_words(words: list[str], stop_words: set[str], start_rank: int, end_rank: int) -> dict[str, int]:
	# 1. words 리스트의 단어의 빈도수를 HashOpenAddr 객체를 만들어 센다
	# 2. start_rank부터 end_rank까지의 단어와 빈도수만 저장된 dict 자료구조 selected_words를 리턴한다
    H = HashOpenAddr()
    for i in range(start_rank-1, end_rank):
        if H.search(words[i]):
            H.values[H.find_slot(words[i])] += 1
        else:
            H.set(words[i], 1)
			
    selected_words = H.save_as_dict() # dict로 변경
    return selected_words

# Word Cloud 생성 및 출력
def generate_wordcloud(freq_dict: dict[str, int]) -> None:
	wordcloud = WordCloud(width=800, height=800, background_color='white')
	wordcloud.generate_from_frequencies(freq_dict)

	plt.figure(figsize=(10, 10))
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis('off')
	plt.show()

# Main 함수
def main() -> None:
	text = read_file(input("텍스트 파일명: "))  # 파일명을 적절히 변경
	words = preprocess_text(text)
	
	# stopwords 설정 및 추가
	stop_words = set(stopwords.words('english'))
	stop_words.update(['ye', 'said', 'll', 'th', 'thus', 'ay', 'till', 'whose', 'which', 'that', 'mine', 'let', 
	'thy', 'thee', 'upon', 'say', 'go', 'tis', 'st', 'us', 'one', 'will', 'thou', 'though', 'now', 
	'well', 'may', 'might', 'yet', 'much', 'must', 'way', 'long', 'sir', 'come', 'hath', 'shall',
	'to', 'of', 'the', 'at', 'from', 'these', 'and', 'in', 'other', 'an', 'a', 'with', 'two', 'each'])

	# 랭킹 범위 입력 (예: 1위~200위: 자연수 입력)
	start_rank = int(input("시작 랭킹 입력: "))
	end_rank = int(input("끝 랭킹 입력: "))

	selected_words = count_words(words, stop_words, start_rank, end_rank)
	generate_wordcloud(selected_words)

if __name__ == "__main__":
	main()