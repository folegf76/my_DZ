# 1
# def generator(start, n, funcs):
#     while n > 0:
#         yield start
#         start = funcs(start)
#         n = n - 1
#
#
# g = generator(1, 10, lambda x: x * 2)
#
# for i in g:
#     if i > 100:
#         g.close()
#     print(i)

# 2
# import timeit
#
# s1 = '''
# def fibo(n):
#     if n < 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(20))
# '''
#
# s2 = '''
def fibo_2():
    memo = {}

    def number(n):
        if n in memo:
            return memo[n]
        elif n < 2:
            memo[n] = 1
        else:
            memo[n] = number(n - 1) + number(n - 2)
        return memo[n]
    return number


f = fibo_2()
print(f(20))
# '''
#
# print(timeit.timeit(s1, number=10))
# print(timeit.timeit(s2, number=10))

# 3

# def my_summ(a, f):
#     temp = []
#     for i in a:
#         temp.append(f(i))
#     return sum(temp)
#
#
# a = [2, 3, 50, 6, 8, 10]
# print(my_summ(a, lambda x: x ** 2))
