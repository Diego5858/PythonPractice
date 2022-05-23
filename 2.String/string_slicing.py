greeting = "Good Morning, "
name = "Sumit"
#print(type(name))
# Concatenating two strings
c =  (greeting + name)
print (c)

#String Slicing
names  = "Sudip"
print(names[2])
print(names[0:2])
print(names[:4]) # is same as [0:4]
print(names[-4:-1])


# slicing with skip value

naam = "Sumit says good morning"
d = naam[0:20 :2] # [0 = starting value : 20 = end value : 2 = skip value]
print(d)