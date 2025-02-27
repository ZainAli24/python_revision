# 4. Reverse a String
# Problem: Reverse a string using a loop.

user_string = input("Enter a word to see its reverse: ").strip()
reverse_str = ""

for char in user_string:
    reverse_str = char + reverse_str
print(f"The reverse of '{user_string}' is: '{reverse_str}'")
