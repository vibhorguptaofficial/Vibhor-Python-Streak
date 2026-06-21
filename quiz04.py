a = input("Enter your choice ('code' and 'decode') :")
print("your choice is:", a)

i = input("enter your name")
print("your name is:", i)

import random
import string

if  a == "code":
   if(len(i) >= 3):
     b = (i[1:] + i[0])
     random_shuru = "".join(random.choices(string.ascii_lowercase, k=3))
     random_ant = "".join(random.choices(string.ascii_lowercase, k=3))
     secret_word = random_shuru + b + random_ant
     print("Aapka secret code hai:", secret_word)

   else:
     secret_word = (i[::-1])
     print("Aapka secret code hai:", secret_word)

if  a == "decode":
   if(len(i) >= 3):
     
     print(i)

   else:
     secret_word = (i[0:])
     print("Aapka secret code hai:", secret_word)