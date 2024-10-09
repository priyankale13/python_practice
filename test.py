import math
print("math library")
print(dir(math))
 
print("\n")

import random
print("random library")
print(dir(random))
#
from inspect import getmembers,isfunction,ismodule,isgenerator
print("math functions")
print(getmembers(math,isfunction))
print(getmembers(math,ismodule))
print(getmembers(math,isgenerator))
