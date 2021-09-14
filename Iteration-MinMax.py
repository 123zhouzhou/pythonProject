# -*- coding: utf-8 -*-

def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    elif len(L)==1:
        min=max=L[0]
        return (L[0], L[0])
    # 秀高级
    elif len(L)>1:
        L.sort()
        return (L[0], L[len(L)-1])
    # elif len(L)>1:
    #     min=max=L[0]
        
    #     # 迭代：通过for循环来遍历list/tuple
    #     for i in L:
    #         if(i<min):
    #             min=i
    #         if(i>max):
    #             max=i
    #     return(min,max)
    

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
