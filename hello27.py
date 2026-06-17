# =======================================================
# 1. FOR LOOP WITH ELSE (Normal execution)
# =======================================================
for i in range(5):
    print(i) # 0 se lekar 4 tak print karega
else:
    # 🟢 Kyunki loop bina kisi rukawat ke poora khatam hua, isliye else chalega!
    print("sorry no i") # Output: sorry no i


# =======================================================
# 2. EMPTY LOOP WITH ELSE (Khali list ka jadoo)
# =======================================================
for i in []:
    print(i) # List khali hai, toh loop ke andar ka code ek baar bhi nahi chalega
else:
    # 🟢 Kyunki loop ne apna kaam normal khatam kiya (chahe khali hi tha), else chalega!
    print("sorry no i") # Output: sorry no i


# =======================================================
# 3. FOR LOOP WITH BREAK 🚨 (The Big Exception)
# =======================================================
for i in range(6):
    print(i)
    if i == 4:
        break # 🛑 Loop ko beech mein se hi tod kar baahar nikal gaya!
else:
    # ❌ Kyunki loop normal khatam nahi hua, beech mein break hua, isliye yeh else NAHI chalega!
    print("sorry no i")


# =======================================================
# 4. WHILE LOOP WITH BREAK 🚨 (While ka dimaag)
# =======================================================
i = 0
while i < 7:
    i = i + 1
    print(i) # 1 se lekar 4 tak print karega
    if i == 4:
        break # 🛑 While loop ko bhi beech mein se tod diya!
else:
    # ❌ Loop break hone ki wajah se yeh else bhi bypass ho jayega, nahi chalega!
    print("sorry no i")


# =======================================================
# 5. STRING FORMATTING WITH LOOP ELSE
# =======================================================
for x in range(6):
    # .format(x + 1) se 1 se lekar 6 tak ki ginti sentence mein fit hogi
    print("iteration no {} in for  loop".format(x + 1))
else:
    # 🟢 Loop 6 baar chal kar normal khatam hua, toh else block chalega!
    print("else black in loop.")

# 🏁 Yeh toh loop ke ekdum baahar hai, toh yeh hamesha chalega hi chalega
print("out of loop")
