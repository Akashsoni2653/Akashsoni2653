# import mpmath
try:
  from sympy.mpmath import mp # old SymPy
except ImportError:
  from mpmath import mp # newer version

# set number of digits
mp.dps = 100000

# print pi to a thousand places
print(mp.pi)
