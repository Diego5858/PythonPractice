from Audi import Audi
from Volkswagen import Volkswagen
from students import Students

class Test:
     #THis is the parent or the base class
    # volkswagenobj = Volkswagen()
    # print(volkswagenobj.drive)
    # volkswagenobj.getMileage()


    # #  This is the child or the derived class

    # audiObj = Audi()

    # print(audiObj.driver)
    # audiObj.getEngine()
    # audiObj = Audi()

    passyearobj = Students("Sumit", "Singh", 2201)
    print(passyearobj.firstname, passyearobj.lastname, passyearobj.passing_year)

    x = dir(Audi)
    print(x)

import datetime

x = datetime.datetime.now()
print(x)
print(x.strftime("%C"))

import math
y = math.pi
print(y)

import json
a = {
    "name " : "Sumit",
    "age": 30, 
    "city":"New York"
}

b = json.dumps(a)

print(b)




    
    
    
