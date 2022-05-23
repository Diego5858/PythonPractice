song = '''this is ten percent luck
Twenty percent skill
Fifteen percent concentrated power of will
Five percent pleasure
Fifty percent pain'''

#string function
print(len(song))  #lenght of string

print(song.endswith("pain")) #last variable of string

print(song.count("is"))  #counts the particular character

print(song.capitalize())  # capitalised the 1st character of the given string

print(song.find("luck")) # finds the character

print(song.replace("percent", "bocha")) #replcaes the character



#Escapae sequence character

Story = "My name is sumit. \n I am \tlearning \'python\'" #\n - new line \t - tab
print(Story)