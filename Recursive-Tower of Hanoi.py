# -*- coding:utf-8 -*-

# 不要考虑单个如何移动，具体移动交给递归函数，只要把握整体，将n-1看成整体移动就ok了
def move(n, a, b, c):
    # 若n=1，则直接A到C
    if n == 1:
        print(a, '-->', c)

    else:
        move(n-1, a, c, b)  # 表示先将n-1个整体从A移到B作为过渡，如何标字母可以参考n=1的情况
        move(1, a, b, c)    # 表示将最底下的那个从A移到C
        move(n-1, b, a, c)  # 表示再将n-1个整体从B移到C，完成移动

move(3, 'A', 'B', 'C')