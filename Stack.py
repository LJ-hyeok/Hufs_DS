class Stack:
    def __init__(self, size=500):
        self.items = [None] * 500
        self.index = -1
    def push(self, key):
        if (self.index+1 != len(self.items)):
            self.index += 1
            self.items[self.index] = key
    def pop(self):
        if (self.index) == -1:
            return None
        else:
            x = self.items[self.index]
            self.index -= 1
            return x
        
def pop_stack(s1,s2):
    tmp = ''
    for i in range(s1.index+1):
        s2.push(s1.pop())
    for i in range(s2.index+1):
        tmp+=s2.pop()
    return tmp

def get_token_list(expr):
    l = []
    left = Stack()
    right = Stack()
    op = ['+', '-', '*', '/', '^', '(' , ')']
    for i in range(len(expr)):
        if(expr[i] == ' '): continue
        is_op = False
        for j in range(7):
            if(expr[i] == op[j]):
                is_op = True
        if(is_op):
            if(left.index>-1):
                l.append(pop_stack(left, right))
            l.append(expr[i])
        else:
            left.push(expr[i])
    if(left.index>-1):  l.append(pop_stack(left, right))
    return l
	
def infix_to_postfix(token_list):
    l = []
    left = Stack()
    right = Stack()
    c1 = 0
    c2 = 0
    op = [['(' , ')'], ['+', '-'], ['*', '/'], ['^']]
    for i in range(len(token_list)):
        is_op = False
        priority = 0
        for j in range(4):
            for k in range(len(op[j])):
                if(token_list[i]==op[j][k]):
                    is_op = True
                    priority = j
        if(is_op): #연산자
            if(token_list[i] == '('): #여는 괄호인 경우
                c1 += 1
                right.push([0, '('])
            elif(token_list[i] == ')'): #닫는 괄호인 경우
                c2 += 1
                while(right.index >= 0 and right.items[right.index][1] != '('):
                    left.push(right.pop()[1])
                right.pop()
            else:
                while(right.index >= 0 and right.items[right.index][0] >= priority): #우선순위가 높거나 같으면
                    left.push(right.pop()[1])
                right.push([priority, token_list[i]])
                
        else: #피연산자
            left.push(token_list[i])
    while(right.index >= 0): #스택에 남은 연산자
        left.push(right.pop()[1])

    for i in range(left.index+1):
        l.append(left.items[i])
    if(c1 != c2):
        print("INVALID_EXPRESSION")
        quit()
    return l
    
def compute_postfix(token_list):
    left = Stack()
    right = Stack()
    op = ['+', '-', '*', '/', '^']
    for i in range(len(token_list)-1,-1,-1):
        left.push(token_list[i])
    if(left.index < 0) :
        print("INVALID_EXPRESSION")
        quit()
    for i in range(left.index+1):
        is_op = False
        top = left.items[left.index]
        if(top == '(' or top==')'):
            print("INVALID_EXPRESSION")
            quit()
        for j in range(5):
            if(top == op[j]):
                is_op = True
        if(is_op):
            if(right.index+1 < 2):
                print("INVALID_EXPRESSION")
                quit()
            try:
                a = float(right.pop())
                b = float(right.pop())
            except:
                print("INVALID_EXPRESSION")
                quit()
            if top == '+':
                right.push(b+a)
            elif top == '-':
                right.push(b-a)
            elif top == '*':
                right.push(b*a)
            elif top == '/':
                if(a == 0):
                    print("ZERO_DIVISION_ERROR")
                    quit()
                right.push(b/a)
            elif top == '^': 
                right.push(b**a)
            left.pop()
        else:
            try:
                right.push(float(left.pop()))
            except:
                print("INVALID_EXPRESSION")
                quit()
    return right.items[right.index]


s = input()
token = get_token_list(s)
postfix = infix_to_postfix(token)
result = compute_postfix(postfix)
print(f"{result:.3f}")