import numpy as np

dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], ndmin=2 ,dtype = dt)
print(a)
print(a['age'])

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a['name'])

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
print(a)

a.shape = (3,2)

print(a)

b = a.reshape(2,3)

print(a)
print(b)

a = np.arange(24)
print(a.ndim)
print(a)

b=a.reshape(2,4,3)

print(b.ndim)

a = np.array([1,2,3,4],dtype=np.int8)

print(a)

print(a.itemsize)
