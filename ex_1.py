#!/usr/bin/env python3
import os

import sys

from librip.gens import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800,'color': None}#, 'color': 'white'}
]

# Реализация задания 1
for f in field(goods,'color'):#,'title'):
    print(f)

print(' '.join(map(str,gen_random(1,3,5))))

n = 5
for i,x in enumerate(gen_random(1, 5, n)):
    # os.write(1, str(x).encode())
    if i == n-1:
        print(x)
    else:
        print(x, end=', ')

