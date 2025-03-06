# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model  # Internally becomes self._Car__model

    def full_name(self):
        return f"{self.brand} {self.__model}"  # Uses the mangled name

    
    def get_model(self):
        return self.__model  # Accesses the original private variable

my_car = Car("Toyota", "Grande")

# Yeh sahi tarike se original private attribute ko access karne ke liye hai:
print(my_car.get_model())    # Output: Grande

# Lekin yeh code:
# print(my_car.__model)        # Yeh new attribute __model ko refer karta hai, na ke asli private variable
my_car.__model = "Aqua"        # Yeh new attribute ko update karta hai
print(my_car.__model)        # Output: Aqua

# Agar aap asli private attribute dekhna chahein:
print(my_car._Car__model)    # Output: Grande (still unchanged)

my_car._Car__model = "ZAIN"  # value ko change kar pa rahe hai.
print(my_car._Car__model)    


#-----------------------------------------------------------------------
# using property decorator:
# @property decorator aik aisa mechanism hai jo aap ke class ke method ko ek property mein badal deta hai. Is se aap us method ko bina parentheses ke attribute ki tarah access kar sakte hain. Matlab, agar aap ke paas koi method hai jo kisi value ko return karta hai, to @property lagane ke baad aap us value ko asani se read kar sakte hain, lekin usay directly modify nahi kar sakte (agar setter define nahin kiya gaya ho). 
# Iska mtlb hai ke aapko function call ki tarah parentheses lagane ki zaroorat nahi, balkay wo method, attribute ki tarah behave karta hai, jo encapsulation aur data ko protect karne mein madad karta hai.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model  # Internally becomes self._Car__model

    def full_name(self):
        return f"{self.brand} {self.__model}"  # Uses the mangled name

    @property
    def get_model(self):
        return self.__model  # Returns the original private variable

my_car = Car("Toyota", "Grande")

# Property ke zariye asli private attribute ko access karna (recommended):
print(my_car.get_model)    # Output: Grande
# my_car.get_model = "ZAIN"  # property decorator lagane se hum sirf value ko read kar sakhte hai, update nahe kar sakhte.
# print(my_car.get_model)
# Yeh code:
# print(my_car.__model)      # Yeh new attribute __model ko refer karta hai, na ke asli private variable
my_car.__model = "Aqua"      # Yeh new attribute ko update karta hai
print(my_car.__model)      # Output: Aqua

# Agar aap asli private attribute dekhna chahein:
print(my_car._Car__model)  # Output: Grande (still unchanged)
my_car._Car__model = "ZAIN" # property decorator lagane se hum sirf value ko read kar sakhte hai, update nahe kar sakhte.
print(my_car.Car__model)


# Double underscore and Property decorator difference:
# Aap bilkul sahi keh rahe hain. Double underscore se declare kiya gaya attribute name mangling ke zariye private ban jata hai, jise aap my_car._Car__model se access aur modify kar sakte hain. Lekin jab aap @property decorator use karte hain (without setter), to woh attribute read-only property ban jata hai, jise sirf access kiya ja sakta hai, change nahi kiya ja sakta.

