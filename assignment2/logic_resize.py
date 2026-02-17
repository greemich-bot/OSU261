from ctypes import resize
from static_array import *
from dynamic_array import *
from ref import *

testarr=StaticArray(9)

testarr[0]=0
testarr[1]=1
testarr[2]=2
testarr[3]=4

resize(testarr,12)
print(testarr)





