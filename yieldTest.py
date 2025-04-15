def yield_test():
    for i in range(5):
        yield i
        print(i,"번째 호출")

t = yield_test()
print(type(t))
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print("<----->")

for k in yield_test():
    print(k)

print("<--->")