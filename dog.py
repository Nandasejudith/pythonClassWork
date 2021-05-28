class Dog:
    #name = Max
    #breed = American
    #color = White
    #Size = Medium
    def __init__(self,name,breed,color,size):
        self.name = name
        self.breed = breed
        self.color = color
        
    def run (self):
        return f"My {self.name } is of an {self.breed } and {self.color} is it's color?" 

    def bark (self):
        return f"Hey my beloved {self.name }, {self.breed }, glowing  {self.color } doggy,stop backing at night."     