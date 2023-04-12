import random

import numpy as np
#
# """
# print(np.array([[[11, 2, 33], [43, 54, 6]], [[11, 22, 3], [14, 15, 16]]]))
#
# # Verificarea numărului de dimensiuni ale matricei: .ndim
# # 0-d array
# x = np.array(4)
# # 1-d array
# y = np.array([1, 2, 3])
# # 2-d array
# z = np.array([[11, 62, 3], [46, 95, 96]])
# # 3-d array
# c = np.array([[[11, 2, 3], [48, 85, 6]], [[17, 78, 78], [44, 95, 6]]])
#
# print(x.ndim)
# print(y.ndim)
# print(z.ndim)
# print(c.ndim)
#
# ar1 = np.array(['chair', 'book', 'notebook'])
# print(ar1.dtype)
# print(c.dtype)
#
# x = np.empty([4, 4], dtype=int)
# print(x)
#
# x = np.zeros([4, 4], dtype=int)
# print(x)
#
# x = np.ones([4, 4], dtype=int)
# print(x)
# """
#
# ls = [[1, 3, 4], [1, 2, 3], [8, 9, 3], [5, 7, 1]]
# new_ls = np.asarray(ls)
# print(new_ls)
#
# print('Coloana 1 este: ', new_ls[..., 0])
# print('Coloana 2 este: ', new_ls[..., 1:])
# print('Coloana 3 este: ', new_ls[..., 2])
#
# print('Randul 1 este: ', new_ls[0, ...])
# print('Randul 2 este: ', new_ls[1:, ...])
# print('Randul 3 este: ', new_ls[2, ...])
#
# print()
#
#
# """
# new_ls = [1, 3, 2, 4, 2, 5]
# it = iter(new_ls)
# x = np.fromiter(it, dtype=int)
# print(x)
# print(x.dtype)
#
# print(np.array(new_ls))
#
# print(np.arange(-100, 100, 2, int))
# print(np.linspace(10, 50, 10, retstep=True))
# print(np.logspace(10, 20, num=5, endpoint=True))
# """
#
# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])
# c = a + b
# print(c)
#
# # sorting along the first axis
# a = np.array([[17, 35], [10, 25]])
# arr1 = np.sort(a, axis = 0)
# print ("Sorting Along first axis : \n")
# print(arr1)
#
# # sorting along the last axis
# b = np.array([[1, 15], [20, 18]])
# arr2 = np.sort(b, axis = -1)
# print ("\nSorting along last axis : \n")
# print(arr2)
#
#
# c = np.array([[12, 15], [10, 1]])
# arr3 = np.sort(c, axis = None)
# print ("\nSorting Along none axis : \n")
# print(arr3)
#
#
# input_arr = np.array([[5, 2, 7, 4], [9, 0, 2, 3], [1, 2, 3, 19]])
# print(input_arr)
# print(id(input_arr))
#
# b = np.ndarray.copy(input_arr)
# print(b)
# print(id(b))
#
# b.shape = 4, 3
# print(b)
# print(input_arr)
#
# v = input_arr.view()
# input_arr[0, 0] = 25
# print(input_arr)
# print(v)

# arr = np.arange(0, 45, 5)
# print('arr = \n', arr)
#
# for x in np.nditer(arr):
#     print(x)

# a = np.array([[11, 2, 3, 4], [29, 4, 15, 6], [11, 21, 39, 31]])
# print(a)

# transpusa matricei
# at = a.T
# print(at)
#
# for x in np.nditer(at, order='C'):
#     print(x, end=' ')
# print()
# # reshape
# a = np.arange(0, 60, 5)
# a = a.reshape(3, 4)
# print(a)
#
# for i in np.nditer(a, op_flags=['readwrite']):
#     i[...] = 2 + i
# print('Added two: ', a)

# a = np.arange(0, 9)
# a = a.reshape(3, 3)
# print(a)
# b = np.arange(10, 19)
# b = b.reshape(3, 3)
# print(b)
#
# c = a * b
# print('*\n', c)
#
# c = np.matmul(a, b)
# print(c)
#
# a = np.array([1,0,29,3,8,4])
# b = np.array([1,2,0,9,3,84])
# c = np.dot(a, b)
# print(c)
#
# print(np.dot(3, a))
#
#
# inp = np.array(['Dance-Tonight', 'Sleep-Tonight', 'Walk-Tonight','Study-Tonight'])
# print ("The original Input array : \n", inp)
#
# output = np.char.split(inp, sep='-')
# print("The output split array: ", output)
#
# import numpy.matlib
# x = numpy.matlib.eye(n = 3, M = 3, k = 0, dtype=int)
# print(x)
#
# y = numpy.matlib.identity(5)
# print(y)
#
# print(np.__version__)


# a = np.arange(0, 40, 5)
# a = a.reshape(2, 2, 2)
# print(a)

# Transforma o matrice multidimensionala intr-un array unidimensional
# new_a = a.flatten()
# print(new_a)
# print(a.ravel())

# Ordinea elementelor inversata
# print()
# print(np.flip(a, axis=1))

# Rotirea cu 90 de grade a matricei
# b = np.arange(1, 10)
# b = b.reshape(3, 3)
# print(b)
# print(np.rot90(b, k=2))

# Inversarea orizontala a matricei
# print(np.fliplr(b))

# Inversarea verticala a matricei
# print(np.flipud(b))

# Numere random
# x = np.random.randint(100, size=(3, 5))
# print(x)

# choice() - alege din numerele date
# y = np.random.choice([1, 2, 0, 9, 3, 4, 8, 7], size=(3, 5))
# print(y)

# Probabilitatea de a pica acele numere
# x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# print(x)

# random.shuffle()
# x = np.array([6, 8, 7, 3, 4, 9, 0, 2])
# np.random.shuffle(x)
# print(x)
# print(np.random.permutation(x))

# cumsum()
arr = np.arange(1, 10)
print(arr)
print(np.cumsum(arr))

# prod()
print(np.prod(arr))

# cumprod()
print(np.cumprod(arr))

# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot([1, 2, 3, 4, 5], hist=False)
# plt.show()
#
# sns.distplot(np.random.normal(size=1000), hist=False)
# plt.show()
