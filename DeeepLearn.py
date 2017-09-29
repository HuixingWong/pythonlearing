
import numpy as np


s = np.array(5)

s.shape

v = np.array([1,2,3])

x = v[1]

print x

print v[1:]


m = np.array([[1,2,3], [4,5,6], [7,8,9]])

print m

t = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[7],[8]],\
    [[9],[10]],[[11],[12]]],[[[13],[14]],[[15],[16]],[[17],[17]]]])

print t.shape


v = np.array([1,2,3,4])
print v.shape

# x = v.reshape(1,4)
# print x.shape

x = v[None, :]

print x.shape


values = [1,2,3,4,5]

print 'values:'
print values

values = np.array(values)+5

print 'values:'
print values

a = np.array([[12,34,64],[34,45,23]])
b = np.array([[44,34,678],[34,888,554]])

print a+b


print "=============================="
c = a*a
print 'a*a'
print c


print "=============================="
d = a*b
print d

a1 = np.array([[0,2,4,6],[8,10,12,14]])
b1 = np.array([[1,3,5],[7,9,11],[13,15,17],[19,21,23]])

print "========================"
# print a1*b1

c1 = np.dot(a1,b1)

print c1



