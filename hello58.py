# Ek class banayi jiska naam employee rakha
class employee:
    # Constructor banaya jo employee ka naam set karega
    def __init__(self, name):
        self.name = name
    # Ek function banaya jo employee ka naam dikhayega
    def show(self):
        print(f"the name is {self.name}")

# Ek doosri class banayi jiska naam dancer rakha
class dancer:
    # Constructor banaya jo dance ka type set karega
    def __init__(self, dance):
        self.dance = dance
    # Ek function banaya jo dance ka type dikhayega
    def show(self):
        print(f"the dance is {self.dance}")


# Multiple Inheritance: Ek nayi class banayi jo dancer aur employee dono ki khubiyan ek sath legi
class danceremployee(dancer, employee):
    # Constructor banaya jo dance aur name dono inputs lega
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name



o = danceremployee("kathak", "shivani") # danceremployee class ka ek object banaya 'o'
print(o.name)  # Object se name print kiya (shivani)
print(o.dance) # Object se dance print kiya (kathak)

# MRO Rule: Dono parent classes me 'show' naam ka function hai, par Python pehle dancer wale show ko chalayega
o.show()

# Is class ke dimaag ka order dekhne ke liye mro() chalaya, jo batayega ki Python pehle kahan galti ya function dhoondhta hai
print(danceremployee.mro())
