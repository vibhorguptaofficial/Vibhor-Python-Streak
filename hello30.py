# =======================================================
# 1. NUMERIC CUSTOM ERROR (Sankhya ka check)
# =======================================================
a = int(input("enter any value between 5 and 9: "))

# 📐 Agar user ne 5 se chota (jaise 3) ya 9 se bada (jaise 12) number dala
if(a < 5 or a > 9):
     # 🚨 BRAHMASTRA: 'raise' keyword ka use karke hum computer ko zabardasti 
     # gussa dila sakte hain aur apna custom error message screen par phenk sakte hain!
     raise ValueError("value sholud be between 5 and 9")


# =======================================================
# 2. STRING MATCHING CUSTOM ERROR (Quit ka check)
# =======================================================
a = input("enter the word 'quit': ")

# 🔤 Agar user ne 'quit' ke alawa kuch bhi aur likha (jaise 'exit' ya 'vibhu')
if a != "quit":
     # 🚨 Computer turant yahan code tod dega aur laal rang mein hamara message print karega!
     raise ValueError(" Error: word sholud be excalyt 'quit'!")
