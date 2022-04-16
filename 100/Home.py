class Car(object):
    def __init__ (self, doors, color, type, compeny, speed_limit):
        self.doors = doors
        self.color = color
        self.type = type
        self.compeny = compeny
        self.speed = speed_limit

    def forward(self):
        print("the car moved int the forward direction")

    def  reverse(self):
        print("the car reversed")
    
    def change(self, gear):
        print("the gear chenged to " + str(gear) )

    def stop(self):
        print("the car stopped")

car1 = Car(5, "red", "suv", 'hondi', 100 )
car2 = Car(4, "white", "sedan", "audi", 150)

car1.forward()
car2.reverse()
car1.change(3)