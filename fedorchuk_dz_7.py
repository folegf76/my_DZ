# 1
def geometric_prog(start, stop, n):
    index = 1
    while index <= stop:
        start = start * n
        yield start
        index += 1


g = geometric_prog(1, 10, 2)

for i in g:
    if i > 200:
        g.close()
    print(i)


# 2
def range_my(*args):
    start = 0
    step = 1

    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 1:
        stop = args[0]
    else:
        raise TypeError

    while start < stop:
        yield start
        start += step


for i in range_my(4, 40, 2):
    print(i)


# 3
def simple_n(n):
    i, j = 1, 1
    while i <= n:
        while j < i:
            if i % j == 0:
                break
            j += 1
        else:
            yield i
        j = 2
        i += 1


g = simple_n(100)
for i in g:
    print(i)

# 4
a = [x**3 for x in range(2, 10)]
print(a)


