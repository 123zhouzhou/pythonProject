from _collections_abc import Iterator

# 创建迭代器对象
it=iter([1,2,3,4,5])

while True:
    try:
        # next()方法调用返回下一个值
        print(next(it))
    except StopIteration:
        break

x=isinstance(it, Iterator)
print('it是否为可迭代对象：', x)