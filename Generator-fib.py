# Python生成器，以斐波那契数列生成器为例
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

L=fib(6)
for i in L:
    print(i)