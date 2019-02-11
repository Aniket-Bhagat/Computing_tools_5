print """-------------------------------
| Numpy Matrix Multiplication |
-------------------------------\n"""
import numpy as np
import sys

p,q,r,s =(map(lambda x : int(x),sys.argv[1:]))

A=np.random.randint(10,size=(p,q))
B=np.random.randint(10,size=(r,s))

print 'Matrix A :\n',A
print '\nMatrix B :\n',B

print "\n-------------------------------"
try:
	multiplication = A.dot(B)
	print 'Multiplication :\n',multiplication
except ValueError:
	print '''Multiplication can't be done here
Number of columns of matrix A must be \nequal to number of rows of matrix B'''
print "-------------------------------"