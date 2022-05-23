# def func(fname):
#   print(fname + " Refsnes")

# func("Emil")
# func("Tobias")
# func("Linus")


# def my_function(*fname):
#   print(" Refsnes" , fname)

# my_function("Emil")
# my_function("Tobias","dfdf", "fddf")
# my_function("Linus", "sdwe")

# def my_func(country = "Norway"):
#   print("I am from " + country)

# my_func("Sweden")
# my_func("India")
# my_func()
# my_func("Brazil")


# def my_fun(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# my_fun(fruits)

# print('------------------------')
# vegetable =["tomato","potato"]
# my_fun(vegetable)

# # ==================================

# def functi(x):

#   # functi(3)
#   return 5 * x

# print(functi(3))
# print(functi(5))
# print(functi(9))

# Recursion Example

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)






# import numpy as sumit


# def myfin(n):
#   return lambda a : a *n
# mytrip = myfin(3)
# print(mytrip ())

# Cars = ["Toyota", "hyundai" , ]

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))