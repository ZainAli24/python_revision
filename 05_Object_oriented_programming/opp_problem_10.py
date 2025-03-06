# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both,
# demonstrating multiple inheritance.

class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size


class Engine:
    def __init__(self, Engine_fuel_average):
        self.Engine_fuel_average = Engine_fuel_average



class Electric_Car(Battery, Engine):
    def __init__(self, battery_size, Engine_fuel_average, brand, model):
        Battery.__init__(self, battery_size)
        Engine.__init__(self, Engine_fuel_average)
        self.brand = brand
        self.model = model


my_ev = Electric_Car("85kwh", "11kmph,petrol", "Hundai", "Sonata")
print(my_ev.battery_size)
print(my_ev.Engine_fuel_average)
print(my_ev.brand)
print(my_ev.model)
