# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    def f(x, y):
        return x*10+y
    
    def char2sum(s):


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')