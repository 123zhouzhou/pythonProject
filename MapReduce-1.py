
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字

# -*- coding: utf-8 -*-

def normalize(name):
    name=name.lower()
    N_name=name[0].upper()+name[1:]
    return N_name

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)