class BMW():
    def fuel_type(self):
        print("This BMW model uses petrol")

    def max_speed(self):
        print("BMW maximum speed is 180 mph")
    

class Ferrari():
    def fuel_type(self):
        print("This Ferrari model uses diesal")
    
    def max_speed(self):
        print("Ferrari maximum speed is 200 mph")


obj_bmw=BMW()
obj_fer=Ferrari()

for car in (obj_bmw, obj_fer):
    car.fuel_type()
    car.max_speed()
