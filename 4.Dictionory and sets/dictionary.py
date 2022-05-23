mydict = {

    "Sumit": "A Gamer",
    "Life": "Sucks",
    "Marks": [1,2,5,6],
    "anthrdict":{"Lumia":"A rider"} #nested dictionary
    
}
mydict['Marks'] = [45.78] # cannot contain duplicate so it changes the first value

print (mydict['Sumit'])
print (mydict['Life'])
print (mydict['Marks'])
print (mydict['anthrdict']['Lumia'])

