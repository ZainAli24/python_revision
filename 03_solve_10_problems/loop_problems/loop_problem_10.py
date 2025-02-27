# ▼10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, 
# starting from 1 second, but stops after 5 retries.
import time 

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempts {attempts + 1} wait time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1


### **Conclusion:**
# - **Print pehle hoga**, jo bhi values hain wo display hongi.
# - **Phir `time.sleep(wait_time)` ke wajah se loop stop hoga** for given seconds.
# - **Phir wait_time double hoga** aur **attempts count increase hoga**.
# - **Agar attempts `max_retries` tak pohch gaya toh loop stop ho jayega.** 
