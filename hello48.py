# --- BLOCK 1: PUBLIC ACCESS MODIFIER ---

# Ek basic class banayi Employee naam ki
class Employee:
    # Constructor banaya jo automatic chalu hoga
    def  __init__(self):
        self.name = "vibhu" # Yeh ek public variable hai jise bahar se padha ja sakta hai

a = Employee() # Employee class ka ek object banaya 'a'
print(a.name)  # Public hone ke karan iska naam direct print ho jayega


# --- BLOCK 2: PRIVATE ACCESS MODIFIER (ENCAPSULATION) ---

# Wahi class dobara banayi private variables ko samajhne ke liye
class Employee:
    # Constructor banaya
    def  __init__(self):
        self.__name = "vibhu" # Do underscore (__) lagane se yeh variable ab private ho gaya hai

a = Employee() # Naya object banaya 'a'
# print(a.__name) can not be accessed directly -> Private hone ke karan yeh line error degi

# Name Mangling ka use karke private variable ko ghumakar (indirectly) padha ja raha hai
print(a._Employee__name) 

# Object ke andar mojud saare methods aur hidden variables ki list dekhne ke liye print kiya
print(a.__dir__())


# --- BLOCK 3: PROTECTED ACCESS MODIFIER ---

# Ek nayi class banayi student naam ki
class student:
    # Constructor banaya
    def __init__(self):
        self._name = "vibhu" # Ek underscore (_) lagane se yeh protected variable ban gaya hai
    
    # Ek protected function banaya jo sirf is class ya iski child class me use hona chahiye
    def _funname(self):  #procected method
        return "vibhuwithcode"
    

# student class ko copy (inherit) karke ek nayi class banayi subject naam ki
class subject(student):  #inherited class
    pass # Pass ka matlab abhi iske andar alag se kuch nahi likhna hai

obj = student() # Parent class (student) ka object banaya 'obj'
obj1 = subject() # Child class (subject) ka object banaya 'obj1'

# student object ke andar ke saare functions aur variables ki list print ki
print(dir(obj))
# subject object ke andar ke saare functions aur variables ki list print ki
print(dir(obj1))

 #calling by object of student class 
  
print(obj._name) # Protected variable ko parent class ke object se direct print kiya
print(obj._funname()) # Protected function ko parent class ke object se call kiya

 #calling by object of student class 

print(obj1._name) # Protected variable ko child class ke object se bhi print kiya ja sakta hai
print(obj1._funname()) # Protected function ko child class ke object se bhi call kiya ja sakta hai
