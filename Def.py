# -*- coding:utf-8 -*-

import math

def quadratic(a,b,c):
    h=b**2-4*a*c
    if a==0:
        x=-c/b
        return x
    if h==0:
        x=-b/(2*a)
        return x
    elif h>0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
    else:
        print('该方程无解')

print('ax2+bx+c=0')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

print('quadratic(a, b, c) =', quadratic(a, b, c))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')