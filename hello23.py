# =======================================================
# 1. SET DEFINITION & UNIQUE VALUES (Set ka basic dimaag)
# =======================================================
s = {2, 4, 2, 6}
# 🤫 VIP RULE: Set kabhi bhi duplicate values ko bardasht nahi karta!
# Isliye jab tum 's' ko print karoge, toh extra '2' automatic gayab ho jayega.
print(s)  # Output: {2, 4, 6}

# Set ke andar tum integers, string, aur boolean sab mix maal daal sakte ho
info = {"carla", 19, False, 5, 9, 19}
# 🚨 Jadoo check: Ek toh duplicate '19' hat jayega, aur doosra—Set ka koi fixed order (index) nahi hota!
# Isliye har baar run karne par saaman aage-piche (Unordered) dikhega.
print(info) 


# =======================================================
# 2. THE BIG TRAP: Khali Set banane ka sahi jugaad
# =======================================================
vibhu = {}
# ❌ Galti check: Agar tum khali curly brackets likhoge, toh Python use 'Set' nahi maangega!
# Python ko lagega yeh ek khali Dictionary hai.
print(type(vibhu))  # Output: <class 'dict'>

vibhu = {0}
# Agar brackets ke andar ek bhi number (jaise 0) daal diya, toh woh automatic Set ban jata hai.
print(type(vibhu))  # Output: <class 'set'>

vibhu = set()
# 👑 MASTERSTROKE: Python mein ekdum khali Set banane ka asli aur professional tarika yahi hai!
print(type(vibhu))  # Output: <class 'set'>

vibhu1 = {0}
print(len(vibhu1))  # ➡️ Output: 1 (Kyunki iske andar '0' naam ka ek sadasya baitha hai!)

# 📭 2. Ekdum Khali Set
vibhu2 = set()
print(len(vibhu2))


# =======================================================
# 3. SET LOOPING (Set ke parivaar se milna)
# =======================================================
# Kyunki Set mein koi index (tup[0] ya list[0]) nahi hota, isliye iska saaman nikalne ke liye
# hamesha 'for loop' ka hi hathiyar chalana padta hai!
for value in info:
    print(value) # 'info' ke saare elements ek-ek karke neeche print ho jayenge
