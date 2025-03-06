# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    

my_car = Car("Toyota", "Grande")
print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))

my_tesla = ElectricCar("Tesla", "E-class", "85kwh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
