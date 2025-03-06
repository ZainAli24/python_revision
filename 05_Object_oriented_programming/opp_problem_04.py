# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and 
# provide a getter method for it.

# Encapsulation ka matlab hota hai cheezon ko `chhupana`.
# Jab hum kisi variable ya method ke aage __ lagate hain, to wo private ho jata hai.
# Iska matlab hai ke ye sirf class ke andar access ho sakta hai,
# lekin jab hum class ka object banate hain, to isay seedha access nahi kar sakte.
# Humein in private members ko access karne ke liye class ke methods ka istemal karna padta hai.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"
    
    def set_brand(self, new_brand):
        self.__brand = new_brand
        return self.__brand



mycar = Car("Toyota", "Supraa")
# print(mycar.__brand)      # no access directly because its a private.
print(mycar.get_brand())
print(mycar.set_brand("Honda"))
print(mycar.get_brand())


# Getter se hum kisi variable ki value ko read (padhna) kar sakte hain.
# Setter se hum kisi variable ki value ko update (badalna) kar sakte hain.


# Ji haan, aap method ko bhi private bana sakte hain by prefixing it with double underscores (__). Matlab, agar aap kisi method ke naam ke aage __ lagate hain, to woh sirf class ke andar hi access hota hai.

# Lekin getter aur setter ka concept mainly variables (attributes) ke liye hota hai. Private methods ko aap directly class ke bahar call nahi kar sakte, lekin aap unhe indirectly access karne ke liye public method bana sakte hain jo private method ko call kare.

# Misal ke taur par:

# ```python
# class MyClass:
#     def __init__(self, value):
#         self.__value = value

#     # Private method
#     def __private_method(self):
#         return f"Private value is {self.__value}"

#     # Public method that accesses the private method
#     def get_private_info(self):
#         return self.__private_method()

# obj = MyClass(10)
# print(obj.get_private_info())  # Ye private method ka result print karega.
# # print(obj.__private_method())  # Isse error aayega, kyun ke __private_method private hai.
# ```

# Is example mein, `__private_method` ko directly access nahi kiya ja sakta, lekin `get_private_info` us method ko call karke result return karta hai.

# Setter ka istemal usually variables ko update karne ke liye hota hai, methods ko update karne ke liye nahi. Methods function ke hisse hote hain, jinhe aap runtime mein update nahi karte.
