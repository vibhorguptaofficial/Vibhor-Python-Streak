# # x = [1, 2, 3]
# # print(dir(x))
# # print(x.__add__)
# -> Upar ki yeh teeno lines comment hain, jo dikhati hain ki kisi list ke saare hidden methods kaise check karte hain

# Ek class banayi jiska naam person rakha
class person:
    # Constructor banaya jo object bante hi naam aur umar set karega
    def __init__(self, name, age):
        self.name = name          # Object ka name variable save kiya
        self.age = age            # Object ka age variable save kiya
        self.version = 1          # Ek default version variable set kiya jiski value 1 hai


p = person("vibhu", 30) # person class ka ek object banaya 'p' aur usme data bheja

# Object ke saare variables aur unki values ko ek dictionary ke format me dekhne ke liye print kiya
print(p.__dict__)

# Is person class ka poora kacha-chitha aur documentation (help guide) dekhne ke liye help function chalaya
print(help(person))
