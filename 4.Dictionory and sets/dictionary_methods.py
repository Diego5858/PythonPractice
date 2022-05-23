mydict = {

    "sumit": "A Gamer",
    "life": "Sucks",
    "marks": [1,2,5,6],
    "anthrdict":{"Lumia":"A rider"}, #nested dictionary
    1:12
    
}

print(mydict)

print(mydict.keys())

#dictionary methods

print(type(mydict.keys())) # shows the type
print(list(mydict.keys())) # prints the keys of the dictionary
print(mydict.values()) # shows the values
print(mydict.items()) #prints the key,value for all items in the dictionary

udict = {

    "Rajjo":"Friends",
    "Mehul":"Friends"
}

mydict.update(udict) #update dictionary by adding key,values pairs usind .update
print(mydict)

print(mydict.get("sumit")) 
print(mydict.get("sumit2")) #Returns None as sumit2 is not in the dictionary

print(mydict["sumit"]) 
# print(mydict["sumit2"])  #Throws an error as sumit2 is not in the dictionary
 
