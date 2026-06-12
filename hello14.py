# 1. Bina Function ke: Dekho mehnat zyada lag rahi hai, formula baar-baar likhna pad raha hai
a = 9
b = 3
gmean1 = (a*b)/(a+b)
print(gmean1)

c = 4
d = 8
gmean2 = (c*d)/(c+d)
print(gmean2)

# 2. Function ke saath (Smart Work):
# 'def' ka matlab hai hum computer ko ek naya kaam sikha rahe hain
def calculategmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a, b):
    if(a>b):
     print("first number is greater")
    else:
     print("second number is greater or equal")

# 3. 'pass' ka jadoo:
# Iska matlab hai "Bhai abhi iska code baad mein likhunga, abhi error mat dena"
def islesser(a, b):
   pass

# 4. Functions ko "Call" karna: 
# Ab humne sirf naam liya aur kaam apne aap ho gaya
a = 9
b = 3
isGreater(a, b)
calculategmean(a, b)

c = 4
d = 8
isGreater(c, d)
calculategmean(c, d)
