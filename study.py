import numpy as np

dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], ndmin=2 ,dtype = dt)
print(a)
print(a['age'])

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a['age'])

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

print(a.flags)

b = a

print(b.flags)

x = np.empty([3,5],dtype=int)
print(x)

x = np.zeros([3,5],dtype=int)
print(x)

x = np.zeros((3,5),dtype=[('x','i1'),('y','i4'),('z','i4')])
print(x)

s = 'Hello World1'
a = np.frombuffer(s, dtype = 'S3')
print(a)


a = np.array([[3,7],[9,1]])

print(a)

print(np.sort(a, axis = 0))



a = np.array([[30,0,40],[0,20,10],[50,0,0]])

print 'Our array is:'
print a
print '\n'

print 'Applying nonzero() function:'
print np.nonzero (a)

a = np.array([1,2,3,4,5])
np.save('outfile',a)

b = np.load('outfile.npy')
print b

a = np.array([1,2,3,4,5])
np.savetxt('out.txt',a)
b = np.loadtxt('out.txt')
print b 
