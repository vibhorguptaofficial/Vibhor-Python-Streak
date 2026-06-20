# =======================================================
# 1. LOCAL VS GLOBAL SCOPE (Andar aur baahar ka dhanda)
# =======================================================
x = 4 # 🌐 GLOBAL VARIABLE: Yeh pure parivaar (pure page) ka sadasya hai

print(x) # Output: 4

def hello():
    x = 5 # 🏠 LOCAL VARIABLE: Yeh variable sirf is hello() function ke andar hi zinda hai!
    print(f"the local x is {x}") # Output: 5
    print("hello harry")

# Baahar se print karoge toh hamesha Global wala '4' hi dikhega
print(f"the global x is {x}") # Output: 4

hello() # Function call hua toh uske andar ka local '5' print hoga

x = 5 # 🌐 Global variable ki value ko baahar se hi permanent badal kar 5 kar diya
print(f"the global x is {x}") # Output: 5


# =======================================================
# 2. THE 'GLOBAL' KEYWORD (Andar se baahar dakaiti)
# =======================================================
z = 10 # 🌐 Global variable baitha hai bahar

def my_function():
    # 👑 MASTERSTROKE: 'global' keyword ne computer ko strict order diya ki 
    # "Bhai, andar naya variable mat banao, balki baahar baithe asli 'z' ko hi andar khinch lo!"
    global z
    
    z = 8 # 💥 Is line ne baahar baithe asli global 'z' ki value ko permanent 8 kar diya!
    y = 5 # 🏠 Yeh bechara local hi rahega
    print(y)

my_function() # Function chala, 'y' (5) print hua aur z badal gaya

# 🚀 Jadoo check: Ab baahar se 'z' ko print karne par 10 nahi, balki 8 milega!
print(z) # Output: 8
