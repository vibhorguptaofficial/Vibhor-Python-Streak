# ==========================================
# 🤝 1. UPDATE (Do Dictionaries ko jodhna)
# ==========================================
ep1 = {122: 45, 123: 89,  221: 67, 134: 55}
ep2 = {222: 78, 556: 99}

# update(): ep2 ka saara maal utha kar ep1 ke andar merge kar dega
ep1.update(ep2)
print(ep1) # Output: {122: 45, 123: 89, 221: 67, 134: 55, 222: 78, 556: 99}

# ==========================================
# 📭 2. CLEAR (Dabbe ko khali karna)
# ==========================================
ep1 = {122: 45, 123: 89,  221: 67, 134: 55}
# clear(): Dictionary ke dappe ko delete nahi karega, bas uske andar ka saara maal saaf kar dega
ep1.clear()
print(ep1) # Output: {} (Ekdum khali dictionary)


# ==========================================
# ✂️ 3. POP & POPITEM (Maal bahar nikalna)
# ==========================================
ep1 = {122: 45, 123: 89,  221: 67, 134: 55}
# pop(): Jo specific key tum doge (jaise 122), yeh usko aur uski value ko uda dega
ep1.pop(122)
print(ep1) # Output: {123: 89, 221: 67, 134: 55}

ep1 = {122: 45, 123: 89,  221: 67, 134: 55}
# popitem(): Yeh bina puche ekdum LAST waale key-value pair ko nikal kar phenk deta hai!
ep1.popitem()
print(ep1) # Output: {122: 45, 123: 89, 221: 67} (134:55 gayab ho gaya)


# ==========================================
# 🪓 4. DEL KEYWORD (Jad se khatam karna)
# ==========================================
ep1 = {122: 45, 123: 89,  221: 67, 134: 55}

# 🚨 del ep1: Agar sirf itna likhoge toh poora ep1 variable hi memory se delete ho jayega, 
# jisse baad mein print karne par 'NameError' aayega!

# del ep1[122]: Yeh specific key '122' ko jad se mita dega
del ep1[122]

# 🤫 SHATIR OBSERVATION :
# del ep1["122"] -> Yeh line 100% ERROR degi! Kyunki upar key integer (122) hai,
# aur hum dhoondh string ("122") rahe hain. Data Type ka hamesha dhyan rakhna hai!
print(ep1) # Output: {123: 89, 221: 67, 134: 55}


# ==========================================
# 📦 5. EMPTY DICTIONARY (Khali Dabba)
# ==========================================
empt = {}
print(empt) # Output: {}
