# 1. Explicit Typecasting (Humne khud bataya)
# Yahan 'a' aur 'b' strings hain (dabbe mein band hain)
a = "1"
b = "2"

# Agar hum int(a) + int(b) nahi karte, toh Python "12" print kar deta (chipka deta)
print((a) + (b))
# int() laga kar humne Python ko bola: "Bhai isey number ki tarah treat kar"
print(int(a) + int(b)) # Output: 3


# 2. Implicit Typecasting (Python ka apna dimaag)
# Jab hum seedha numbers ko jodte hain, toh Python khud samajh jata hai 
# ki ye integers hain aur inhe kaise jodna hai.
c = 9
d = 4

print(c + d) # Output: 13
