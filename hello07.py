# 1. Slicing ka basic: [shuruat : khatam]
names = "vibhu,vishesh"
print(names[0:6]) # 0 se shuru karke 5th index se pehle tak (vibhu)

# 2. len() function: String ki poori lambai (length) nikalne ke liye
print(len(names)) # Sab kuch ginega (letters + comma)

names = "vibhu"
len1 = len(names)
print("vibhu is a", len1, "letter word.") # Output: 5

# 3. Slicing ke alag-alag tareeke:
print(names[0:4]) # 0 se 3 tak (vibh)
print(names[:4])  # Agar shuruat na likho, toh Python apne aap 0 se shuru karta hai
print(names[1:4]) # 1 se 3 tak (ibh)
print(names[:])   # Poori string print kar dega (vibhu)

# 4. Negative Indexing (Sabse important logic):
# Python ise 'len(names) - index' mein badal deta hai
print(names[0:-3]) # 0 se (5-3=2) tak -> Output: vi

# names[0:len(names)-4] -> names[0:5-4] -> names[0:1]
print(names[0:len(names)-4]) # Output: v

# names[-1:len(names)-4] -> names[4:1] -> Ye kuch print nahi karega 
# Kyunki hum piche se aage nahi ja sakte slicing mein bina step ke
print(names[-1:len(names)-4]) 

# names[-3:-1] -> names[2:4] (5-3=2 aur 5-1=4)
print(names[-3:-1]) # Output: bh

nm = "vibhu"
# nm[-4:-2] -> nm[1:3] (5-4=1 aur 5-2=3)
print(nm[-4:-2]) # Output: ib
