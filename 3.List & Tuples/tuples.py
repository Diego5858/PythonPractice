t = (1,5,6,7,1,9,18)
t1 = (1,) # to create a tuple use ','
print(t)
print(t[0])
print(t1)

#t[0] = 34 # Cannot update in tuple

print (t.count(1))
print (t.index(6))

#-------------------------------------------

myTuple1=("sudip", "Pooja", "Sumit", "Monica", "Ayaaz")
myTuple2=(666, 6, 55, 54, 14)
mylist= [myTuple1, myTuple2]


for list in mylist:
    for item in list:
         print(item)

# myTuple2[1]= "surya"

# myTuple3 = ("surya",)
# print(type(myTuple3))
# newList = list(myTuple2)

# # newList.append("suraj")

# print('after appending ' , newList)
# myTuple2 = tuple(newList)

# print(myTuple2)

myTuple1 += myTuple2
print(myTuple1)
