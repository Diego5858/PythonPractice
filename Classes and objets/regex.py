import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)



txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))