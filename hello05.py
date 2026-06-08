# 1. Simple Input: User se uska naam poochna
# Jo bhi user type karega, wo 'a' naam ke dabbe mein save ho jayega
a = input("enter your name:")
print("my name is", a)

# 2. Numbers ka khel:
x = input("enter first number:")  # Computer ise "String" (text) manega
y = input("enter second number:") # Computer ise bhi "Text" manega

# 3. Bina Typecasting ke:
# Yahan Python dono ko chipka dega (Concatenate). 
# Agar tumne 5 aur 6 dala, toh answer "56" aayega.
print(x + y)

# 4. Asli Maths (Typecasting ke saath):
# int(x) ka matlab hai: "Bhai x ke andar jo text hai, use asli number bana de"
print(int(x) + int(y)) # Ab 5 + 6 ka sahi answer 11 aayega
