# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

user_string = input("Enter a word to find the first non-repeating character: ").strip()

for char in user_string:
    print(char)
    if user_string.count(char) == 1:
        print(f"The first non-repeating character is: {char}")
        break

