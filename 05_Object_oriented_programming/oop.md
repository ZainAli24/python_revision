## 1. Class defination with form example:
### Empty Form ik class hai , aur us mien jo inputs fields hai wo constructor function hai , toh constructor function hum se input leta hai aur class mien use fill karta hai, aur phir humen us ki copy(object) de deta hai.


## 2. Encapsulation:
- ### Encapsulation ka matlab hota hai cheezon ko `chhupana`.
- ### Jab hum kisi variable ya method ke aage __ lagate hain, to wo private ho jata hai.
- ### Iska matlab hai ke ye sirf class ke andar access ho sakta hai,
- ### lekin jab hum class ka object banate hain, to isay seedha access nahi kar sakte.
- ### Humein in private members ko access karne ke liye class ke methods ka istemal karna padta hai.

## 3. Getter and Setter:
- ### Getter se hum kisi variable ki value ko read (padhna) kar sakte hain.
- ### Setter se hum kisi variable ki value ko update (badalna) kar sakte hain.


## 4. can we use `__` for methods and can we use `get`and `set` method for access and update: 
- ### Ji haan, aap method ko bhi private bana sakte hain by prefixing it with double underscores (__). Matlab, agar aap kisi method ke naam ke aage __ lagate hain, to woh sirf class ke andar hi access hota hai.

- ### Lekin `getter` aur `setter` ka concept mainly variables (attributes) ke liye hota hai. Private methods ko aap directly class ke bahar call nahi kar sakte, lekin aap unhe indirectly access karne ke liye public method bana sakte hain jo private method ko call kare.

Misal ke taur par:

```python
class MyClass:
    def __init__(self, value):
        self.__value = value

    # Private method
    def __private_method(self):
        return f"Private value is {self.__value}"

    # Public method that accesses the private method
    def get_private_info(self):
        return self.__private_method()

obj = MyClass(10)
print(obj.get_private_info())  # Ye private method ka result print karega.
# print(obj.__private_method())  # Isse error aayega, kyun ke __private_method private hai.
```

- ### Is example mein, `__private_method` ko directly access nahi kiya ja sakta, lekin `get_private_info` us method ko call karke result return karta hai.

- ### `Setter` ka istemal usually variables ko update karne ke liye hota hai, methods ko update karne ke liye nahi. Methods function ke hisse hote hain, jinhe aap runtime mein update nahi karte.

---------------------------------
---------------------------------
---------------------------------

## 5. Polymorphism :

```python
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
```


### Polymorphism ka matlab hai "ek hi method, lekin alag objects par alag behavior." Is code ko dekhain:

## 1. **Class Car:**  
- ###  Is class mein method **fuel_type()** defined hai jo "Petrol and Diesel" return karta hai.
   
## 2. **Class ElectricCar:**  
- ### Yeh class, Car se inherit karti hai.  
- ### Is class mein **fuel_type()** method ko dobara (override) define kiya gaya hai, jo "Electric charge" return karta hai.

## 3. **Objects Banane Par Behavior:**  
- ### Jab aap **Car** ka object banate hain aur **fuel_type()** call karte hain, to aapko "Petrol and Diesel" milta hai.  
- ### Lekin jab aap **ElectricCar** ka object banate hain aur **fuel_type()** call karte hain, to aapko "Electric charge" milta hai.

### Is tarah, dono classes mein method ka naam same hai (fuel_type), lekin unka behavior alag hai. Yehi polymorphism ka concept hai—ek hi method ka naam, lekin alag-alag roop (behavior) alag objects mein.

---------

### Polymorphism ka matlab hai "ایک ہی چیز کے مختلف روپ" ya "اکی ہی نام، مختلف عمل"۔ 

### Iska seedha sa matlab hai ke ek hi function ya method ka naam use karke, alag-alag objects par alag tareeke se kaam kiya ja sakta hai. Matlab, agar aap ek hi function ka naam use karte hain, to woh alag-alag classes ke objects ke liye mukhtalif behavior (rawaiya) dikha sakta hai. 

### Ye concept object-oriented programming mein bohot zaroori hai, kyun ke is se code ko reuse karna aur manage karna asaan ho jata hai.

----------------------------------------------
## 6. `self.total_car` and `Car.total_car` differrece:

- **self.total_car ke case mein:**  
  Jab hum constructor call karte hain, Python dekhata hai ke self (object) ke paas total_car variable hai ya nahin. Agar nahin, toh woh class ke total_car variable ko leta hai, usse object ke liye ek naya variable bana deta hai, aur phir usme 1 add kar deta hai. Isliye Har object ke liye self.total_car us object ka apna alag variable hota hai, jiska initial value 1 set hota hai.

- **Car.total_car ke case mein:**  
  Jab bhi constructor call hota hai, Car.total_car (jo class ka shared variable hai) mein 1 add hota hai. Ye variable sabhi objects ke liye common hai, isliye har naya object banne par ye update hota hai aur humein sahi total count milta hai.

Aapne bilkul sahi samjha hai!


----------------------------------------------
## 7. **Static Method ki Definition (Seedhi Baat Mein):**  
#### Static method ek aisa function hai jo class ke andar define hota hai, lekin iska koi "self" parameter nahi hota. Matlab, yeh method object-specific (instance-specific) nahi hota, aur aap isay directly class ke naam se call kar sakte hain, bina object banaye.

**Static Method vs. Instance Method (jismein self hota hai):**

- **Instance Method:**  
  - Har instance method ka pehla parameter "self" hota hai.  
  - "self" se aap us object ke attributes (data) ko access aur modify kar sakte hain.  
  - Inhe call karne ke liye aapko pehle object create karna padta hai.

- **Static Method:**  
  - Static method ke paas "self" parameter nahi hota.  
  - Yeh object ki state se independent hota hai, matlab yeh kisi specific object ke data par depend nahi karta.  
  - Inhe directly class ke naam se call kiya ja sakta hai, object banane ki zaroorat nahi.

Is tarah, static methods un functions ke liye best hote hain jo class se related utility ya helper functions provide karte hain, jismein object-specific data ki zaroorat nahi hoti.


--------
### static method and self(object) confusion:
#### Static method mein object-specific data is liye use nahi hota kyun ke iska signature "self" parameter include nahi karta. Matlab, jab aap koi static method define karte hain to aap usay @staticmethod decorator ke saath likhte hain aur ismein instance-specific information (jaise ke object ke attributes) automatically pass nahi hoti.

**Aasan Alfaaz Mein:**

- **Instance Method vs Static Method:**  
  Instance methods, jo aap "def method(self):" likhte hain, unmein pehla parameter `self` hota hai jo us particular object ko refer karta hai. Iss se aap us object ke attributes aur state ko access kar sakte hain.  
  Lekin static methods mein `self` nahi hota, isliye woh sirf apne explicitly diye gaye parameters ke saath kaam karte hain aur object-specific data tak unka koi access nahi hota.

- **Kyun Nahi Hota:**  
  Jab static method ko call kiya jata hai, chaahe aap use class ke naam se call karein ya kisi instance se, Python automatically koi instance pass nahi karta. Is liye, static method ko aapne jo bhi arguments diye hain unhi se kaam karna padta hai.

**Example Se Samjhain:**

```python
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
```

Is example se pata chalta hai ke **description()** method ko call karne par, chahe aap class ya instance ke through call karein, is method ke paas koi reference (jaise `self`) nahi jata, is liye yeh object-specific data ko use nahi kar sakta.

In short, static methods mein instance-specific data ka istemal na hone ki wajah yeh hai ke Python unhe koi object ka reference (self) automatically provide nahi karta.


________________________________________________
________________________________________________
________________________________________________
## **8. inner working of `__`(private method):**
Python mein, agar aap kisi variable ko double underscore (__) se shuru karte hain, to interpreter usko naam tabdeel kar deta hai aur internally rename kar deta hai. Yani, jo variable aap "self.__model" kehte hain, woh asal mein "self._Car__model" ke naam se store hota hai.

**Assaan Alfaz Mein:**

- **Naam Tabdeel (Mangling):**  
  Jab aap `__model` likhte hain, Python isko rename karke `_Car__model` bana deta hai. Is se yeh variable class ke bahar directly accessible nahi hota.

- **Access Karna:**  
  Agar aap object ke bahar `my_car.__model` access karne ki koshish karte hain, to Python usko alag se treat karta hai. Yeh na to asli private variable (jo `_Car__model` hai) ko refer karta hai, aur na hi koi error deta hai—balkay yeh ek naya attribute create ho jata hai.

- **Value Change Karna:**  
  Jab aap `my_car.__model = "Aqua"` likhte hain, to aap asal mein ek naya attribute bana rahe hote hain jiska naam __model hai. Iska matlab yeh hai ke aap original private variable (`_Car__model`) ko change nahi kar rahe, balkay ek alag variable ko change kar rahe hain.

**Code Example Se Samjhain:**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model  # Internally becomes self._Car__model

    def full_name(self):
        return f"{self.brand} {self.__model}"  # Uses the modified name

    def get_model(self):
        return self.__model  # Accesses the original private variable

my_car = Car("Toyota", "Grande")

# Yeh sahi tarike se original private attribute ko access karne ke liye hai:
print(my_car.get_model())    # Output: Grande

# Lekin yeh code:
print(my_car.__model)        # Yeh new attribute __model ko refer karta hai, na ke asli private variable
my_car.__model = "Aqua"        # Yeh new attribute ko update karta hai
print(my_car.__model)        # Output: Aqua

# Agar aap asli private attribute dekhna chahein:
print(my_car._Car__model)    # Output: Grande (still unchanged)
```

**Naam Tabdeel (Mangling) ka Urdu Mein Matlab:**  
"Mangling" ka matlab hai "naam ko tabdeel karna" ya "naam badal dena". Iska maksad yeh hai ke variable ka asal naam chhup jaye, taake woh class ke bahar seedha accessible na ho jaye.

------------------------------------
#### Mangling ka matlab:
"Name Mangling" ka matlab hai ke Python, aapke class ke andar double underscore (__) se shuru hone wale variable ke naam ko internally aise badal deta hai ke woh seedha accessible na ho. Iska maqsad accidental access aur modification se bachna hota hai. 

**Thora Tafseeli Tareeqa:**

- **Naam Ko Tabdeel Karna:**  
  Jab aap koi variable `__model` ke naam se define karte hain, to Python is variable ka naam badal kar `_Car__model` kar deta hai (agar class ka naam `Car` hai). Yeh badla hua naam internal use ke liye hota hai. Is se aap directly `__model` ko class ke bahar access nahi kar sakte.

- **Accidental Access Se Hifazat:**  
  Is tarah se, agar koi developer galti se ya anjaan mein class ke bahar `__model` ko access ya modify karne ki koshish kare, to woh asal variable tak nahi pahunch paata. Yeh system aapke code ko protect karta hai ke aapke "private" attributes ko accidentally change na kar diya jaye.

- **Subclassing Aur Overriding Mein Madad:**  
  Name mangling se, agar aapki class ko extend kar ke subclass banaya jaye, to subclass mein aise variables accidentally override nahi hote. Matlab, original class ke private attributes secure rehte hain aur subclass mein unka naam conflict nahi hota.

- **Lekin Yeh Puray Tarah Se Private Nahi:**  
  Yeh sirf ek mechanism hai jo accidental access se bachata hai. Agar koi zaroorat pade, to aap mangled name, jaise `_Car__model`, ko use karke variable tak pahunch sakte hain. Lekin aam tor par, is tarah ka access discouraged hai taake encapsulation ka maqsad barqarar rahe.

Is tarah se "name mangling" aapke variable ke naam ko itna badal deta hai ke woh class ke bahar seedha nazar na aaye, aur is tarah se aapke class ke "private" attributes ko zyada secure banaya jata hai.


---------------------------------
--------------------------------
## 9. Double underscore and Property decorator difference:
- ### Aap bilkul sahi keh rahe hain. Double underscore se declare kiya gaya attribute name mangling ke zariye private ban jata hai, jise aap my_car._Car__model se access aur modify kar sakte hain. Lekin jab aap @property decorator use karte hain (without setter), to woh attribute read-only property ban jata hai, jise sirf access kiya ja sakta hai, change nahi kiya ja sakta.

## 10. @property decorator:
- ### @property decorator aik aisa mechanism hai jo aap ke class ke method ko ek property mein badal deta hai. Is se aap us method ko bina parentheses ke attribute ki tarah access kar sakte hain. Matlab, agar aap ke paas koi method hai jo kisi value ko return karta hai, to @property lagane ke baad aap us value ko asani se read kar sakte hain, lekin usay directly modify nahi kar sakte (agar setter define nahin kiya gaya ho). 

- ### Iska mtlb hai ke aapko function call ki tarah parentheses lagane ki zaroorat nahi, balkay wo method, attribute ki tarah behave karta hai, jo encapsulation aur data ko protect karne mein madad karta hai.

