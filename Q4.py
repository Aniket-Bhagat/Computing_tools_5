print """------------------------------------------------------------
|  Generate 5 random numbers from the Normal Distribution  |
------------------------------------------------------------\n"""
import numpy as np

mean=0 ; stdev=1 ; n=5
Array = np.random.normal(mean,stdev,n)

print '5 numbers from Normal Distribution :\n',Array
print '\n------------------------------------------------------------'
