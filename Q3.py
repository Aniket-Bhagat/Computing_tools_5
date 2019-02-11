print """---------------------------------------------------------
|	Random Vector (1D Array) of size 10 Sorted	|
---------------------------------------------------------\n"""
import numpy as np

Array = np.random.randint(100,size=10)

print 'Random Vector : ',Array

print '\nSorted Vector : ',sorted(Array)
print '\n---------------------------------------------------------'