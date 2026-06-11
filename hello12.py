# 1. For Loop vs While Loop (Dono 0 se 2 tak print karenge)
for i in range(3):
    print(i)

# While loop mein humein teen cheezein khud karni padti hain:
i = 0               # (i) Shuruat kahan se karni hai
while(i < 3):       # (ii) Shart kya hai (kab tak chalna hai)
    print(i)
    i = i + 1       # (iii) Badlav (Update) - Taaki loop aage badhe
print("Done with the loop")

# 2. <= ka khel: Ye 0 se 3 tak chalega (Total 4 baar)
i = 0
while(i <= 3):
    print(i)
    i = i + 1

# 3. Dynamic While Loop (User se baar-baar poochna):
# Ye loop tab tak chalta rahega jab tak user 38 se chota number dalega
i = int(input("Enter your number: "))
while(i <= 38):
     i = int(input("Enter your number: "))
     print(i)
# Jaise hi user 39 ya bada number dalega, loop ruk jayega.

# 4. Ulta Ginti (Reverse Counting):
count = 10
while(count > 0):
     print(count)
     count = count - 1 # Har baar ek ghatate (minus) raho
