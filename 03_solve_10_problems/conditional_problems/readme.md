# Python mein `%` ka use **main cheezon** ke liye hota hai:  

### **1️⃣ Modulus Operator (`%`)**
Ye **remainder (baqiya)** find karne ke liye use hota hai.  

**Example:**  
```python
print(10 % 3)  # Output: 1  (kyunki 10 ko 3 se divide karne pe remainder 1 bachta hai)
print(15 % 4)  # Output: 3  (kyunki 15 ko 4 se divide karne pe remainder 3 hai)
```

👉 **Use case:** Even ya Odd number check karne ke liye:  
```python
num = 7
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```
✅ Agar remainder `0` ho toh **Even**, warna **Odd** hoga.

---

### **Summary:**  
✅ **`%` Modulus** → Remainder find karne ke liye  

Agar sirf **Mathematics** mein `%` dekho, toh ye **remainder return karta hai**. 🚀


------------------------------
# stripe():
Haan, **`.strip()`** sirf **starting aur ending spaces** remove karega, **beech ki spaces** nahi.  

🔹 **Example:**  
```python
text = "   Hello World   "
print(text.strip())  # Output: "Hello World" (start aur end ki spaces hat gayi)
```
