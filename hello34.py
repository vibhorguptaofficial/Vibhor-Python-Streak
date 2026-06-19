# ==============================================================================
# ENTRY POINT CONCEPT (Main Gate of Python Script)
# ==============================================================================

# def keyword se humne 'welcome' naam ka ek custom function banaya
def welcome():
    # Jab ye function call hoga, toh ye message screen par dikhega
    print("her you are welcomefrom vibhu")


# __name__ Python ka ek hidden variable hai jo batata hai ki file kaise chal rahi hai.
# Agar file ko DIRECT chalayein, toh iski value hamesha "__main__" hoti hai.
print(__name__) 


# Yeh line ek check-post hai. Yeh poochti hai: "Kya ye file direct chalayi gayi hai?"
# Agar hum ise direct run karenge, toh ye condition TRUE (sach) ho jayegi.
if __name__ == "__main__":
    # Condition True hote hi main gate khulega aur welcome() function chal jayega
    welcome()
