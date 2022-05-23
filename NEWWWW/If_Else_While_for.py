# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
#   #-------------------

# c = 330
# d = 330
# print("C") if c > d else print("=") if c == d else print("D")

# # ----------------------------

#while

# i = 1
# while i<20:
#     print(i)
#     i+=1


# i = 1
# while i <= 6 :
#     j = 1
#     while j <= i:
#         print("*", end = " ")
#         j += 1
#     print()
#     i += 1



# k = 1
# while k <6:
#     print(k)
#     if k == 3:
#         break
#     k +=1


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# for t in range(8): # Range starts from 0 nd increments by 1
#     print (t)

# for s in range (2,38,5):
#     print (s)

# name = ["Sumit", "Sudip", "pooja"]
# fruits = ["apple", "banana", " goo"]
# for x in name:
#     for y in fruits:
#      print(x,y)


Cup = {
  "India"  : ["Sumit", "Sudip"],
  "Australia" : ["Ayaz" , "Suraj" , "Rajjo"],
  "Sri lanka" : ["Mehul", "Ashu"]
   }


name = input("Country Name : " )
print(name)
Playerlist = Cup.get(name)
print(Playerlist)
Lenght= len(Playerlist)
print(Lenght)

Q = input("Do u wnat to show player name : ")
if Q == "Yes" or "yes":
       for players in Playerlist:
            print(players)    



    







