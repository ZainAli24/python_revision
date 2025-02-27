# 1. Python Variables: No Own DataType, Only Values Have a DataType

Python me **variable ka khud ka koi datatype nahi hota**, balki **jo value memory me store hoti hai, uska datatype hota hai**.  

### **Simplified Explanation:**  
- **Variable sirf ek naam hai** jo kisi value ko **reference** kar raha hota hai.  
- **Value ka datatype hota hai, variable ka nahi.**  

#### **Example:**
```python
x = 10       # 10 ek integer value hai, x sirf usko refer kar raha hai
x = "Hello"  # Ab x ek string ko refer kar raha hai
```
- Pehle `x` ek **integer (10)** ko refer kar raha tha.  
- Baad me `x` ek **string ("Hello")** ko refer karne laga.  

Matlab Python me **ek hi variable alag-alag type ki values ko hold kar sakta hai.**


# Garbage Collection in Python: Mutable vs Immutable Datatype Deletion Rule : 
Haan, **mutable types (lists, dictionaries, sets, objects, etc.) ko Python zyada jaldi delete karta hai**, kyunki yeh zyada memory use karti hain.  

### **Mutable vs Immutable Types (Deletion Speed)**  
- **Immutable (Numbers, Strings, Tuples)** → Thodi der tak memory me reh sakti hain.  
- **Mutable (Lists, Dicts, Sets, Objects)** → Jaldi delete ho jati hain, kyunki zyada memory leti hain.  

### **Example:**  
```python
x = [1, 2, 3]  # List banayi
x = None       # Pehli list ka reference hat gaya, GC jaldi delete karega
```
Yahan list ka koi reference **nahi raha**, toh **GC isko jaldi free karega** compared to ek simple number ya string.  

### **Summary:**  
- **Choti immutable values** (jaise `int`, `str`) **thodi der memory me reh sakti hain**.  
- **Badi mutable values** (jaise `list`, `dict`) **jaldi delete ho jati hain**.  
- **Garbage collector background me kaam karta hai, isliye timing fix nahi hoti**. 🚀

---------------------------
# 1. Number Datatype :-
-----------------
## repr , str and print : 
Haan, bilkul!  

- **repr()**: Jo value jis type ki hoti hai, usko properly represent karta hai (extra quotes ya details ke sath).  
- **str()**: Jo value dete ho, usko asaan aur readable form mein return karta hai.  
- **print()**: Sirf value ko screen par print karta hai, bina kisi extra formatting ke.




----------------
## floor and trunc methods : 
Haan, bilkul!  

- **math.floor()**: Hamesha neeche wali taraf le jata hai (chhoti value ki taraf), chahe wo zero se door ho.  
- **math.trunc()**: Hamesha zero ki taraf le jata hai (bas decimal hata deta hai, sign change nahi karta).  

### Example:  
- `math.floor(-3.5) → -4` (neeche le gaya)  
- `math.trunc(-3.5) → -3` (zero ke kareeb le gaya)


## Bitwise operations in Python:
Bitwise operations Python mein aise operations hote hain jo numbers ke binary (bits) par kaam karte hain. Aaiye code dekhte hain:

```python
x = 1
x << 2  # Result is 4
```

**Iska matlab samjho:**

- **Binary Representation:**  
  - 1 ka binary form hai `0b1`.

- **Left Shift (<<):**  
  - `x << 2` ka matlab hai ke binary digits ko 2 positions left shift karo.  
  - 1 ko agar 2 positions left shift karen to `0b1` ban jata hai `0b100`.

- **Result Calculation:**  
  - `0b100` binary mein 4 ke barabar hota hai (4 = 1 * 2^2).

**Aasan Alfaaz Mein:**  
- **Bitwise operations:** Numbers ke bits par directly operations karna.  
- **Left shift (<<):** Bits ko left ki taraf move karna, jo number ko 2 ki power se multiply kar deta hai.  
- Is case mein, 1 ko 2 positions left shift karne se 1 * 2^2 = 4 ban jata hai.

Yeh operations binary calculations ko simple aur tez banate hain!

Chaliye asaan alfaaz mein samjhte hain:

1. **Binary Representation:**  
   - Number 1 ko binary mein likhne ke liye hum "0b1" kehte hain.  
   - Yahan "1" hi bit hai.

2. **Left Shift ka Matlab:**  
   - Jab hum "x << 2" likhte hain, iska matlab hai ke x ke binary bits ko 2 positions left move kar do.  
   - Iska asar ye hota hai ke jitni bhi positions shift hongi, un positions par right se 0 add ho jate hain.

3. **Example Samjho:**  
   - 1 ko binary mein likho: **0b1**  
   - Ab isko 2 positions left shift karo:  
     - Pehli position shift karne par "0b1" ban jata hai "0b10".  
     - Doosri position shift karne par "0b10" ban jata hai "0b100".  
   - **0b100** ka matlab hai:  
     - Rightmost bit ka weight 2^0 = 1,  
     - Uske left bit ka weight 2^1 = 2,  
     - Aur uske left mein "1" ka weight 2^2 = 4.  
     - Yahan sirf 4 bacha hai, isliye result 4 hota hai.

**Bas itna samajh lo:**  
Left shift se bit ko left move karke uska weight barh jata hai. 1 ko 2 positions shift karne se 1 se 4 ban jata hai.


Binary system mein sirf **0** aur **1** use hote hain. Isliye:

- Number **2** ka binary representation **0b10** hota hai (1×2¹ + 0×2⁰ = 2).  
- Aap **0b200** likh nahi sakte kyun ke "2" binary digit allowed nahi hai.


## "Shuffle" ka Urdu mein matlab hai **"بکھیرنا"** ya **"ملا دینا"**.  
### Yeh lafz aksar aise istimal hota hai jab cheezon ko mix karke unki order badal di jaye, jaise ke taash ko shuffle karna.


## Union and intersection:
Haan, bilkul!

- **& (Intersection):** Ye operator do sets ke common elements leta hai.  
  - **Intersection ki Tareef:** Intersection un tamam elements ka set hota hai jo dono sets mein mojood hote hain.  
  - **Example:** `{1,2,3,4} & {5,4,3}` ka intersection `{3,4}` hai, kyun ke 3 aur 4 dono sets mein hain.

- **| (Union):** Ye operator do sets ke tamam elements ko combine karta hai, bina duplicate elements ke.  
  - **Union ki Tareef:** Union un tamam elements ka set hota hai jo kisi bhi set mein mojood ho, matlab dono sets ke elements milakar ek set ban jata hai.  
  - **Example:** `{1,2,3,4} | {5,4,3}` ka union `{1,2,3,4,5}` hai.

In asaan alfaaz,  
- **Intersection (&):** Sirf common (mushterka) elements ko leta hai.  
- **Union (|):** Dono sets ke tamam unique elements ko milata hai.

-______________________________________________________________________________________________________________________-

# list in depth : 
Ye is liye hua kyunki Python me **list slicing** ek **iterable** (matlab jo ek ek karke values de sake) ko accept karta hai.  

### 1️⃣ **Jab aap `tea_varities[1:2] = "Lemon"` likhte ho:**  
- `"Lemon"` ek **string** hai, aur string bhi ek iterable hoti hai (har letter alag alag hota hai).  
- Is wajah se Python `"Lemon"` ko ek ek character me tod kar list me daal deta hai.  
- **Result:** `['Black', 'L', 'e', 'm', 'o', 'n', 'White', 'Herbal']`

### 2️⃣ **Jab aap `tea_varities[1:2] = ["Lemon"]` likhte ho:**  
- `["Lemon"]` ek **list** hai jisme ek hi element `"Lemon"` hai.  
- Python **list ko as it is insert karta hai**, bina today huay.  
- **Result:** `['Black', 'Lemon', 'White', 'Herbal']`

### **Aasaan Alfaaz Mein:**  
- **String ek ek character me break ho jati hai.**  
- **List ko as it is rakha jata hai.**  
Isi wajah se pehli case me `"Lemon"` tod gaya, aur doosri case me wo poora ek element bana raha.

---------------
### append() method is add value in the end of list.
### pop() method is remove last value of list .

---------------------------------------------------------------------------------------------
## **List Comprehension loop:-**
Haan, bilkul sahi samjha!  

### **`[x**2 for x in range(10)]` ka Matlab:**  
Ye ek **list comprehension** hai jo ek **loop** ki tarah kaam karta hai.  

### **Breakdown:**  
1. `range(10)` → **0 se 9 tak numbers generate karega** (10 include nahi hoga).  
2. `x**2` → **Har number ka square** le raha hai.  
3. **List me store kar raha hai.**  

### **Equivalent Loop Code:**  
Agar **normal loop** se likhein to ye hoga:  
```python
squared_num = []
for x in range(10):
    squared_num.append(x**2)
```

**Output:**  
```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Matlab **haan, ye loop hi hai jo har number ko square karke list me daal raha hai!** 

-----------------------
## combine keys and values from zip method:
Agar aap chahte hain ke har key ko list ke alag alag value assign ho, to aap **zip()** function use kar sakte hain. Misal ke taur par:

```python
keys = ["Masala", "Ginger", "Lemon"]
default_values = ["Spicy", "Strong", "Fresh"]
new_dict = dict(zip(keys, default_values))
print(new_dict)
```

**Iska nateeja hoga:**

```python
{'Masala': 'Spicy', 'Ginger': 'Strong', 'Lemon': 'Fresh'}
```

**Aasaan Alfaaz Mein:**  
- **zip()** function do lists ko pair karta hai.  
- Pehli list ke har element ko, doosri list ke ussi position ke element se milata hai.  
- Phir **dict()** in pairs ko ek dictionary bana deta hai.  

Is tarah, har key ko alag value milti hai.


---__________________________________________________________________________________________________________________________________________________----
## Tuple is immutable : so its value cannot be changed .


---__________________________________________________________________________________________________________________________________________________----
