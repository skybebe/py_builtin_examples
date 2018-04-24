# # -*- coding:utf-8 -*-

print('\n---------------------Type:真值测试--------------------')
if not None and not '' and not [] and not {} and not () and not 0.0:
	print('None '' () {} [] 0.0 is false')

print('\n---------------------Type:数值运算(位运算、数学运算)--------------------')
print(float(1))
print(round(1.123456, 5))

import math
print(math.floor(1.123456))
print(math.ceil(1.123456))
# 移位
if 1<<3 is 8:
	print('1<<3 is 8')
# 位或
print(3|1)#3
# 异或
print(3^1)#2
# 与或
print(3&1)#1
# 位长
num = 3
print(num.bit_length())#2
print((3).bit_length())#2
# 字节数组
print((3).to_bytes(3, byteorder='big'))#b'\x00\x00\x03'
print(int.from_bytes(b'\x00\x00\x03', byteorder='big'))#b'\x00\x00\x03'
if (-2.0).is_integer():
	print('(-2.0).is_integer')

if not (-2.1).is_integer():
	print('not (-2.1).is_integer()')


print('\n---------------------Type:序列(list、tuple、range、str、bytes、bytearray)--------------------')

print(("aB3").casefold())

print((',').join(['a','1','2']))

list = ['a', 'b', 'c']
list.remove('b')
print(list)
list.reverse()
print(list)
list.insert(1, 'd')
print(list)

print('\n---------------------Type:集合(set、frozenset)--------------------')

print('\n---------------------Type:映射(dict)--------------------')

print('\n---------------------Type:容器类(namedtuple、deque、ChainMap、Counter、OrderedDict、defaultdict)--------------------')



