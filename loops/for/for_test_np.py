import numpy as np
array1=np.array([1,2,3])
print("array 1",array1)
array2=[None]*len(array1)
for i in range(0,len(array1)):
    array2[i]=array1[i]
print("array 2",array2)