# =======================================================
# 1. THREE-WAY SHORT HAND (If-Elif-Else ka single line jadoo)
# =======================================================
a = 303
b = 3003

# 📐 Logic breakdown: 
# Pehle check karega 'a > b' -> Agar hai, toh "A" print karega.
# Agar nahi hai, toh automatic sarak kar next condition 'a == b' check karega -> Agar hai, toh "=" print karega.
# Agar dono nahi hain, toh aakhiri mein baitha "B" print ho jayega!
print("A") if a > b else print("=") if a == b  else print("B") # Output: B


# =======================================================
# 2. VARIABLE ASSIGNMENT SHORT HAND (Value store karne ka shortcut)
# =======================================================
# 💰 Agar 'a > b' hai toh 'c' ki value 9 hogi, warna 'c' ke pet mein 0 chala jayega!
c = 9 if a>b else 0
print(c) # Output: 0


# =======================================================
# 3. CONDITIONAL PRINT WITH EMPTY ELSE (Chalao ya shaant raho)
# =======================================================
# 🤫 Python ka strict rule hai: Short hand 'if' ke sath 'else' lagana COMPULSORY hai!
# Isiliye tumne 'else' ke aage khali string "" lagayi hai taaki condition galat hone par kuch na ho aur error bhi na aaye.
print(9) if a<b else "" # Output: 9 (Kyunki 303 chota hai 3003 se)
