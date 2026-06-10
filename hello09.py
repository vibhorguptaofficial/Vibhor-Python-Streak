# 1. User se input aur Typecasting (Text ko Number banana)
a = int(input("enter your age"))
print("your age is:", a)

# Conditional Operators: Ye sach (True) ya jhoot (False) batate hain
# < (chota), > (bada), <= (chota ya barabar), >= (bada ya barabar), == (barabar), != (barabar nahi)

if(a > 18):
    print("you can drive") # Agar age 18 se upar hai toh ye chalega
    print("yes")
else:
    print("you can no drive") # Agar age 18 ya usse kam hai toh ye
    print("no")

# 2. Budget wala Logic:
a = int(input("enter your budget"))
appleprice = 210

if(a >= appleprice):
    print("alexa,add 1 kg apples to the cart.") # Budget sahi hai toh shopping shuru
else:
    print("alexa,do not add apples to the cart.")

# 3. Elif (Else-If) ka logic:
# Yaad rakhna: Elif tabhi check hota hai jab upar wala 'if' galat (False) ho jaye
appleprice = 10
budget = 200

if(budget - appleprice > 50): 
    print("alexa,add 1 kg apples to the cart.") # Pehle ye check hoga
elif(budget - appleprice > 70):
    print("it is okay you can buy") # Ye sirf tab chalega agar upar wali line galat ho (Jo yahan nahi hoga)
else:
    print("alexa,do not add apples to the cart.")

# 4. Number Checker (Positive/Negative/Zero):
number = int(input("enter your value of number:"))
if(number < 0):
     print("value of negative")
elif(number == 0):
     print("value of zero")
else:
     print("value of positive")

# 5. Nested If-Else: Ek dabba ke andar dusra dabba
num = 30
if(num < 0):
    print("number of negative")
elif(num > 0):
  # Agar number positive hai, toh ab andar check karo ki kitna bada hai
  if(num <= 10):
    print("number is between 1-10")
  elif(num > 10 and num <= 20):
    print("number is between 11-20")
  else:
    print("number is greater than 20") # 30 yahan aayega
else:
    print("number of zero")
