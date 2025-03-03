## Polymorphism ka matlab hai **"ایک چیز کے کئی روپ"**.  

Programming mein polymorphism ka matlab hai ke ek function, method ya object mukhtalif tareeqon se kaam kar sakta hai. Matlab ek hi naam ka function ya method alag-alag tareeqon se behave kar sakta hai.  

### Example:
Agar ek function **`calculate`** hai jo:
- Do numbers ko **add** bhi kar sakta hai  
- Aur strings ko **concatenate** bhi kar sakta hai  

To ye **polymorphism** ka example hoga.  

### Real-life Example:
Ek **"Mobile"** ka concept lein:
- **Calling ke liye** use hota hai  
- **Internet chalane ke liye** bhi use hota hai  
- **Camera ki tarah** bhi kaam karta hai  

Yani ek hi cheez mukhtalif tareeqon se behave kar sakti hai. Isi ko **polymorphism** kehte hain.



________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
## **Area aur Circumference ka Matlab**  

Agar **circle** (daira) ko samjhein, to uske **do important cheezen hoti hain:**  

1. **Area (رقبہ):**  
   - Ye circle ke andar ka **total surface area** hota hai.  
   - Formula: **π × r²**  
   - (π ≈ 3.1416, r = radius)  

2. **Circumference (محیط):**  
   - Ye circle ki **boundary ka total length** hota hai.  
   - Formula: **2 × π × r**  

---

### **Example Function in Python:**
```python
import math

def circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Example Usage:
r = 5
area, circumference = circle_properties(r)
print(f"Area: {area}")
print(f"Circumference: {circumference}")
```

✅ **Agar `radius = 5` ho, to output hoga:**  
```
Area: 78.53981633974483  
Circumference: 31.41592653589793  
```

---

### **Real-life Example:**  
Agar aapke paas ek **gol table** hai aur aap uska **area** ya **boundary ka length** (circumference) nikalna chahte hain, to ye formulas use honge.

________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Behind the scene of return:
Is code ke andar jo "for" loop use ho raha hai, wo even numbers generate karne ke liye design kiya gaya hai. Chaliye step by step samajhte hain:

1. **Loop Ka Structure:**  
   ```python
   for n in range(2, num+1, 2):
       return n
   ```  
   - `range(2, num+1, 2)` even numbers generate karta hai. Agar `num` 10 hai, to ye sequence hogi: 2, 4, 6, 8, 10.
   
2. **Return Statement:**  
   - Lekin "return n" loop ke andar hai. Jaise hi loop ka pehla iteration execute hota hai (jab `n` ka value 2 hota hai), function "return n" execute karke value 2 return kar deta hai.
   - Jab return statement call hota hai, function turant terminate ho jata hai aur baqi iterations (4, 6, 8, 10) kabhi execute nahi hoti.
   - Jab aap "return" statement ko for loop ke andar use karte hain, to yeh na sirf loop ko terminate karta hai balkay poore function ko hi terminate kar deta hai. Matlab, jaise hi "return" execute hota hai, function turant exit ho jata hai aur for loop ke aage ke iterations kabhi execute nahi hote.

3. **Result:**  
   - Is wajah se, even_generator(10) sirf pehla even number (2) return karta hai, aur aapko baqi even numbers nahi milte.

### Agar Aap Multiple Values Chahein:
Agar aap multiple even numbers return karna chahte hain, to aapko "yield" statement use karna chahiye. Jaise:

```python
def even_generator(num):
    for n in range(2, num+1, 2):
        yield n

for even in even_generator(10):
    print(even)
```

Is tarah se, "yield" har iteration ke baad value return karta hai, aur aapko 2, 4, 6, 8, 10 sab values milengi.

---

**Summary:**  
Aapka original code sirf pehla iteration execute hone ke baad return kar deta hai, isliye function se sirf ek hi value (2) milti hai.

_______________________________________________________________________________________________________
-------------------------------------------------------------------------------------------------------
## when we use return in loop:
Agar aap for loop ke andar return use karte hain, toh jaise hi return statement execute hota hai, function poori tarah se terminate ho jata hai, aur for loop ka baqi hissa chalna band kar deta hai. Yeh behavior aapko tab chahiye hota hai jab aapko koi specific condition milne par turant result return karna ho. 

Lekin agar aapko for loop ke tamam iterations se data collect karna ho, toh aap return ko loop ke andar nahi use karte. Uske bajaye, aap:

- **List ka istemal kar sakte hain:**  
  For loop mein har iteration mein value ko list mein add karein, aur loop ke baad list return karein.

- **Generator bana sakte hain (yield use karke):**  
  Yield statement har iteration ke baad value return karta hai aur function execution ko pause karta hai, taki baad mein agle iteration par continue kiya ja sake.
  
  "yield" ek aisa keyword hai jo function se ek value nikalne mein madad karta hai, lekin function ko poori tarah se rokta nahi hai. Matlab, jab aap "yield" use karte hain, to function temporary pause ho jata hai aur ek value return karta hai. Phir jab aap phir se us function ko call karte hain, to woh usi point se continue hota hai jahan pe pause hua tha. 


Is tarah se, agar aap for loop ke andar return use karte hain, toh woh sirf pehli iteration ke baad function se exit kar jaega. Isliye agar aapko multiple values chahiye, return ke bajaye list accumulation ya yield use karna behtar hai.

________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## behind the scene of yield:
Jab aap kisi function mein "yield" use karte hain, to Python us function ko ek **generator function** bana deta hai. Matlab, jab aap function ko call karte hain (jaise `even_generator(10)`), to woh turant ek **generator object** return karta hai—na ke seedha pehli yield value (jaise 2).

**Ye kaise kaam karta hai:**

1. **Generator Function:**  
   - Jab aap "yield" likhte hain, to Python samajhta hai ke yeh function generator hai.  
   - Function ko call karne par, woh immediately execute hona shuru nahi hota; balkay ek generator object return hota hai jo function ka code aur state (jaise variables) ko yaad rakhta hai.

2. **Generator Object:**  
   - Yeh ek special iterator hota hai.  
   - For loop ya `next()` function use karne se, generator object us function ko resume karta hai, jahan pe woh pehle "yield" hua tha, aur phir agla value generate karta hai.

3. **Example Scenario:**  
   - Aapka code:  
     ```python
     def even_generator(num):
         for n in range(2, num+1, 2):
             yield n
     
     # even_generator(10) call karne se ek generator object return hota hai.
     for num in even_generator(10):
         print(num)
     ```
   - Jab `even_generator(10)` call hota hai, function immediately ek generator object return karta hai.  
   - For loop generator object par iterate karta hai aur pehli baar `next()` call karne par, function execute hota hai aur pehla "yield" (2) return hota hai.  
   - Agli baar next() call par, function wahi se resume hota hai aur agla "yield" (4) deta hai, aur aise hi aage.

**Summary:**  
Yield statement directly ek single value return nahin karta; balkay, use karne se function ek generator object ban jata hai jo values ko on-demand (ek ek karke) generate karta hai jab aap us par iterate karte hain.


### internall working of for loop in iterable object:
Bilkul sahi! Jab aap ek iterable object (jaise ke generator object) par for loop lagate hain, to for loop internally us object ka next() method call karta hai. Iska matlab hai:

1. For loop iterable object se iterator leta hai.
2. Phir har iteration mein, for loop next() call karta hai.
3. Generator function usi point se resume hota hai jahan pe pichla yield hua tha, aur agla value yield karta hai.
4. Jab koi aur value na ho, to StopIteration exception raise hota hai aur loop terminate ho jata hai.

Is tarah, for loop next() ke zariye generator function ko bar bar call karta hai taake successive values milti rahein.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Recursive Function internal working:
Chaliye ek simple misal ke through samajhte hain:

### Misal:
Agar hum factorial(5) calculate karna chahein, to yeh likha jata hai:

  **factorial(5) = 5 * factorial(4)**

Lekin iska matlab yeh nahi ke pehle 5 ko turant kisi value se multiply kar diya jaye. Balkay, yeh likha gaya hai ke:

1. **Pehla kaam:**  
   Ab humein **factorial(4)** calculate karna hai. Matlab, function factorial(5) "ruk jata hai" aur uske andar ek naya call hota hai: **factorial(4)**.

2. **Ab factorial(4) ke liye:**  
   Yeh likha jata hai:  
  **factorial(4) = 4 * factorial(3)**
   Phir uske andar **factorial(3)** call hota hai.

3. **Yeh chain aise hi chalta hai:**  
  **factorial(3) = 3 * factorial(2)**  
  **factorial(2) = 2 * factorial(1)**  
  **factorial(1) = 1 * factorial(0)**  
  **factorial(0) = 1** (yeh base case hai)

4. **Ab calculations start hoti hain (unwinding):**  
   - **factorial(0)** return karta hai **1**.
   - Ab **factorial(1) = 1 * factorial(0) = 1 * 1 = 1**.
   - Phir **factorial(2) = 2 * factorial(1) = 2 * 1 = 2**.
   - Phir **factorial(3) = 3 * factorial(2) = 3 * 2 = 6**.
   - Phir **factorial(4) = 4 * factorial(3) = 4 * 6 = 24**.
   - Aakhir mein **factorial(5) = 5 * factorial(4) = 5 * 24 = 120**.

### Important Point:
- **Multiplication ka waqt:**  
  Jab aap likhte hain "5 * factorial(4)", function pehle **factorial(4)** ko calculate karta hai.  
  Jab factorial(4) ka result (24) mil jata hai, tab woh 5 ke saath multiply ho jata hai.  
  Is tarah, 5 se multiply tab hota hai jab aapko factorial(4) ka result mil jata hai.

### Ek Analogy:
Socho aap ek cake bana rahe ho jisme pehle base banana hai aur phir us base ko frosting ke saath multiply karna hai (ya add karna hai).  
- Pehle aap base (factorial(4) ka calculation) banate ho.  
- Jab base taiyaar ho jati hai, tab aap us base ko frosting (5) ke saath combine karte ho.  
Agar base pehle nahi bani, to aap frosting se multiply nahi kar sakte.

### Conclusion:
- **factorial(5) = 5 * factorial(4)** ka matlab hai "5 ko multiply karo factorial(4) se", lekin factorial(4) ko pehle calculate karna zaroori hai.
- Har recursive call function ko "rukhne" par majboor karti hai jab tak uski value calculate na ho jaye.  
- Jab base case mil jata hai (factorial(0) = 1), tab ye pending multiplications ek ek karke complete ho jati hain.

Umeed hai is tarah se aapko samajh aaya hoga ke recursion mein "n * factorial(n-1)" kaise kaam karta hai!



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Recursive Function kya hai?**

- **Seedhi Baat:**  
  Recursive function woh function hai jo apne aap ko call karta hai.

- **Kaise Kaam Karta Hai:**  
  Samajh lijiye aapko 5 se shuru karna hai aur phir har baar 1 ghatana hai jab tak 0 na ho jaye.  
  - Jab aap factorial(5) bolte hain, to function kehta hai:  
    "5 * (ab mujhe factorial(4) ka result chahiye)"  
  - Ab, factorial(4) ke liye woh function phir se khud ko call karta hai:  
    "4 * (ab mujhe factorial(3) chahiye)"  
  - Yeh chalta rehta hai jab tak aap base case (jaise factorial(0)) tak na pohonch jaye.
  - Jab base case (0) tak pohonch jate hain, to result simple ho jata hai (factorial(0) = 1).
  - Ab, yeh sab calls piche se multiply hote hain aur final answer mil jata hai.

- **Urdu Mein Matlab:**  
  Recursive ka matlab hai "اپنی تکرار" — matlab, khud ko baar baar istemal karna.

**Ek Aur Misal:**
Sochiye aapko ek ladder se neeche utarna hai:
- Pehle aap sochenge: "Main ab 1 step neeche utaroon, phir ladder ko dobara use karo"  
- Yeh process tab tak chalti hai jab tak aap neeche tak pohonch nahi jate.
  
Isi tarah, recursive function bhi apne aap ko use karta hai, har baar ek chhota hissa (step) complete karta hai, jab tak ki sab steps complete na ho jayein.

Umeed hai ab aapko asaan alfaaz mein samajh aa gaya hoga ke recursive function kya hota hai aur kaise kaam karta hai!


-------------------
Chaliye ek example se samajhte hain. Hum factorial(5) ka example lete hain:

1. **Function Calls (Recursion):**  
   - factorial(5) = 5 * factorial(4)  
   - factorial(4) = 4 * factorial(3)  
   - factorial(3) = 3 * factorial(2)  
   - factorial(2) = 2 * factorial(1)  
   - factorial(1) = 1 * factorial(0)  
   - factorial(0) = 1 (Base case)

2. **"Piche se Multiply Hona":**  
   Yeh phrase iska matlab hai ke jab hum base case (factorial(0)) tak pahunch jate hain, to wahan se calculation shuru hoti hai. Ab hum reverse order mein multiplication karte hain:

   - **Step A:**  
     Sabse pehle, factorial(0) ne 1 return kiya.  
     Ab factorial(1) ko compute karo:  
     factorial(1) = 1 * (result of factorial(0))  
                 = 1 * 1 = 1

   - **Step B:**  
     Ab factorial(2) compute karo:  
     factorial(2) = 2 * (result of factorial(1))  
                 = 2 * 1 = 2

   - **Step C:**  
     Ab factorial(3) compute karo:  
     factorial(3) = 3 * (result of factorial(2))  
                 = 3 * 2 = 6

   - **Step D:**  
     Ab factorial(4) compute karo:  
     factorial(4) = 4 * (result of factorial(3))  
                 = 4 * 6 = 24

   - **Step E:**  
     Aakhir mein, factorial(5) compute karo:  
     factorial(5) = 5 * (result of factorial(4))  
                 = 5 * 24 = 120

Iska matlab hai, jab aap base case se start karte hain (sabse neeche ka call, factorial(0)=1), to function calls stack se "pop" hote hue upar jate hain aur har call mein pehle call se return hui value ke sath multiplication hoti hai. Yeh process hi "piche se multiply hona" kehlata hai.

Agar aapko ek simple analogy se samjhana ho:  
Sochiye aap ek nayi recipe bana rahe hain jisme pehle sab ingredients ko ek ek karke taiyaar karna hai. Pehle aap base ingredient lete hain, phir us base ingredient ko use karte hue agli ingredient milate hain, aur aakhir mein sabko mila ke final dish ban jati hai. Isi tarah, recursion base case se shuru hota hai aur phir "piche se" (reverse order) sab results ko jod kar final answer milta hai.

Umeed hai ab aapko "piche se multiply hote hain" ka matlab aur process samajh aa gaya hoga!

