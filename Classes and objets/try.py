# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
# else:
#   print("Nothing went Wrong")
# finally:
#   print("The 'try except' is finished")


from asyncore import write
import os


a = open("C:\\Users\\sumit\\OneDrive\\Desktop\\abc.txt", "r")
print (a.read())
print (a.read(3))

a = open("C:\\Users\\sumit\\OneDrive\\Desktop\\abc.txt", "a")
a.write("Tera yaar hu main") # writes in the next line
a.close()

a = open("C:\\Users\\sumit\\OneDrive\\Desktop\\abc.txt", "w")
a.write("what a wonderful world") # Overwright
a.close()
os.remove("C:\\Users\\sumit\\OneDrive\\Desktop\\abc.txt")

