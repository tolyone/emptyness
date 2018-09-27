# 3.a
def foo(a,b):
    return((a>b))

# 3.b
def bar(c):
    global a
    global b
    if c>0:
        max = a
    else:
        max = b
    return max

print('a=', end = '')
a=int(input())
print('b=', end = '')
b=int(input())

max=bar(foo(a,b))
if a==max:
    print(a, ' > ', b, end = '')
else:
    print(b, ' > ', a, end='')