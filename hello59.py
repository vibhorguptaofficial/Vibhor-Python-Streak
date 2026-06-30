# --- MULTILEVEL INHERITANCE (DADA -> PAPA -> BETA) ---

# Sabse pehli main class banayi jiska naam animal rakha (Dada Class)
class animal:
    # Animal ka constructor jo naam aur species ko save karega
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Animal ki details print karne ka basic function
    def show_details(self):
        print(f"name: {self.name}")
        print(f"species: {self.species}")


# animal class ko copy (inherit) karke dog class banayi (Papa Class)
class dog(animal):
    # Dog ka constructor jo naam aur breed (bread) lega
    def __init__(self, name, bread):
        # Dada class (animal) ke constructor ko chalaya aur species ko automatic "dog" kiya
        animal.__init__(self, name, species="dog")
        self.bread = bread # Dog ki breed ko object me save kiya
        
    # Animal ke show_details function ko override kiya
    def show_details(self):
        animal.show_details(self) # Pehle dada class wala function chalaya taaki name aur species print ho sakein
        print(f"bread:  {self.bread}") # Phir apni khud ki breed print ki



# dog class ko copy (inherit) karke goldenretriever class banayi (Beta Class)
class goldenretriever(dog):
    # Goldenretriever ka constructor jo naam aur color lega
    def __init__(self, name, color):
        # Papa class (dog) ke constructor ko chalaya aur breed ko automatic "goldenretriever" set kiya
        dog.__init__(self, name, bread="goldenretriever")
        self.color = color # Apna khud ka color variable save kiya

    # Papa aur dada ke show_details function ko override kiya
    def show_details(self):
        dog.show_details(self) # Pehle papa class (dog) wala function chalaya (yeh piche dada wale ko bhi chalayega)
        print(f"color: {self.color}") # Phir aakhri me apna color print kiya


# Sabse niche wali child class (goldenretriever) ka ek object banaya 'o'
o = goldenretriever("tommy", "black")
# show_details call karte hi teeno classes ke print statements ek ke baad ek chalenge
o.show_details()

# Is multilevel class ke dimaag ka rasta (order) check karne ke liye mro() chalaya
print(goldenretriever.mro())
