#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a','A','b','B']

# Реализация задания 2
print('data:',data1)
print('unique:',', '.join(map(str,Unique(data1))))
print()

print('data:',data2)
print('unique:',', '.join(map(str,Unique(data2))))
print()

print('data:',data3,'ignore_case:',True)
print('unique:',', '.join(map(str,Unique(data3,ignore_case=True))))
print()

print('data:',data3,'ignore_case:',False)
print('unique:',', '.join(map(str,Unique(data3,ignore_case=False))))
print()
