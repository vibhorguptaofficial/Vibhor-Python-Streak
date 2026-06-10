# 1. User se number lena
x = int(input("enter ka value of x:"))

# 2. Match Case shuru: Ye x ki value ko niche ke cases se milayega
match x:

    # Agar x bilkul 0 hai
    case 0:
        print("x is zero")

    # Agar x bilkul 4 hai
    case 4:
        print("case is 4")

    # 3. Match Case with If (Guard Condition):
    # Iska matlab: "Agar upar wala kuch match nahi hua, TOH check karo ki kya x, 90 nahi hai?"
    case _ if x != 90:
        print(x, "is not 90")

    # 4. Ye tabhi chalega jab upar wale saare cases (0, 4, aur not 90) fail ho jayein
    case _ if x != 80:
        print(x, "is not 80")

    # 5. Default Case: Agar kuch bhi match nahi hua toh ye aakhiri rasta hai
    case _:
        print(x)
