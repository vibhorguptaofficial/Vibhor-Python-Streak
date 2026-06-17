# =======================================================
# 1. GENERAL EXCEPTION HANDLING (Saare errors ka ek ilaj)
# =======================================================
a = input("Enter the number:")
print(f"Multiplication table of {a} is:")

try:
    # 📐 Agar user 'vibhu' daal dega, toh int(a) karte hi code tootne lagega
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    # 👑 SHATIR OBSERVATION: Tumne bilkul sahi bola! 'as e' tabhi likhte hain jab 
    # hamein computer wala asli error message print karwana ho (jaise: print(e)).
    # Agar apna custom message dena hai, toh direct neeche wali lines kafi hain!
    print("sorry some reeor occurred")
    print("invalid input")

# 🚀 Try-except ka sabse bada fayda: Error aane par bhi neeche ka code bina ruke chalta rahega!
print("Some lines of code")
print("end of program")


# =======================================================
# 2. SPECIFIC ERROR HANDLING (Value Error ka dappa)
# =======================================================
try:
    num = int(input("enter an integer: "))
except ValueError:
    # 🛑 Agar user ne number ki jagah text daal diya, toh sirf YEH wala block chalega
    print("number entered is not an integer")


# =======================================================
# 3. MULTIPLE EXCEPT BLOCKS (Ek teer se do shikaar)
# =======================================================
try:
    num = int(input("enter an integer: "))
    a = [6, 3] # List mein sirf do elements hain (Index 0 aur Index 1)
    print(a[num]) # 🚨 Agar user ne '5' daal diya, toh Index Error aayega!
except ValueError:
    # ❌ Agar user text input karega toh yeh chalega
    print("number entered is not an integer")
except IndexError:
    # ❌ Agar user aisa index daalega jo list mein hai hi nahi, toh yeh chalega!
    print("IndexError")
