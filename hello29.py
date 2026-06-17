# =======================================================
# 1. BASIC TRY-EXCEPT-FINALLY (Simple dimaag)
# =======================================================
try:
    l = [1, 4, 6, 9]
    i = int(input("enter the index: "))
    print(l[i])
except:
    print("some error occurred")
finally:
    # 🟢 Yeh hamesha chalega, chahe error aaye ya code ekdum perfect chale!
    print("i am always executed") 


# =======================================================
# 2. FINALLY VS NORMAL PRINT (Bina function ke farq)
# =======================================================
try:
    l = [1, 4, 6, 9]
    i = int(input("enter the index: "))
    print(l[i])
except:
    print("some error occurred")

# 🤔 Yahan par bina finally ke bhi yeh normal print chal jata hai, 
# isiliye bache confuse hote hain ki 'finally' ka fayda kya hai.
print("i am always executed") 


# =======================================================
# 3. THE REAL MAGIC: Function aur Return ka kanta 👑
# =======================================================
def func1():
    try:
        l = [1, 4, 6, 9]
        i = int(input("enter the index: "))
        print(l[i])
        return 1  # 🛑 Magic: Function yahi khatam hokar baahar nikalne wala hai!
    except:
        print("some error occurred")
        return 0  # 🛑 Error aane par bhi yahan se return ho jayega
    finally:
        # 👑 BRAHMASTRA: Python ka rule hai—chahe function 'return' ho chuka ho, 
        # memory se baahar nikalne se pehle computer 'finally' wale dabbe ko 
        # 100% execute karega hi karega! Normal print yahan fail ho jata.
        print("i am always executed") 

# Function ko call kiya aur uska return value 'x' mein safe kiya
x = func1()
print(x)  # Output mein pehle 'finally' print hoga, phir 'x' ki value (1 ya 0)
