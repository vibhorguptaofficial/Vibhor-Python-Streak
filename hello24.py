# ==========================================
# 🤝 1. UNION & UPDATE (Parivaar jodhna)
# ==========================================
s1 = {1, 2, 3, 4, 6}
s2 = {5, 6, 7}
# union(): Dono sets ka saaman jodh kar ek NAYA set banata hai, purane sets nahi badalte
print(s1.union(s2)) # Output: {1, 2, 3, 4, 5, 6, 7}

# update(): s2 ka saara maal utha kar s1 ke ANDAR hi daal deta hai (s1 badal jayega)
s1.update(s2)
print(s1, s2) 

# ==========================================
# 🎯 2. INTERSECTION (Common maal dhoondhna)
# ==========================================
cities = {"tokyo", "modrid", "berlin", "delhi"}
cities2 = {"tokyo", "seoul", "kabul", "modrid"}
# intersection(): Dono mein jo ekdum SAME/COMMON hai, uska ek naya set banata hai
cities3 = cities.intersection(cities2)
print(cities3) # Output: {'tokyo', 'modrid'}

# intersection_update(): Sirf common wale maal ko rakh kar baaki sab main set se uda deta hai
cities.intersection_update(cities2)
print(cities) # Output: {'tokyo', 'modrid'}

# ==========================================
# 🪓 3. DIFFERENCE (Alag maal nikalna)
# ==========================================
cities = {"tokyo", "modrid", "berlin", "delhi"}
cities2 = {"tokyo", "seoul", "kabul", "modrid"}
# symmetric_difference(): Jo common hain unhe CHHODKAR, baaki saare alag elements utha lega
cities3 = cities.symmetric_difference(cities2)
print(cities3) # Output: {'berlin', 'delhi', 'seoul', 'kabul'}

# difference(): Sirf 'cities' ke woh elements uthayega jo 'cities2' mein BILKUL nahi hain
cities3 = cities.difference(cities2)
print(cities3) # Output: {'berlin', 'delhi'}

# ==========================================
# 🔎 4. DISJOINT, SUPERSET & SUBSET (Checking tools)
# ==========================================
# isdisjoint(): Agar dono sets mein EK BHI element common hai, toh False dega (Kyunki yahan 'tokyo' common hai)
print(cities.isdisjoint(cities2)) # Output: False

cities0 = {"tokyo2", "modrid2", "berlin", "delhi"}
# Yahan dono mein kuch bhi common nahi hai, isliye True aayega
print(cities0.isdisjoint(cities2)) # Output: True

# issuperset(): Check karta hai ki kya cities3 ka SAARA maal cities ke paas pehle se hai?
cities3 = {"tokyo", "modrid", "delhi"}
print(cities.issuperset(cities3)) # Output: True

# issubset(): Check karta hai ki kya cities3 chota baccha hai jo bade 'cities' parivaar se nikal kar bana hai?
print(cities3.issubset(cities)) # Output: True

# ==========================================
# 🛠️ 5. ADD & REMOVE (Maal daalna aur nikalna)
# ==========================================
cities.add("india") # Set ke andar naya element jodh diya
print(cities)

# remove(): Element ko set se uda dega. 
# 🚨 WARNING: Agar woh element set mein nahi hua, toh remove() bada sa laal ERROR phenk dega!
cities.remove("tokyo") 

# discard(): Yeh ekdum shant hai. Element hua toh uda dega, NAHI hua toh chup rahega, ERROR NAHI DEGA!
cities.discard("tokyo") 

# pop(): Kisi bhi RANDOM (anjaan) element ko bahar nikal kar phenk deta hai aur batata hai kise nikala
item = cities.pop()
print(cities)
print(item) # Jo element delete hua, woh yahan dikhega

# 💡 VIP Note: Pure set ke dabbe ko hi memory se gayab karne ke liye 'del cities' likhte hain!
# del cities

# clear(): Dabbe ko delete nahi karta, bas uske andar ka saara maal saaf karke use ekdum KHALI set() bana deta hai
cities.clear()
print(cities) # Output: set()

# ==========================================
# 🔑 6. MEMBERSHIP OPERATOR (In/NotIn)
# ==========================================
info = {"carla", 19, 5.9, False}
if "carla" in info:
    print("carla is present.") # Carla hai, toh yeh print hoga
else:
    print("carla is absent.")
