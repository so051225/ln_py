

modules matplotlib

import math


dir(math)

import sys as s



# all system builtins module name
s.builtin_module_names

s.modules.keys()

s.__file__
# no s.__file__

import numpy as np
print(np.__file__)
# /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/numpy/__init__.py


def dir2(path):
    from os import listdir
    print(listdir(path))


"""
import scipy as sp
dir(sp).index('pv')
help(sp.pv)
help(sp.npv)

scipy.npv is deprecated and will be removed in SciPy 2.0.0, use numpy.npv instead

`npv` is deprecated; for details, see NEP 32 [1]_.
       Use the corresponding function in the numpy-financial library,
       https://pypi.org/project/numpy-financial.

"""

import numpy_financial as nf
nf.npv(.1, [-100,50,40,20,10,50])
# 31.414893418854874

nf.pmt(4.5/100/12, 30*12, 250000)
# -1266.7132745647143
# excel: pmt(4.5/100/12, 30*12, 250000)

g = np.array([[1,2,3], [4,5,6]])
h1 = np.zeros_like(g)
h2 = np.ones_like(g)

'''
>>> h1
array([[0, 0, 0],
       [0, 0, 0]])
>>> h2
array([[1, 1, 1],
       [1, 1, 1]])
>>> 
'''

pv=np.array([[100, 10, 10.2], [34, 22, 34]])
flat_pv = pv.flatten()
pv2 = np.reshape(flat_pv, [2,3]) # 2 rows & 3 columns

'''

>>> flat_pv
array([100. ,  10. ,  10.2,  34. ,  22. ,  34. ])
>>> pv2
array([[100. ,  10. ,  10.2],
       [ 34. ,  22. ,  34. ]])

'''

import numpy as np
x = np.array(dir(np))
for k in x:
    if k.find('uni') != -1:
        print(k)