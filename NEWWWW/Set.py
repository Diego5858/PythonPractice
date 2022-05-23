z ={"Sumit", 1,2 ,55, 66, 69, 2, 5.2}
z.remove(1)
print(z)

z.pop()
print(z)

z.add ("Sudip")
print(z)

Sets = {"zaheer" , "ajit" , "danish" , "venkatesh" , "harbhajan"}

Lists = list(Sets)
# x[2] = "sohaib"

a = "danish"
if a in Lists:
    index = Lists.index(a)
    Lists[index]="Sohaib"

print(Lists)

x = set(Sets)
print(x)

# #-------------------------------
# teamSet = {"Sudip", "SUmit", "Danish Kaneria", "Mahmoud", "Raka"}
# teamList = list(teamSet)
# print(type(teamList))
# x = "Danish Kaneria"

# if x in teamList :
#     index = teamList.index(x)
#     teamList[index]= "Shoeheb AKtar"
    
# teamList= set(teamList)
# print(teamList)

# y = "Sudo Kumr"
# y = y.replace("Kumr", "Kumar")
# print(y)


a = {"Ajit" , "Sumit" , "Sudip" , "ajit" }
b = list(a)

c = "Ajit"
d = "ajit"

if c in b :
    index = b.index(c)
    b[index] = "Ayaz"
if d in b:
    index = b.index(d)
    b[index] = "ayaz"

    print(b)

b = set(b)
print(b)

#-------------------------------------


q = {"a" , "b", "c"}
t = q.copy()
print(t)
w = {1,2,3,}
e = q.union(w)
print(e)
q.update (w)
print(q)

