a={0,102,3,65,4,3} # set is a collection of non repetetive elements
print(a)
print(type(a))

b={}  #creates empty dict nd not empty set
print(type(b)) 

c = set()
print(type(c))

c.add(45)
c.add(56)
c.add(45)
a.add(5)
# c.add([4,5,6]) #list and dict can not be add in set
c.add ((4,5,6))

print(a)
print(c)
print(len(c)) #prints the lenght of the set

c.remove(45)
print(c)

print(c.pop()) #removes any value from the set

