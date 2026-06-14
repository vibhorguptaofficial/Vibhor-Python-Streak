# ==========================================
# 🛠️ TUPLE MODIFICATION TRICK (Badlav karne ka jugaad)
# ==========================================
countries = ("india", "japan", "nepal", "america", "china")

temp = list(countries)  # 🔄 Step 1: Tuple ko pehle list mein badla taaki badlav ho sake
temp.append("ruusia")   # ➕ Step 2: Naya desh "russia" list mein jodh diya
temp.pop(3)            # ❌ Step 3: Index 3 par baithe "america" ko nikal phekka
temp[2] = "iland"       # 📝 Step 4: Index 2 wale "nepal" ki jagah "iland" likh diya

countries = tuple(temp) # 🔄 Step 5: List ko wapas standard Tuple mein badal diya
print(countries)        # Output: ('india', 'japan', 'iland', 'china', 'ruusia')

# ==========================================
# 🔗 TUPLE CONCATENATION (Do parivaar aapas mein jodhna)
# ==========================================
countries = ("india", "japan", "nepal", "america", "china")
countries2 = ("shri lanka", "india", "pakistan")

# 🤝 Dono alag-alag tuples ko '+' se chipka kar ek bada naya tuple banaya
southeastaisa = countries + countries2
print(southeastaisa)

# ==========================================
# 📊 TUPLE METHODS (Ginna aur rasta dhoondhna)
# ==========================================
tuple1 = (0, 9, 5, 4, 3, 3, 6, 7, 3, 2, 3)

# 🔢 1. COUNT: Check karega ki pure parivaar mein '3' kitni baar aaya hai
res = tuple1.count(3)
print('count of 3 in tuple is:', res)  # Output: 4

# 🔍 2. INDEX (Simple): Shuruat se check karega ki pehla '3' kaunse number par baitha hai
res = tuple1.index(3)
print('index of 3 in tuple is:', res)  # Output: 4 (Index 4 par pehla 3 hai)

# 🎯 3. INDEX (With Window): Sirf index 4 se lekar index 8 ke beech mein '3' ko dhoondhega
res = tuple1.index(3, 4, 8)
print('index of 3 in tuple is:', res)  # Output: 4 (Kyunki index 4 khud is window mein shamil hai)

# 📏 4. LENGTH: Check karega ki is tuple mein total kitne akshar/numbers hain
res = len(tuple1)
# 🛠️ VIP Correction: Print ka text humne 'length' ke hisab se sahi kar diya hai
print('Length of tuple1 is:', res)     # Output: 11
