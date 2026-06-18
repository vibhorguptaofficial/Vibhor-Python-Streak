# =======================================================
# 1. THE BIG TRAP 🚨 (Bina define kiye index use karna)
# =======================================================
marks = [12, 56, 32, 98, 12, 45, 3, 4, 8]

for mark in marks:
    print(mark) 
    # ❌ Galti check: yeh line NameError degi! 
    # Kyunki pure computer ko pata hi nahi hai ki 'index' kya cheez hai.
    # if(index == 3):
    #     print("Vibhu, awesome!") 


# =======================================================
# 2. OLD METHOD (Manually index variable badhana)
# =======================================================
index = 0 # Manual counter shuru kiya
for mark in marks:
    print(mark) 
    if(index == 3):
        print("Vibhu, awesome!") # Index 3 (yaani chautha element 98) par print hoga
    index += 1 # 📐 Har loop ke sath index ko ek aage badhaya


# =======================================================
# 3. MODERN METHOD: Enumerate (Sabse VIP aur Short)
# =======================================================
# 👑 JADOO: 'enumerate' automatic loop ke sath index (0, 1, 2...) nikaal kar deta hai.
# Isme manually 'index += 1' likhne ka jhanjhat hi khatam!
for index, mark in enumerate(marks):
    print(mark) 
    if(index == 3):
        print("Vibhu, awesome!") # Default ginti 0 se shuru hui, toh 98 par chalega


# =======================================================
# 4. ENUEMRATE WITH CUSTOM START (Ginti badalna)
# =======================================================
# 📐 start=1 karne se computer ab 0 se nahi, balki 1, 2, 3 se ginti shuru karega!
for index, mark in enumerate(marks, start=1):
    print(mark) 
    if(index == 3):
        # 🔥 Magic: Ab ginti 1 se shuru hui hai, toh index 3 par teesra element '32' aayega!
        print("Vibhu, awesome!") 
