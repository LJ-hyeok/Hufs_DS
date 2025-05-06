def hash(x):
    f = 0
    for i in x:
        f = (f*31+ord(i))%5
        print(ord(i)%31, f)
    return f


tmp = hash('apple')
print(tmp)
for i in range(5):
    print(tmp%31)
    tmp//=31