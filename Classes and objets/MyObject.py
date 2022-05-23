# from MystudyRoom import MystudyRoom
from MystudyRoom import Sports


# myobj = MystudyRoom("pragati" , "Sumit 55")

# print(myobj.Bencho)
# print(myobj.teacher)


sports = Sports()
player = sports.cricket()
print(player)

print(sports.six)

sports.six = 20
x = sports.six
print(x)

# del sports.six
print(sports.six)


