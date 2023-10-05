from datetime import date

class Student:
    def __init__(self, student_id, name, dob, classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__classification = classification.lower()
        self.__age = 0
        self.__register = ''

    def calculate_age(self):
        today = date.today()
        dob = self.dob.split('/')
        dob_year = int(dob[2])
        self.__age = today.year - dob_year

    def registration_dates(self):
        if self.__classification == 'Senior':
            self.__register = "November 1 to November 3"
        elif self.classification == 'Junior':
            self.__register =  "November 4 to November 6"
        elif self.classification == 'Sophomore':
            self.__register =  "November 7 to November 9"
        elif self.classification == 'Freshman':
            self.__register = "November 10 to November 12"
        else:
            self.__register =  "classification not found"
        
    def return_age(self):
        return self.__age
    
    def return_registration(self):
        return self.__register


