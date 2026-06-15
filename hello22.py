# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# =======================================================
# 🪆 RECURSION ENGINE: Factorial ka calculation
# =======================================================

# Factorial ka mathematical rule: factorial(n) = n * factorial(n-1)
def factorial(n):
    # 🛑 BASE CASE: Agar n ki value 0 ya 1 hai, toh loop ko roko aur 1 return karo,
    # warna computer hamesha ke liye peeche (minus) mein bhaagta rahega!
    if(n==0 or n==1):
        return 1
    else:
        # 🔄 RECURSIVE CALL: Function khud ko hi dobara call kar raha hai n-1 ke sath
        return n * factorial(n-1)
    

# 🚀 Functions ko call kiya alag-alag values ke sath
print(factorial(3)) # Output: 6  (3 * 2 * 1)
print(factorial(4)) # Output: 24 (4 * 3 * 2 * 1)
print(factorial(5)) # Output: 120 (5 * 4 * 3 * 2 * 1)

# 🧠 REASON (Computer ke dimaag ka breakdown jo tumne sahi likha):
# 5 * factorial(4)            -> (factorial(5) ne call kiya)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1           -> (Base case touch hote hi 1 laut aaya)
# Final Jawab = 120


# =======================================================
# 🧬 FIBONACCI SEQUENCE (Agle codes ke liye formula)
# =======================================================
# Fibonacci ka niyam: Agla number hamesha pichle do numbers ka jod hota hai.
# Series dikhti hai aise: 0, 1, 1, 2, 3, 5, 8, 13, 21...

# f(0) = 0                  -> Pehla element hamesha 0 hoga
# f(1) = 1                  -> Doosra element hamesha 1 hoga
# f(2) = f(1) + f(0)        -> 💡 Note Correction: Teesra element pichle do ka jod hoga (1 + 0 = 1)
# f(n) = f(n-1) + f(n-2)    -> 👑 MASTER FORMULA: Kisi bhi n-th number ko nikalne ka rule

