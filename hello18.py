# 📦 Ek Tuple banaya jisme integers, string aur boolean sab mix maal hai
tup = (1, 4, 5, 67, 54, "red", True)

# 🔬 Tuple ka type (class 'tuple') aur uske saare elements print kiye
print(type(tup), tup)

# ➡️ Positive Indexing (Aage se ginti 0 se shuru hoti hai)
print(tup[1])   # Output: 4  (Index 1 par 4 baitha hai)
print(tup[5])   # Output: "red" (Index 5 par string hai)
print(tup[3])   # Output: 67 (Index 3 par 67 hai)
print(tup[6])   # Output: True (Index 6 par last element hai)

# ⬅️ Negative Indexing (Peeche se ginti -1 se shuru hoti hai)
print(tup[-6])  # Output: 4  (Peeche se chhatha element)
print(tup[2])   # Output: 5  (Positive Index 2 par 5 hai)
print(tup[-4])  # Output: 67 (Peeche se chautha element)

# ✂️ Tuple Slicing (Index 1 se lekar 3 tak ka maal uthayega, 4 ko chhod dega)
tup2 = tup[1:4]
print(tup2)     # Output: (4, 5, 67)

# 🔎 Membership Check (Check kar raha hai ki kya 342 is parivaar mein hai?)
if 342 in tup:
    print("Yes 342 is present in this tuple") # Agar hota toh chalta, abhi yeh nahi chalega
