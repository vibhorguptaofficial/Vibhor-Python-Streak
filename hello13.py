# 1. Break Statement: Loop ko beech mein hi todne ke liye
for i in range(12):
    if(i == 10):
       break # "Bas bhai, bohot ho gaya!" - i=10 hote hi loop poora khatam
    print("5  X", i+1, "=", 5 * (i+1))

# 2. Continue Statement: Sirf ek chakkar (iteration) ko chhodne ke liye
for i in range(12):
    if(i == 10):
       print("skip the iteration")
       continue # Is chakkar ko chhodo aur agle (i=11) par bhago
    print("5  X", i+1, "=", 5 * (i+1))

# 3. Table Logic with Continue:
for i in range(12):
    if(i == 10):
       print("skip the iteration")
       continue
    print("5  X", i, "=", 5 * i)

# 4. While True (Do-While ka jugad):
# Ye loop hamesha chalta rahega jab tak andar 'break' na mil jaye
i = 0
while True:
    print(i)
    i = i + 1
    if(i%50 == 0): # Jaise hi 100 se divide hone wala number aayega
     break          # Loop turant ruk jayega
