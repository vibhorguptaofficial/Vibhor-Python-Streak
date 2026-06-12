# 1. Default Arguments: 
# Agar hum koi value na dein, toh Python apne aap a=9 aur b=1 utha lega.
def average(a=9, b=1):
    print("the average is", (a+b)/2)

average()      # Output: 5.0 (9 aur 1 ka average)
average(5)     # a=5 ho gaya, b abhi bhi default 1 hai -> 3.0
average(b=9)   # a abhi bhi 9 hai, b ko humne 9 kar diya -> 9.0

# 2. Keyword Arguments:
# Yahan 'fname' zaroori hai (Required), baaki default hain.
def name(fname, mname = "jhon", lname = "vibhu"):
    print("hello", fname, mname, lname)

name("chiku") # Sirf fname diya, baaki apne aap aa gaye
name("chiku", "agawal", "gupta") # Humne saare naam badal diye

# 3. *args (Arbitrary Arguments): 
# Jab humein na pata ho ki kitne numbers aayenge. Ye 'numbers' ko ek TUPLE bana deta hai.
def average(*numbers):
     sum = 0
     for i in numbers:
          sum = sum + i
     print("the average is", sum/len(numbers))

average(5, 6, 7, 8) # Jitne marzi number dalo, sabka average nikal dega!

# 4. **kwargs (Keyword Arbitrary Arguments):
# Ye data ko ek DICTIONARY bana deta hai.
def name(**name):
    print("hello", name["fname"], name["mname"], name["lname"])

name(mname = "jhon", lname = "vibhu", fname = "gupta")

# 5. Return Statement (Sabse Kaam ki Cheez):
# Ye function se answer bahar fenkta hai taaki hum usey aage kisi 'c' variable mein save kar sakein.
def average(*numbers):
    sum = 0
    for i in numbers:
           sum = sum + i
    return sum / len(numbers) # Answer wapas bhejo

c = average(5, 6) # c mein answer save ho gaya
print(c)
