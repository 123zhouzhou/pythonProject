#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# name = input('Please input your name: ')
# len = len(name)
# print('Sum:%d,' % len)

# 数据类型
# a = 72
# A = 85
# high = (A-a)/a
# print('小明成绩提升了%.1f %%' % (high))

# 条件判断
# height = float(input('请输入小明的身高：'))
# weight = float(input('请输入小明的体重：'))
# bmi = weight/(height**2)
# if bmi<18.5 :
#     print('小明BMI指数为 %.1f, 过轻' % bmi)
# elif bmi<25:
#     print('小明BMI指数为 %.1f, 正常' % bmi)
# elif bmi<28:
#     print('小明BMI指数为 %.1f, 过重' % bmi)
# elif bmi<32:
#     print('小明BMI指数为 %.1f, 肥胖' % bmi)
# elif bmi>32:
#     print('小明BMI指数为 %.1f, 严重肥胖' % bmi)
# else:
#     print('无法衡量')

# 计算1-100内的整数之和
# sum = 0
# for x in range(101):
#     sum = sum+x
# print(sum)

# 计算100以内的奇数之和
# 方法1
# sum = 0
# n = 99
# while(n > 0):
#     sum = sum + n
#     n = n-2
# print(sum)

# #方法2
# sum = 0
# for x in range(101):
#     if x%2 != 0:
#        sum = sum + x
# print(sum) 

# #字典
# d = {'Sunny':100, 'Micao':99, 'Bob':20}
# print(d['Sunny'])
# d['Nina'] = 97
# d.pop('Sunny')
# print(d)
# print(d.get('Marry',-1))

# set
s1 = set([(1,2,3),5,6])
print(s1)
s2 = set([[1,2,3],5,6])
print(s2)