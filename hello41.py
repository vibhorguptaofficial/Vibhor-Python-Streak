# =======================================================
# 🗺️ 1. MAP METHOD (Sab par ek saath jadoo chalana)
# =======================================================
def cube(x):
    return x*x*x

print(cube(2)) # Output: 8

l = [1, 2, 5, 8, 9, 7, 4]

# 🐌 Purana aalsi tarika: For loop chala kar manually list mein append karna
newl = []
for items in l:
    newl.append(cube(items))

# 🚀 Tarika A: 'map' lagakar ek jhatke mein poori list ka cube nikaala
newl = list(map(cube, l)) # Output: [1, 8, 125, 512, 729, 343, 64]

# 🚀 Tarika B: Bina 'def' function banaye, direct lambda ke sath map chalaya
newl = list(map(lambda x: x*x*x, l))

# 🚨 VIP OBSERVATION: Agar list() nahi lagaoge, toh computer data nahi dikhayega, 
# balki sirf ek anjaan memory address '<map object at 0x...>' dega!
newl = map(cube, l)
print(newl) 


# =======================================================
# 🪓 2. FILTER METHOD (Chhanani lagakar maal nikalna)
# =======================================================
def filter_function(a):
    return a > 2 # 📐 Sirf wahi numbers pass honge jo 2 se bade hain

# Filter bhi map ki tarah object deta hai, isliye isko bhi list() mein band kiya
newnewl = list(filter(filter_function, l))
print(newnewl) # Output: [5, 8, 9, 7, 4] (1 aur 2 automatic chhan gaye!)


# =======================================================
# 🧮 3. REDUCE METHOD (Poori list ko nichod kar ek number banana)
# =======================================================
# 👑 VIP IMPORT: Reduce in-built nahi hota, isey 'functools' parivaar se bulana padta hai
from functools import reduce

numbers = [4, 5, 3, 6, 7, 4, 5]

def mysum(x, y):
   return x + y

# 🧮 Logic Breakdown: Pehle 4+5=9 karega, fir 9+3=12, fir 12+6=18... poori list ko jod dega!
# 🛠️ Variable name 'sum' ko badal kar 'total_sum' kiya taaki built-in function safe rahe
total_sum = reduce(mysum, numbers)
print(total_sum) # Output: 34
