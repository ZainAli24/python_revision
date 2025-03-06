# ▼3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute
# battery_size.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size




ev = ElectricCar("Large", "Toyota", "Supraa")
print(ev.full_name())
print(ev.battery_size)
