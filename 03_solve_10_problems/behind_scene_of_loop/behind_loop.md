# Loop Behind Scene :
![alt text](<Screenshot (1).png>)


### File is iteratable object.

## **Definition of `end=""` in Python `print()` function:**  
`end=""` ka kaam **print statement ke akhri mein jo default new line hoti hai usko replace karna hota hai.**  

### **Default behavior:**  
Python mein `print()` ka default `end="\n"` hota hai. Matlab har baar `print()` chalay ga, to **automatically ek new line add ho jaye gi**.  

**Example:**  
```python
print("Hello")
print("World")
```
**Output:**  
```
Hello
World
```
(Yahan har `print()` ke baad ek new line aa rahi hai, kyunki `end="\n"` by default hai.)

---

### **How `end=""` works:**  
Agar hum `end=""` lagayen, to **`print()` ke baad koi extra new line nahi lagegi**.  

**Example:**  
```python
print("Hello", end="")
print("World")
```
**Output:**  
```
HelloWorld
```
(Yahan dono words ek hi line mein print huay, kyunki `end=""` ne default new line (`\n`) ko hata diya.)

---

### **Explanation in Simple Terms:**  
- `end=""` ka matlab hai **kuch bhi extra nahi lagana** (default `\n` hata do).  
- `end=" "` (space dena) ka matlab hai **ek space dalna new line ki jagah**.  
- `end="--"` ka matlab hai **new line ki jagah "--" add karna**.  

**Example:**  
```python
print("Apple", end="--")
print("Banana", end=" ")
print("Cherry")
```
**Output:**  
```
Apple--Banana Cherry
```
(Yahan `Apple` aur `Banana` ke darmiyan `--` laga, `Banana` aur `Cherry` ke darmiyan ek space laga.)

---

### **In Your Code:**  
```python
for line in open('chai.py'):
    print(line, end="")
```
- **Default behavior:** Har line ke baad ek new line hoti hai.
- **With `end=""`**: Extra new line nahi aayegi, sirf jo file ke andar new line hai wohi rahe gi.  

**Without `end=""`:**  
```
Line 1

Line 2

Line 3
```
(Extra new lines aa gayi.)

**With `end=""`:**  
```
Line 1
Line 2
Line 3
```
(Extra new line nahi lagi, file ka original format maintain raha.)

---

**Conclusion:**  
✅ `end=""` **print ke akhri mein jo bhi default new line hoti hai usko replace karta hai.**  
✅ `end=""` ka use jab karna hota hai jab aap **extra new lines avoid karna chahain.**


-----------------------------
# **Important Note:**
### 1. `string`, `dictionary`, `list` aur  `range`  ye ap ko khud iter() method (loop) lagane nahe dete , yani hume in se pochna parhta hai ke kia mein ap pe **iter(loop)** lga lu toh ye kehte hai ke han lga lo, first value ka memory reference de kar aur har iteration ka baad ye __next__() deta hai aur last value ke baad ye **iter(loop)** ko bolte hai execution stop kardo.

### 2. `File` lekin file ke case mein file khud se apna memory reference pehle se hi de deta hai ke ap **iter (loop)** lga lo aur first value ka memory reference de kar aur har iteration ka baad ye __next__() deta hai aur last value ke baad ye **iter(loop)** ko bolte hai execution stop kardo.

--------------------

