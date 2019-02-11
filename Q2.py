print """------------------------------------------------------
|	     Generate Array of Random Numbers 	     |
------------------------------------------------------\n"""
import numpy as np
from random import *

def generate(n):
	seq=[randint(0,100) for x in range(n)]
	return seq

Random_No = generate(10)
print 'Random Numbers Generated :\n',Random_No

print '\nArray of Random Numbers :\n',np.array(Random_No)
print '\n---------------------------------------------------------'
