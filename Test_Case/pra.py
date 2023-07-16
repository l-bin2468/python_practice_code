import sys
from ctypes import *
import ctypes


class PyObject(Structure):
    _fields_ = [
        ("char", c_char_p),
        ("refcnt", c_int),
        ("typeid", c_bool)
    ]


i = "1".encode()
j = 123
k = True

l = 0
while l < 5:
    li = [i, j, k]
    # print(li[0])

    struct = PyObject(i, j, k)

    val = byref(struct)
    # print(sys.getsizeof(val))
    # print("real_i", struct.char)
    # print("real_j", struct.refcnt)
    # print("real_k", struct.typeid)
    # print(i)
    i += i
    j += j
    print(i, j, k)

    l += 1
