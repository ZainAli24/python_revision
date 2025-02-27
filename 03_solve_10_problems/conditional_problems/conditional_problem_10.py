# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years -Puppy food, Cat: >5 years - Senior cat food).

userPet = input("Enter your pet type (Cat or Dog): ").strip().lower()
petYear = int(input("Enter your pet's age in years: "))

if userPet in ["cat" , "dog"]:
    if userPet == "cat":
        if petYear < 5:
            print("Recommended: Baby cat food for your young cat. 🐱")
        else:
            print("Recommended: Senior cat food for your adult cat. 🐱")

    elif userPet == "dog":
        if petYear < 2:
            print("Recommended: Puppy food for your young dog. 🐶")
        else:
            print("Recommended: Senior dog food for your adult dog. 🐶")
else:
    print("Invalid pet type! Please enter either 'Cat' or 'Dog'.")
