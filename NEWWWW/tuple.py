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
