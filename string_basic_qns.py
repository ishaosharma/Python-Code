# s = "string in python"
# print(s.capitalize())
# print(s.title())

# s1 = 'STRING'
# print(s1.lower())

# su = 'str upper fun'
# print(su.upper())

# s5 ='THIs IS tEST'
# print(s5.swapcase())

# s6 = 'Python is good programming'
# print(s6.replace("good", "easy")) 

#1st assignment of slice-Extract specing Patterns of string
test_string = "Python Programming Practice for Advanced Developers"
print(test_string)

# 1. First 6 Characters
print("First 6 Characters:", test_string[:6])  # Output: 'Python'   gets indices 0–5.

# 2. Extract characters at odd indices
print("Odd Indices:", test_string[1::2])  # Starts at index 1, steps by 2    
#Odd Indices: [1::2] starts at 1, jumps by 2 (indices 1, 3, ...).

# 3. Extract characters at even indices
print("Even Indices:", test_string[0::2])  # Starts at index 0, steps by 2
#Even Indices: [0::2] starts at 0, jumps by 2 (indices 0, 2, ...).

# 4. Every 3rd Character imp cuz mene galat kia
print("Every 3rd Character:", test_string[::3])  # Steps by 3
#Every 3rd Character: [::3] starts at 0, takes every third character.

# 5. Substring from index 5 to 14
print("Index 5 to 14:", test_string[5:15])  # Indices 5 up to 14
#Substring (5 to 14): [5:15] grabs indices 5 up to 14.

# 6. Substring from last 10 characters IMP
print("Last 10 Characters:", test_string[-10:])  # Last 10 chars
#Last 10 Characters: [-10:] slices the last 10 characters.

# 7. Reverse String
print("Reverse String:", test_string[::-1])  # Reverse whole string
#Reverse String: [::-1] reverses the full string.

# 8. Reversed substring from index 5 to 14   NHI
print("Reversed (5 to 14):", test_string[5:15][::-1])  # 5-14 then reversed
#Reverse Substring (5 to 14): [5:15][::-1] slices then reverses.

# 9. Substring from Index+ i.e 0 to 14 with Step 2 (assuming Index+ means index 0)
print("Index 0 to 14 Step 2:", test_string[0:15:2])  # 0-14 step 2
#Substring (0 to 14, step 2): [0:15:2] from 0 to 14, every 2nd character.

# 9. Substring from Index 4 to 14 with Step 2 
print("Index 4 to 14 Step 2:", test_string[4:15:2])  # 0-14 step 2
#Substring (4 to 14, step 2)

# 10. Check Substring Presence and Index
substr = "Practice"
is_present = substr in test_string
first_at = test_string.find(substr)
print(f"Substring '{substr}' present:", is_present)
print(f"Index of '{substr}':", first_at if is_present else "Not Found")
#Check Substring: "Practice" in string for presence, .find() for index.


#negative indexing operations


