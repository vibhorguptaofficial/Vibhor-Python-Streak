# 🛠️ Ek function banaya jo number ka square nikalega
def square(n):
    '''Take in a number n, returns the square n '''
    # 📝 VIP RULE: Yeh line normal comment nahi hai! Kyunki yeh function ke ekdum 
    # shuruat mein triple quotes (''' ''') mein likhi hai, isiliye Python ise 'Docstring' maanta hai.
    
    print(n**2) # Number ki power 2 (Square) print karega

# 🚀 Function ko call kiya aur 5 pass kiya
square(5) # Output: 25

# 👑 JADOO LINE: '__doc__' ka use karke hum function ke andar likhi hui 
# us definition/documentation ko screen par print karwa sakte hain!
print(square.__doc__) 
# Output: Take in a number n, returns the square n 
