#1st question

name = input("Enter your name : ")
print("Good Afternoon," , name )


#2nd question

letter = '''Dear <|Name|>

You are the champion!

Date: <|Date|>'''

names = input("Enter your Name :")
date = input("Enter Date :")
letter = letter.replace("<|Name|>", names)
letter = letter.replace("<|Date|>", date)

print(letter)