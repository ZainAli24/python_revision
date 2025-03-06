# ▼6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand}{self.model}"



res1 = Car("Toyota", "Supraa")
res2 = Car("Honda", "Civic")
res3 = Car("Mercedes", "Benz")
res4 = Car("Suzuki", "Swift")
res5 = Car("Suzuki", "Cultas")

print(Car.total_car)


## 6. `self.total_car` and `Car.total_car` differrece:

# - **self.total_car ke case mein:**  
#   Jab hum constructor call karte hain, Python dekhata hai ke self (object) ke paas total_car variable hai ya nahin. Agar nahin, toh woh class ke total_car variable ko leta hai, usse object ke liye ek naya variable bana deta hai, aur phir usme 1 add kar deta hai. Isliye Har object ke liye self.total_car us object ka apna alag variable hota hai, jiska initial value 1 set hota hai.

# - **Car.total_car ke case mein:**  
#   Jab bhi constructor call hota hai, Car.total_car (jo class ka shared variable hai) mein 1 add hota hai. Ye variable sabhi objects ke liye common hai, isliye har naya object banne par ye update hota hai aur humein sahi total count milta hai.

# Aapne bilkul sahi samjha hai!
