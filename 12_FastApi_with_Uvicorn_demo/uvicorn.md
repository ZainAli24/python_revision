### **Uvicorn Kya Hai?**
Uvicorn ek **ASGI server** hai jo Python mein use hota hai. ASGI ka matlab hai **Asynchronous Server Gateway Interface**. Yeh ek tarah ka tool hai jo web applications ko run karne ke liye server ka kaam karta hai. Yani, agar aapne koi Python web app banayi hai (jaise FastAPI ya Starlette), to Uvicorn us app ko internet par live karne mein madad karta hai.

### **Yeh Kya Kaam Karta Hai?**
Uvicorn ka main kaam hai aapki Python web application ko **host** karna aur usse **requests** (jaise users ke clicks ya form submissions) ko handle karna. Yeh kaam kuch is tarah karta hai:

1. **App Ko Run Karta Hai**: Jab aap apni web app ko start karte hain, Uvicorn usko ek server par chalata hai, taake woh browser ya API calls ke through accessible ho.
   - Misal: Agar aapne FastAPI se ek API banayi, to Uvicorn usko localhost (jaise `http://127.0.0.1:8000`) par chalata hai.

2. **Requests Ko Handle Karta Hai**: Jab koi user aapki app ko visit karta hai ya API call karta hai, Uvicorn us request ko aapki app tak pohanchata hai aur jawab wapas bhejta hai.

3. **Asynchronous Support**: Uvicorn asynchronous code (jaise `async` aur `await`) ko support karta hai, jo web apps ko tezi se kaam karne mein madad deta hai, khaas kar jab bohat saari requests ek saath aati hain.

### **Simple Misal**
Maan lo aapne FastAPI se ek chhoti si app banayi jo kehta hai "Hello, World!" jab koi `http://localhost:8000` pe jata hai. Uvicorn ka kaam hai yeh app ko server par chalana taake koi bhi browser ya tool us tak pohanch sake. Aap command line mein yeh command chalate hain:
```bash
uvicorn main:app --reload
```
- `main:app`: Yeh aapki app ka naam aur object hai.
- `--reload`: Yeh development ke liye hota hai, taake code mein changes hone par app apne aap restart ho.

### **Uvicorn Kyun Zaroori Hai?**
- **Tezi**: Yeh asynchronous hai, to bohat saari requests ko jaldi handle kar sakta hai.
- **Aasaan Setup**: FastAPI jaisi frameworks ke saath yeh bohat simple hai.
- **Development aur Production**: Yeh dono ke liye kaam karta hai—testing ke liye local server aur live apps ke liye production server.

### **Output**
Uvicorn ek server tool hai jo Python web apps (jaise FastAPI) ko internet ya local machine par chalata hai. Yeh user ke requests ko app tak le jata hai aur jawab wapas bhejta hai, aur asynchronous kaam karke tezi deta hai. Bas itna hi simple hai!


-----------
-----------
-----------

##  1. FastApi With Uvicorn installation command:
```python
uv pip install fastapi uvicorn
```

