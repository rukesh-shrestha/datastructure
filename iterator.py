from typing import NewType

print(NewType)


li = [45,32,56,31,22,24,56,232,567]

ob = iter(li)
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))
print('size',ob.__sizeof__())