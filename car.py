class Car:
    #make = Avendor
    #model = Lamborghin
    #color = White
    #speed = 220mph

    def __init__(self,make,model,color,speed):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed
    def crash (self):
        return f"Hello my {self.make }  {self.model }  {self.color }, stop reaching your maximum speed of {self.speed}mph!"  
    def capacity (self):
         return f"My {self.make }  {self.model } surely goes up to {self.speed }mph.I will have to change it's color to {self.color } next week"


         