## **1. We install Virtual Environment package:**
```python
pip install virtualenv
```

## **2. After installation, We create Virutal Environment with two commands:**
```python
virtualenv env_name
```
or
```python
python -m venv <environment_name>
```
env_name or <environment_name> is virtual environment name

## **3. After Creating Virtual Environment, We need to __activate__ Virtual Environment:**
```python
.\env_name\Scripts\activate
```

## **4. Deactivate use:**

**`deactivate` likhne se hum virtual environment se bahar aa jate hain.** 

Jab aap ek virtual environment mein hote hain (jaise `source venv/bin/activate` ya `venv\Scripts\activate` se activate karte hain), aur aap `deactivate` command run karte hain, toh yeh aapko us virtual environment se exit kar deta hai aur aap wapas global Python environment mein aa jate hain. Bas itna simple hai!

-----------

## **1. pip list > requirement.txt breakdown:**
Chaliye, command `pip list > requirement.txt` ka kaam simple Urdu mein samajhte hain, English likh kar.

### **Yeh Command Kya Hai?**
Yeh ek terminal ya command-line command hai jo Python ke package manager `pip` ka use karta hai. Iska kaam hai aapke current Python environment mein install kiye gaye sabhi packages ki list ko ek file mein save karna.

### **Breakdown of the Command**
1. **`pip list`**:
   - Yeh `pip` ka ek sub-command hai.
   - Iska kaam hai aapke Python environment mein install kiye gaye sabhi packages aur unke versions ko list karna.
   - Jab aap `pip list` chalate hain, toh terminal mein ek output aata hai, jaise:
     ```
     Package    Version
     ---------- -------
     numpy      1.21.0
     pandas     1.3.0
     pymongo    4.0.1
     ```
     Yeh dikhata hai ke kaunse packages install hain aur unke versions kya hain.

2. **`>`**:
   - Yeh ek **redirection operator** hai jo terminal ke output ko kisi file mein save karta hai.
   - Is case mein, `pip list` ka output jo terminal mein dikhna tha, woh seedha ek file mein chala jata hai.

3. **`requirement.txt`**:
   - Yeh us file ka naam hai jisme `pip list` ka output save hoga.
   - Agar yeh file pehle se nahi hai, toh nayi file ban jati hai. Agar hai, toh woh overwrite ho jati hai.

### **Yeh Command Kya Kaam Karta Hai?**
Jab aap `pip list > requirement.txt` chalate hain, toh:
- `pip list` aapke environment ke sabhi packages aur unke versions ki list banata hai.
- Yeh list terminal mein dikhne ke bajaye `requirement.txt` naam ki file mein save ho jati hai.
- File ka content kuch is tarah dikhega:
  ```
  Package    Version
  ---------- -------
  numpy      1.21.0
  pandas     1.3.0
  pymongo    4.0.1
  ```

### **Iska Practical Use Kya Hai?**
Yeh command tab kaam aata hai jab aap apne project ke dependencies ko track karna chahte hain ya doosron ke saath share karna chahte hain. Lekin ek baat dhyan rakhne wali hai: `pip list > requirement.txt` jo file banata hai, woh **standard requirements.txt format** mein nahi hoti. Standard format mein sirf package naam aur version hota hai, jaise:
```
numpy==1.21.0
pandas==1.3.0
pymongo==4.0.1
```

`pip list` ka output table format mein hota hai, jo `pip install -r requirements.txt` ke liye directly kaam nahi karta. Isliye, agar aapka maqsad ek proper `requirements.txt` file banana hai jo doosre environments mein use ho sake, toh yeh command behtar hai:
```bash
pip freeze > requirements.txt
```

### **`pip freeze` vs `pip list`**
- **`pip list`**: Saare install kiye gaye packages ki list deta hai, table format mein, jo zyada human-readable hai.
- **`pip freeze`**: Packages ko `requirements.txt` ke standard format mein deta hai (jaise `package==version`), jo `pip install` ke liye perfect hai.

### **Example**
1. Agar aap `pip list > requirement.txt` chalate hain, toh file aisi banegi:
   ```
   Package    Version
   ---------- -------
   numpy      1.21.0
   pandas     1.3.0
   pymongo    4.0.1
   ```
   Lekin is file ko `pip install -r requirement.txt` ke liye use nahi kar sakte kyunki format galat hai.

2. Agar aap `pip freeze > requirements.txt` chalate hain, toh file aisi banegi:
   ```
   numpy==1.21.0
   pandas==1.3.0
   pymongo==4.0.1
   ```
3. Is file ko aap kisi bhi Python environment mein use kar sakte hain dependencies install karne ke liye:
   ```bash
   pip install -r requirements.txt
   ```
    `-r` ka matlab hai **"requirements"**. Yeh `pip install` command mein ek option (flag) hai jo batata hai ke aap ek file se dependencies install karna chahte hain. Jab aap `pip install -r requirements.txt` likhte hain, to `-r` yeh indicate karta hai ke `requirements.txt` naam ki file mein listed packages aur unke versions ko read karke install karna hai.

    Simple zubaan mein: `-r` bolta hai, "Is file ke andar jo packages likhe hain, unko install karo."

------

### **Conclusion**
- `pip list > requirement.txt` ka kaam hai aapke Python environment ke saare packages aur unke versions ki list ko ek file (`requirement.txt`) mein save karna, table format mein.
- Yeh command zyada tar debugging ya packages check karne ke liye useful hai, lekin agar aapko ek proper `requirements.txt` file chahiye jo doosre environments mein kaam kare, toh `pip freeze > requirements.txt` use karein.

Agar aapko yeh file banana hai taki aap apne project ke dependencies share kar sakein, toh `pip freeze` wala command behtar hai!