# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes,
# but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol and Diesel"

class ElectricCar(Car):
    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


car = Car("Toyota", "Altis")
print(car.fuel_type())
electric = ElectricCar("85kwh", "Hundai", "Elentra")
print(electric.fuel_type())




# Polymorphism ka matlab hai "ek hi method, lekin alag objects par alag behavior." Is code ko dekhain:

# 1. **Class Car:**  
#    - Is class mein method **fuel_type()** defined hai jo "Petrol and Diesel" return karta hai.
   
# 2. **Class ElectricCar:**  
#    - Yeh class, Car se inherit karti hai.  
#    - Is class mein **fuel_type()** method ko dobara (override) define kiya gaya hai, jo "Electric charge" return karta hai.

# 3. **Objects Banane Par Behavior:**  
#    - Jab aap **Car** ka object banate hain aur **fuel_type()** call karte hain, to aapko "Petrol and Diesel" milta hai.  
#    - Lekin jab aap **ElectricCar** ka object banate hain aur **fuel_type()** call karte hain, to aapko "Electric charge" milta hai.

# Is tarah, dono classes mein method ka naam same hai (fuel_type), lekin unka behavior alag hai. Yehi polymorphism ka concept hai—ek hi method ka naam, lekin alag-alag roop (behavior) alag objects mein.

# ---------

# Polymorphism ka matlab hai "ایک ہی چیز کے مختلف روپ" ya "اکی ہی نام، مختلف عمل"۔ 

# Iska seedha sa matlab hai ke ek hi function ya method ka naam use karke, alag-alag objects par alag tareeke se kaam kiya ja sakta hai. Matlab, agar aap ek hi function ka naam use karte hain, to woh alag-alag classes ke objects ke liye mukhtalif behavior (rawaiya) dikha sakta hai. 

# Ye concept object-oriented programming mein bohot zaroori hai, kyun ke is se code ko reuse karna aur manage karna asaan ho jata hai.
