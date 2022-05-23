from Person import Person

class Students(Person):
    def __init__(self, fname, lname , passing_year):
        super().__init__(fname, lname)
        self.passing_year = passing_year
        
                

                

