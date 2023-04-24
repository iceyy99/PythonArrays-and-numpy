import numpy as np


#Generate and print a 5x5 array
a = np.random.randint(9, size=(5,5))
print(a)
print("--------------------")


#Get number from array
print(a[1,2])
print("--------------------")


#Print sum of all elemnts in array
print(np.sum([a]))
print("--------------------")


#print the mean of each row in the array
print(np.mean(a, axis=1))
print("--------------------")


#Print the max value in each collumn
print(np.amax(a, axis=0))
print("--------------------")