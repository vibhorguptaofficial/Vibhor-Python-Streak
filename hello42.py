# =======================================================
# 1. DIFFERENT DATA TYPES (Integer vs String)
# =======================================================
a = 4   # Integer
b = "4" # String

# ❌ Data type hi alag hai, toh na toh value same hai aur na hi memory location!
print(a is b) # Output: False (Exact location of object in memory)
print(a == b) # Output: False (Value check)


# =======================================================
# 2. IMMUTABLE CACHING (Integers, Strings, aur Tuples)
# =======================================================
a = 4
b = 4
# 🟢 Python memory bachane ke liye chote integers ko ek hi jagah save karta hai!
print(a is b) # Output: True (Dono ek hi memory address par hain)
print(a == b) # Output: True

a = "vibhu"
b = "vibhu"
# 🟢 Strings ke sath bhi same jadoo chalta hai (String Interning)
print(a is b) # Output: True 
print(a == b) # Output: True

a = (1, 2)
b = (1, 2)
# 🟢 Tuples immutable (na badalne wale) hote hain, isliye inki location bhi same ho sakti hai
print(a is b) # Output: True
print(a == b) # Output: True


# =======================================================
# 3. NONE TYPE CHECKING (Sabse standard standard format)
# =======================================================
a = None
b = None

# 👑 Professional Rule: None poore Python system mein ek single object hota hai,
# isliye isko hamesha 'is None' se check karna hi sabse best aur fast mana jata hai!
print(a is b)    # Output: True
print(a is None) # Output: True
print(a == b)    # Output: True
print(a == None) # Output: True


# =======================================================
# 4. MUTABLE EXCEPTION 🚨 (Lists ka khunkhar dappa)
# =======================================================
c = [1, 23, 45]
d = [1, 23, 45]

# 🪓 BRAHMASTRA POINT: Kyunki list mutable (badalne wali) hoti hai, 
# isliye computer dono ke liye memory mein ekdum alag-alag naye dabbe banata hai,
# taaki agar tum 'c' mein kuch badlo toh 'd' kharab na ho!
print(c is d) # 💥 Output: False (Kyunki dono ki memory locations ekdum alag hain!)
print(c == d) # 🟢 Output: True  (Kyunki dono ke andar ka maal/value ekdum same hai)
