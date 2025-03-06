# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance(object) of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model



my_car = Car("Honda", "Civic")
print(my_car.brand)
print(my_car.model)

my_car_two = Car("Toyota", "Supraa")
print(my_car_two.brand, my_car_two.model)
