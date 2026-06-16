# ==========================================
# 📖 1. DICTIONARY DEFINITION (Key-Value ka dhanda)
# ==========================================
dic = {
    "vibhu": "Human being",
    "spoon": "object"
}
# Direct Key ka naam likhkar uski Value ko bahar nikal liya
print(dic["vibhu"],  dic["spoon"]) # Output: Human being object

# Dictionary ke andar Keys hamesha unique hoti hain, par values mix ho sakti hain
dic = {
    "344": "vibhu",
    "98": "harry",
    "348": "rahul",
    "988": "neha",
}
print(dic["348"]) # Output: rahul

# ==========================================
# 🔬 2. DICTIONARY METHODS (Keys, Values aur Keys nikalna)
# ==========================================
info = {'name':'karan', 'age': 19, 'eligible': True}
print(info)
print(info['name']) # Output: karan

# .keys(): Pure parivaar ki saari chabiyan (Keys) ek saath nikal lega
print(info.keys()) # Output: dict_keys(['name', 'age', 'eligible'])

# .values(): Saari keys ke andar ka maal (Values) ek saath nikal lega
print(info.values()) # Output: dict_values(['karan', 19, True])

# 👑 THE BIG DIFFERENCE 
# .get() tool ekdum shant hai. Agar key nahi mili, toh chupchaap 'None' dega, error nahi dega.
print(info.get('eligible2')) # Output: None

# 🚨 Lekin direct square brackets lagane par agar key nahi mili, toh code turant TOOT jayega!
# print(info['eligible2']) # -> KeyError dega kyunki 'eligible2' exists hi nahi karta!

# ==========================================
# 🔄 3. DICTIONARY LOOPING (Chabiyon aur maal ke sath khelna)
# ==========================================
# Tarika 1: Sirf keys nikal kar unke raste se values ko print karna
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

# .items(): Keys aur Values dono ka ekdum joda (Pairs) bana kar bahar nikalta hai
print(info.items()) 

# Tarika 2: Direct 'key, value' ka jadoo chalakar ek saath dono ko loop mein print karna
for key, value in info.items():
     print(f"The value corresponding to the key {key} is {value}")
