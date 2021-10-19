class Car:
    def __init__(self,name,engine,torque):
        self.name=name
        self.engine=engine
        self.torque=torque
    
    def accelerate(self):
        print(self.name+" is accelerating")
        return self.torque

    @classmethod
    def works(self):
        print("This car works")


# engine=int(input("Enter the value of engine-"))
# torque=int(input("Enter the value of torque-"))
# swift=Car(engine,torque)

swift=Car("Swift",1197,110)
fortuner=Car("Fortuner",2500,700)

x=swift.accelerate()
print(x)
y=fortuner.accelerate()
print(y)

swift.works()
fortuner.works()

print(swift.engine,swift.torque)
print(fortuner.engine,fortuner.torque)