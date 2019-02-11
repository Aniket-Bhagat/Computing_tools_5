print """------------------------------------------------------
|		  Numpy Matrix Printing	 	     |
------------------------------------------------------\n"""
import numpy as np

print 'Enter a 3X3 matrix (Elements in each row must be seperated by space):'

n=3
Matrix=[]
for i in range(n):
	row=(raw_input())
	row=map(lambda x : int(x), row.split(' '))
	Matrix.append(row)

Matrix =  np.matrix(Matrix)
rank = np.ndim(Matrix)

print "\n------------------------------------------------------"
print 'Your numpy matrix is :\n',Matrix
print '\nRank of matrix is :',rank
print 'Shape of matrix is :',Matrix.shape
print "------------------------------------------------------"