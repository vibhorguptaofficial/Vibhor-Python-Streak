# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if(hour>=5 and hour<12):
  print("Good Morning sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon sir!")
elif(hour>=17 and hour<21):
  print("Good Evening sir!")
else:
  print("Good Nigth sir!")

  # 1. User se input lena aur use Number (int) mein badalna (ye maine likha uper harry sir vala likha hai )
# Yaad rakhna: input() hamesha text deta hai, isliye int() lagana zaroori hai
# Time = int(input("Enter Your Time: "))

# # 2. Condition 1: Agar time 5 se 11 ke beech hai
# if(Time >= 5 and Time < 12):
#   print("Good Morning Sir")

# # 3. Condition 2: Agar time 12 se 16 ke beech hai
# elif(Time >= 12 and Time < 17):
#   print("Good Afternoon Sir")

# # 4. Condition 3: Agar time 17 se 20 ke beech hai
# elif(Time >= 17 and Time < 21):
#   print("Good Evening Sir")
  
# # 5. Default Case: Agar upar ki koi condition sahi nahi hui 
# # (Matlab raat ke 9 baje se subah 4 baje tak ka time)
# else:
#   print("Good Nigth Sir")
