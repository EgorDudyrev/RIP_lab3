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
#for f in field(goods,'color'):#,'title'):
 #   print(f)
#print(', '.join(map(str,field(goods,'color'))))
print('field generator:')
print(', '.join(map(str,field(goods,'color','title'))))
print()

print('random generator:')
print(', '.join(map(str,gen_random(1,3,5))))
