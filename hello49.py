# Ek class banayi jiska naam math rakha
class math:
    # Constructor banaya jo object bante hi num variable ko set karega
    def __init__(self, num):
        self.num = num # Object ke andar num naam ka variable save kiya
    
    # Ek normal function banaya jo purane num me ek naya number jod dega
    def addtonum(self, n):
        self.num = self.num + n # Purane num ko naye number se badal diya


    # Staticmethod decorator ka use kiya taaki is function me 'self' na lagana pade
    @staticmethod
    def add(a, b):
        return a + b # Yeh function bina object ke data ke do alag numbers ko jodta hai


a = math(5)  # math class ka ek object banaya 'a' aur usme num=5 bheja
print(a.num) # Screen par 'a' ke num ki shuruat ki value (5) print ki

a.addtonum(6) # addtonum function ko call kiya aur usme 6 bheja (5 + 6 = 11)
print(a.num)  # Screen par num ki nayi badli hui value (11) print ki
