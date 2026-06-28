# --- BLOCK 1: CLASS WITH DEFAULT VARIABLE AND LEN DUNDER METHOD ---

# Ek class banayi jiska naam Employee rakha
class Employee:
    name = "harry" # Class variable jisme default naam harry set hai
    
    # Python ka magic method __len__ banaya jo object par len() chalne par automatic chalu hoga
    def __len__(self):
        i = 0
        # self.name ke ek-ek akshar ko ginne ke liye loop chalaya
        for c in self.name:
            i = i + 1
        return i # Aksharon ki kul ginti ko wapas bhej diya
    
e = Employee()    # Employee class ka ek object banaya 'e'
print(e.name)     # Screen par default naam harry print hoga
print(len(e))     # len(e) likhte hi upar wala __len__ function chalu hoga aur 5 print karega


# --- BLOCK 2: CLASS WITH CONSTRUCTOR AND LEN DUNDER METHOD ---

# Wahi class dobara banayi parameterized constructor ke sath
class Employee:
    # Constructor banaya jo naya object bante waqt naam lega
    def __init__ (self, name):
        self.name = name

    # Dobara __len__ magic method banaya aksharon ko ginne ke liye
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
e = Employee("vibhu") # Naya object banaya 'e' aur is baar naam vibhu bheja
print(e.name)         # Screen par vibhu print hoga
print(len(e))         # Is baar __len__ function vibhu ke aksharon ko ginega aur 5 print karega


# --- BLOCK 3: STANDALONE MAGIC METHODS (OUTSIDE CLASS) ---

# Yeh functions abhi class ke bahar likhe hain, class ke andar hone par yeh alag kaam karte hain:

# __str__ method ka use tab hota hai jab koi object ko direct print() kare (User ko accha message dikhane ke liye)
def  __str__(self):
    return f"the name of the employee is {self.name} str"

# __repr__ method ka use developers ke liye hota hai taaki wo object ka asli roop ya debugging details dekh sakein
def __repr__(self):
    return f"employee ('{self.name}')"

# __call__ method ka use tab hota hai jab hum object ke naam ke aage bracket laga kar use function ki tarah chalayein, jaise e()
def __call__(self):
    print("hey i am good")
