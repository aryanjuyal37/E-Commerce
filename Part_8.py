class Utensils:
    def __init__(self,material):
        self.material=material 
    def use(self):
        print("Used in the kitchen and is made of "+ self.material)

class Plate(Utensils):
    def __init__(self,material):
        Utensils.__init__(self,material)

p=Plate("paper")
p.use()

class Spoon(Utensils):
    def __intit__(self,material):
        Utensils.__init__(self,material)
    
    def use(self):
        print("Used to eat and name of "+self.material)

d=Spoon("Steel")
d.use()

class Bowl(Utensils):
    def __intit__(self,material):
        super().__intit__(material)
    
    def use(self):
        print("Used to store food and made of "+self.material)
b=Bowl("Glass")
b.use()