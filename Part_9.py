class Utensils:
    def __init__(self,material):
        self.material="Steel"

    def use(self):
        print("Used in the kitchen and is made of "+ self.material)

class plate(Utensils):
    def __init__(self,material):
        #super().__init__(self) if this statement instead of the one below then the variable will be overrided
        self.material=material
        # super().__init__(self)# since the parent class constructor is being called after the variable it switches to the parent value 
    
    def use(self):
        super().use() #using the parent class contructor with super to make material equal to steel
        print("I am a plate and made of "+ self.material)
        
        
p=plate("Paper")
p.use()

