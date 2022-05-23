from Volkswagen import Volkswagen

class Audi(Volkswagen):
    maxSpeed = 350
    driver= "right"

    def getEngine(self):
        print("This chils engine")

    def __init__(self):
        print('This init is of child class')

        #first way to call parent init funtion
        Volkswagen.__init__(self)  # First way to call parent function

        super().__init__() # Second way to call parent function