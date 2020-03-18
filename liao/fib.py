# -*- coding: utf-8 -*-
"""斐波那契数列Fibonacci，生成器"""

def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a+b
        n = n+1
    return "done"


"""如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中"""
"""如果不想取得返回值，仅想打印生成器"""
g = fib(9)
# while(True):
#     try:
#         x = next(g)
#         print("g=", x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
for x in g:
    print("g=", x)
