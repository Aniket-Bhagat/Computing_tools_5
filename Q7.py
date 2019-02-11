import numpy as np
import sys

N,M =(map(lambda x : int(x),sys.argv[1:]))

while not(N>=3 and 0<=M<=7):
	if N<3 :
		print '\'n\' must be Greater than or equal to 3'
	if 0>M or M>7:
		print '\'m\' must be between 0-7'

	print '\ninput n and m again'
	N=input("n = ")
	M=input("m = ")

print "\n------------------------------------------------------"
a =  np.zeros((N,M),int)
print 'Matrix A :\n',a

b=np.random.randint(10,size=(N,M))
print '\nMatrix B :\n',b

for i in range(N):
	for j in range(M):
		a[i][j]=a[i][j]+b[i][j]
print "\n------------------------------------------------------"
print "Matrix A after addition of Matrix B in A\n",a
print "------------------------------------------------------"