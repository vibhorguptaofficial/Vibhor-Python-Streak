# --- BLOCK 1: ANIMAL AUR DOG CLASS (METHOD OVERRIDING) ---

# Ek main class banayi jiska naam animal rakha
class animal:
    # Constructor banaya jo name aur species lekar object me save karega
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Ek default function banaya jo batayega ki animal aawaz nikal raha hai
    def make_sound(self):
        print("sound made by the animal.")


# animal class ko inherit karke dog class banayi
class dog(animal):
    # Dog ka constructor jo naam aur breed (bread) lega
    def __init__(self, name, bread):
        # Parent class ke constructor ko manually chalaya aur species ko automatic "dog" set kar diya
        animal.__init__(self, name, species = "dog")
        self.bread = bread # Dog ki breed ko object me save kiya

    # Parent class ke make_sound function ko badal kar dog ke liye bark! kiya (Method Overriding)
    def make_sound(self):
       print("bark!")


d = dog("dog", "doggermam") # dog class ka ek object banaya 'd'
d.make_sound()              # Dog ka apna function chalega aur 'bark!' print karega

a = animal("dog", "dog")    # animal class ka ek normal object banaya 'a'
a.make_sound()              # Parent class ka default function chalega aur 'sound made by...' print karega


# --- BLOCK 2: ANIMAL AUR CAT CLASS (POLYMORPHISM) ---

# Wahi main class dobara banayi cat ke logic ko samajhne ke liye
class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal.")


# animal class ko inherit karke ab cat class banayi
class cat(animal):
    # Cat ka constructor jo naam aur milk (ya koi extra variable) lega
    def __init__(self, name, milk):
        # Parent class ke constructor ko chalaya aur species ko automatic "cat" set kar diya
        animal.__init__(self, name, species = "cat")
        self.milk = milk # Cat ke variable ko object me save kiya

    # Parent class ke function ko override karke cat ke liye meow! kiya
    def make_sound(self):
       print("meow!")


b = cat("cat", "catrmam") # cat class ka ek object banaya 'b'
b.make_sound()            # Cat ka apna function chalega aur 'meow!' print karega

c = animal("cat", "cat")  # animal class ka ek normal object banaya 'c'
c.make_sound()            # Parent class ka function chalega aur 'sound made by...' print karega
