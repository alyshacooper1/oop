import random

class Insect:

    def __init__(self, w,l,n):
        self.wings = w
        self.legs = l
        self.flight = 0
        self.name = n
    
    def flight_length(self):
        self.flight = random.randint(1,10)

    
    def get_flight(self):
        return self.flight
    
    def get_name(self):
        self.name

    

