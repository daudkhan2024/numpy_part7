# Indexing and slicing in Array
#Indexing:
import numpy as np
print("Topic : indexing in 1 row array")
#indexing in 1 row array
var = np.array([9,8,7,6])
print(var[1])
print(var[-3])


print()
var1 = np.array([[9,8,7],[4,5,6]])
print(var1)
print(var1.ndim)
print()
print(var1[0][1])

print("Topic : 2D Indexing")
#2D array indexing
var2 = np.array([[1,2],[3,4]])
# to get 3 from it
print(var2)
print(var2[0,1])
print(" number of arrays :", var2.ndim)

print()
#Array slicing
print("Topic : array slicing ")
#One dimention array
var  = np.array([1,2,3,4,5,6,7])
print(var)
print()
print("number of arrays :  ",var.ndim)

print("To get elements from 2 to 5")
print(var[1:5])
print()
print("slice from 2 till end ")
print(var[1:])

print()
print("to get element from 1 to 5 ")
print(var[ : 5])

print()
print("getting data into jumping ")
print(var[ ::2])

print()
print("when we have 2D array and how we do slicing?")
var2 = np.array([[1,2,3,4],[5,6,7,8]])
# to get 5 to 7 elements
print(var2[1,0:3])
#same for 3D array

print()
