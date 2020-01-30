

#
# some ex for python syntax
#

import math
# import math as m
# from math import sqrt
# sqrt(3)

dir(math)


7//3 == int(7//3) == math.floor(7/3)

# round 有builtin, 但 no floow()?

# dir() 和 help() 可以配合使用
# dir('') -> strip()
# help(''.strip)

#
# tuple = ('Jojo', 21)
# tuple 是 不可改值的 
#


#
# Future value: PV = FV / (1 + r) ** n
#
#

def pv_f(fv, r, n):
    pv = fv / (1 + r) ** n
    return pv

pv_f(100, 0.1, 1) == pv_f(r=0.1, fv=100, n=1) == pv_f(100, r=0.1, n=1)

"""
>>> pv_f(r=0.1, fv=100, n=1) == pv_f(100, r=0.1, 1)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
"""
