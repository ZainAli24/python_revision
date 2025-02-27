# ▼8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak),
# 6-10 chars (Medium), >10 chars (Strong).


userPassword = input("Please Enter Your Password: ")

if len(userPassword) < 6:
    print("❌ Your password is too weak. Please use at least 6 characters.")
elif len(userPassword) >=6 and len(userPassword) <=10:
    print("⚠️ Your password is medium strength. Consider making it stronger.")
elif len(userPassword) >10 and len(userPassword) <=20:
    print("✅ Your password is strong! Great job!")
else:
    print("❌ Your password is too long. Please enter a maximum of 20 characters.")
