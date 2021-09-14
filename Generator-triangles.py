# -*- coding: utf-8 -*-

# for i in range(1,3):
#     print(i)

def triangles():
    L=[1]
    
    while True:
        b=L.copy()
        yield b
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]

# def triangles():
#     Fir=[1]
#     yield Fir
#     t=[1,1]
#     while True:
#         yield t
#         tmp=[1]
#         for i in range(1,len(t)):
#             ttmp=t[i]+t[i-1]
#             tmp.append(ttmp)
#         tmp.append(1)
#         t=tmp

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')