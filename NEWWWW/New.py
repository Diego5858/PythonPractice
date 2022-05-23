import queue


print ("Hi")

if 5>2:
    print("5 is graeter")
if 2<5:
    print("kkdjf")

# =========================================

p,q,r = "Sumit", "Sudip" , "kdkfj"
s = (p,q,r)
print(s)

print(type(p), type(q), type(r))

names = ["Sumit", "Sudip" , "kdkfj"]
print(type(names))

# x = 5
# y = "fdf"
# print(x+y)

# =========================================================

c = "Super"

def myfun():
    global c
    c = "Sumit"
    print ("Abba is "+ c)
myfun()

print ("Abba is ", c)



