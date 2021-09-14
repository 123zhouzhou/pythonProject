# -*- coding:utf-8 -*-

def trim(s):
    start = 0
    tail = len(s)

    while start<tail and s[start]==" ":
        start+=1
    while tail>0 and s[tail-1]==" ":
        tail-=1

    return s[start:tail]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')