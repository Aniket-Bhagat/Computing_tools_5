print """---------------------------------------------------------
|	Numpy Matrix Addition & Subtraction		|
---------------------------------------------------------\n"""
import numpy as np
import sys

n,m =(map(lambda x : int(x),sys.argv[1:]))

A=np.random.randint(10,size=(n,m))
B=np.random.randint(20,size=(n,m))

print 'Matrix A :\n',A
print 'Matrix B :\n',B

addition = A+B
subtraction = A-B
print '\n---------------------------------------------------------'
print 'Addition (A+B):\n',addition
print 'Subtraction (A-B):\n',subtraction
print '---------------------------------------------------------'
