# =======================================================
# 1. OLD METHOD: .format() ka simple use
# =======================================================
letter = "hey my name is {} and i am from {}"
country = "india"
name = "vibhu"

# ➡️ Pehla variable pehle {} mein jayega, doosra doosre mein
print(letter.format(name, country))  # Output: hey my name is vibhu and i am from india

# 🚨 Galti check: Agar order badla toh sentence ka kachra ho jata hai
print(letter.format(country, name))  # Output: hey my name is india and i am from vibhu


# =======================================================
# 2. MODERN METHOD: f-strings (Sabse Best aur Modern)
# =======================================================
# 🟢 Direct curly brackets ke andar variables ka naam chipka diya
print(f"hey my name is {name} and i am from {country}")

# 🤫 Jadoo: Double curly brackets {{}} lagane se variable ki value print nahi hoti,
# balki woh brackets ke sath waisa ka waisa hi screen par chamak jata hai!
print(f"hey my name is {{name}} and i am from {{country}}") 
# Output: hey my name is {name} and i am from {country}


# =======================================================
# 3. INDEX METHOD: .format() mein numbering ka chakkar
# =======================================================
# 📐 {1} ka matlab hai format() ka doosra variable (name) aur {0} ka matlab pehla (country)
letter = "hey my name is {1} and i am from {0}"
country = "india"  # Index 0
name = "vibhu"     # Index 1

# Is wajah se country pehle hone par bhi 'name' sahi jagah fit hoga
print(letter.format(country, name)) # Output: hey my name is vibhu and i am from india


# =======================================================
# 4. MATHS & ROUND-OFF (f-strings ka asli dimaag)
# =======================================================
price = 49.67532
# ✂️ :.2f ka matlab hai point (.) ke baad sirf 2 numbers tak round-off karo
txt = f"for only {price: .2f} dollars!" 
print(txt)  # Output: for only  49.68 dollars!

# 🧮 f-strings ke andar tum direct math ka calculation bhi kar sakte ho!
print(f"{2 * 30}")  # Output: 60
