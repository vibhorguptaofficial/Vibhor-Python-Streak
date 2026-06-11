#1. String par Loop: 'i' ek-ek karke 'abhishek' ke har akshar (letter) ke paas jayega
name = 'abhishek'
for i in name:
    print(i)
    if(i =="b"): # Agar akshar 'b' hai, toh extra message print karo
        print("this is something spical")

# 2. Nested Loop (Loop ke andar Loop):
colors = ["red", "yellow", "green", "pink"]
for color in colors:
    print(color)      # Pehle poora rang ka naam print hoga
    for i in color:   # Phir us rang ke ek-ek akshar (letter) print honge
        print(i)

# 3. Range Function ka khel:
# range(5) ka matlab: 0 se shuru karo aur 5 se pehle (yaani 4 tak) jao
for k in range(5):
    print(k) # Output: 0, 1, 2, 3, 4

# range(5) ke saath +1 karke 1 se 5 tak ginti print karna
for k in range(5):
    print(k+1) # Output: 1, 2, 3, 4, 5

# range(start, stop): 1 se shuru aur 10 se pehle (yaani 9 tak)
for k in range(1, 10):
    print(k)

# Python ki power: 1 se 20,000 tak ki ginti chutkiyo mein!
for k in range(1, 20001):
    print(k)

# Negative Range: -5 se shuru aur -1 se pehle (yaani -2 tak)
for k in range(-5, -1):
    print(k)

# 4. Range with Step: range(start, stop, step)
# 1 se shuru karo, 12 tak jao, par har baar 3-3 ka kood (jump) maro
for k in range(1, 12, 3):
    print(k) # Output: 1, 4, 7, 10
