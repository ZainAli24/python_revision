# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        # Instance method, yahan 'self' use hota hai
        return f"{self.brand} {self.model}"

    @staticmethod
    def description():
        # Static method, yahan 'self' nahi hota, is liye object-specific data (jaise brand/model) access nahi kar sakte
        return "Cars are means of transport"

# Static method ko class ke through call karna:
print(Car.description())  # Output: Cars are means of transport

# Agar instance ke through call karte hain, to bhi:
my_car = Car("Honda", "Civic")
print(my_car.description())  # Output: Cars are means of transport





# static method and self(object) confusion:
# Static method mein object-specific data is liye use nahi hota kyun ke iska signature "self" parameter include nahi karta. Matlab, jab aap koi static method define karte hain to aap usay @staticmethod decorator ke saath likhte hain aur ismein instance-specific information (jaise ke object ke attributes) automatically pass nahi hoti.

# Aasan Alfaaz Mein:
# Instance Method vs Static Method:
# Instance methods, jo aap "def method(self):" likhte hain, unmein pehla parameter self hota hai jo us particular object ko refer karta hai. Iss se aap us object ke attributes aur state ko access kar sakte hain.
# Lekin static methods mein self nahi hota, isliye woh sirf apne explicitly diye gaye parameters ke saath kaam karte hain aur object-specific data tak unka koi access nahi hota.

# Kyun Nahi Hota:
# Jab static method ko call kiya jata hai, chaahe aap use class ke naam se call karein ya kisi instance se, Python automatically koi instance pass nahi karta. Is liye, static method ko aapne jo bhi arguments diye hain unhi se kaam karna padta hai.

# Example Se Samjhain:

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         # Instance method, yahan 'self' use hota hai
#         return f"{self.brand} {self.model}"

#     @staticmethod
#     def description():
#         # Static method, yahan 'self' nahi hota, is liye object-specific data (jaise brand/model) access nahi kar sakte
#         return "Cars are means of transport"

# # Static method ko class ke through call karna:
# print(Car.description())  # Output: Cars are means of transport

# # Agar instance ke through call karte hain, to bhi:
# my_car = Car("Honda", "Civic")
# print(my_car.description())  # Output: Cars are means of transport
# Is example se pata chalta hai ke description() method ko call karne par, chahe aap class ya instance ke through call karein, is method ke paas koi reference (jaise self) nahi jata, is liye yeh object-specific data ko use nahi kar sakta.

# In short, static methods mein instance-specific data ka istemal na hone ki wajah yeh hai ke Python unhe koi object ka reference (self) automatically provide nahi karta.
