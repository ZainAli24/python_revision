## 1. internal working of decorator in python:
Dekorators mein, function definition ke waqt hi timer function call hota hai aur woh aapke original function ko wrap karta hai bina usko immediately execute kiye hue. Iska matlab hai:

1. **Decorator Application at Definition Time:**  
   Jab aap likhte hain:
   ```python
   @timer
   def example_function(n):
       time.sleep(n)
   ```
   Python internally isko convert karta hai:
   ```python
   def example_function(n):
       time.sleep(n)
   
   example_function = timer(example_function)
   ```
   Yahan **timer(example_function)** call hota hai immediately jab function define hota hai. Lekin is call mein, timer function **wrapper** function ko return karta hai—na ke usko execute karke uska result de de.

2. **Assignment Without Execution:**  
   Important baat yeh hai ke aap **wrapper()** ko call nahi kar rahe. Aap sirf **wrapper** ko return kar rahe hain. Matlab:
   ```python
   example_function = wrapper
   ```
   Ab, **example_function** variable ek function object (wrapper) ko point karta hai, jo ki ek callable hai.

3. **Call Time Execution (example_function(3))**  
   Jab aap **example_function(3)** call karte hain, asal mein aap **wrapper(3)** call kar rahe hote hain.  
   - Yahan, argument **3** automatically **wrapper** ke parameter **\*args** mein store ho jata hai.  
   - **Wrapper** function ke andar, hum likhte hain:
     ```python
     result = func(*args, **kwargs)
     ```
     Is mein **func** wo original function hai (jo timer mein pass hua tha), aur **\*args** mein aapka argument **3** aa jata hai. Is tarah, original function ko **3** pass ho jata hai.

4. **Summary of the Flow:**  
   - **Definition Time:**  
     Decorator call hota hai: **example_function = timer(example_function)**.  
     Yahan, **timer** function return karta hai **wrapper** function ko as a function object, lekin wrapper ko execute nahi karta.  
   - **Call Time:**  
     Jab **example_function(3)** call hota hai, woh actually **wrapper(3)** execute karta hai.  
     - **3** value **\*args** mein aa jati hai.  
     - Wrapper ke andar, original function ko **func(*args, **kwargs)** ke zariye call kiya jata hai jisse original function ko **3** parameter milta hai.

Is tarah se, decorator ka mechanism ensure karta hai ke aapke function ko modify karke usme extra functionality (jaise ke timing) add ho jati hai, bina original function ko directly modify kiye hue.  
   
Ye internal working samjha deti hai ke kaise example_function ko decorate karne se, woh wrapper function ko point karta hai aur call time par arguments usme transfer ho jate hain. citeturn0search0


_______________________________________________________________________________
## 2. problem 03 kwargs confusion:
Chaliye detail se samjhte hain:

- **kwargs ek dictionary hoti hai, na ke tuple.  
  Jab aap function call karte hain aur keyword arguments pass karte hain, to **kwargs uss function ke andar ek dictionary ke roop mein aati hai.  
  Example:  
  ```python
  def func(**kwargs):
      print(kwargs)
  
  func(name="zain", age=30)
  ```  
  Iska output hoga:  
  ```python
  {'name': 'zain', 'age': 30}
  ```

- Dictionary mutable (badalne wali) hoti hai aur uska order fix nahi hota, matlab aap ke pass hamesha ek hi order mein items nahi milte.  
  Aur sab se important baat, dictionary directly hashable (ya "safe" key) nahi hoti, isliye aap dictionary ko caching key ke roop mein use nahi kar sakte.

- Ab, jab hum likhte hain:  
  ```python
  kv = tuple(sorted(kwargs.items()))
  ```
  Ye teen cheezein karta hai:  
  1. **kwargs.items()**: Dictionary ke items ko (key, value) pairs ki form mein leta hai.  
  2. **sorted(kwargs.items())**: Ye in items ko sort karta hai, usually keys ke hisaab se, taake order fix ho jaye.  
  3. **tuple(...)**: Sorted list ko immutable tuple mein convert kar deta hai, jo ke hashable hota hai.

- **Key Banane Ka Maqsad:**  
  Caching ke liye, aapko ek unique aur consistent key chahiye jo function call ke inputs ko represent kare.  
  Agar aap sirf **kwargs ko as-is use karte, to aapko dictionary milti, jisko directly key ke roop mein use nahi kar sakte.  
  Isliye, hum us dictionary ko sorted tuple mein convert karte hain.

**Summary:**  
- **kwargs dictionary hai, tuple nahi.**  
- Sorted tuple banane se:  
  - Aapko items ka consistent order milta hai.  
  - Tuple immutable hai aur cache key ke liye suitable (hashable) hai.  

Is liye, ye conversion zaruri hai, taki aap reliable tareeke se keyword arguments ko caching key ka hissa bana sakein.

___________________________________________________________________--
## 3. cached_value print confusion:
    
    cached_value = {}   
    print("empty", cached_value)    is mien cached_value ik baar kue print howe hai  jab ke hum ne function ko 3 bbar call kia hai  
    
Jab aap decorator use karte hain, to decorator function (yani `decorator(func)`) function definition ke waqt execute hota hai. Is waqt hi `cached_value = {}` initialize hota hai aur `print("empty", cached_value)` bhi execute hota hai. Ye print statement sirf ek baar, jab function decorate hota hai, chalti hai.

Uske baad, jab aap decorated function ko call karte hain, to aap `wrapper(*args, **kwargs)` call kar rahe hote hain, na ke decorator function ko dubara. Is wajah se "empty {}" print nahin hota, balkay sirf wrapper ka code execute hota hai jo cache check karta hai aur result return karta hai.

**Summary:**

- **Decorator Execution:**  
  Jab aap `@decorator` lagate hain, to decorator function execute hota hai sirf ek baar, jab function define ho raha hota hai. Is waqt `cached_value` create hota hai aur "empty {}" print hota hai.

- **Wrapper Execution:**  
  Har function call par, sirf wrapper function execute hota hai, jo ke cached_value ko check karta hai. Is waqt decorator ke andar jo initial print thi, wo dobara execute nahin hoti.

Isliye, aapka "empty {}" message sirf ek baar print ho raha hai, chahe aap function ko 3 ya us se zyada baar call karein.
