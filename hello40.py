# =======================================================
# 1. NORMAL FUNCTION (Purana tareeqa 'def' ke sath)
# =======================================================
def double(x):
    return x*2

# 👑 HIGHER-ORDER FUNCTION: Yeh ek aisa VIP function hai jo apne pet 
# ke andar ek doosre function ('fx') ko argument ki tarah leta hai!
def appl(fx, value):
    return 6 + fx(value)


# =======================================================
# 2. LAMBDA FUNCTIONS (Single line wale shortcut chhotu)
# =======================================================
# lambda argument: expression (Isme 'return' shabd likhna nahi padta)
double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y: (x + y) / 2 # Do variables wala lambda function

print(double(5)) # Output: 10
print(cube(5))   # Output: 125
print(avg(3, 5)) # Output: 4.0


# =======================================================
# 3. THE MASTER STROKE: Lambda inside Higher-Order Function 👑
# =======================================================
# Tarika A: Pehle se bane hue lambda variable 'cube' ko pass kiya
# Logic: 6 + cube(2) -> 6 + (2*2*2) -> 6 + 8 = 14
print(appl(cube, 2)) # Output: 14

# 🤫 SHATIR OBSERVATION (Jo tumne ekdum perfect pakda):
# Tarika B: Bina koi variable ya bada function banaye, direct line ke andar hi lambda chipka diya!
# Isse code ekdum saaf ho jata hai aur memory bhi bachti hai.
print(appl(lambda x: x * x * x, 2)) # Output: 14
