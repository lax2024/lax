# np.array()

import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1)

# np.zeros()

print(np.zeros((2,2))) #(order)

# np.ones()

print(np.ones((3,3)))

# arange() - print values within a given range

a = np.arange(0,8,2) #(start,stop,step)
print(a)

# reshape() - chsnges shape of a NumPy array without changing data

b = a.reshape((2,2))
print(b) 

# mean(),median(),std()

print(np.mean(arr_1))
print(np.median(arr_1))
print(np.std(arr_1))

# random.rand() - generates random float numbers in the range[0,1]

arr = np.random.rand()
print(arr)

arr1 = np.random.rand(5)
print(arr1)

arr2 = np.random.rand(2,2)
print(arr2)

# radom.randint()

x = np.random.randint(1,10)
print(x)

y = np.random.randint(0,100,size=5)
print(y)

z = np.random.randint(10,21,size=(3,3))
print(z)

new = np.random.randint(0,10,size=6)
print("OTP:",new)