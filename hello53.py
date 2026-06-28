class parentclass:
    def parent_method(self):
        print("this is the parent method1.")

class childclass(parentclass):
    
    def parent_method(self):
        print("vibhu2")
        super().parent_method()
    def child_method(self):
        print("this is a child method2.")
        super().parent_method()

# --- BLOCK 1: METHOD OVERRIDING AUR SUPER() METHOD KE SATH ---

# Ek main class banayi jiska naam parentclass rakha
class parentclass:
    # Parent class ka apna ek function banaya
    def parent_method(self):
        print("this is the parent method1.")

# parentclass ko copy (inherit) karke ek childclass banayi
class childclass(parentclass):
    
    # Parent class ke hi naam ka function child me dobara banaya (Method Overriding)
    def parent_method(self):
        print("vibhu2") # Pehle child class ka apna message print hoga
        super().parent_method() # super() ki madad se parent class ka asli function bhi chalaya
        
    # Child class ka apna ek alag function banaya
    def child_method(self):
        print("this is a child method2.") # Child ka message print hua
        super().parent_method() # Yahan se bhi parent class ke function ko direct call kiya


child_object = childclass() # childclass ka ek object banaya 'child_object'
child_object.child_method() # Child method ko call kiya (Isme parent method bhi chalega)
child_object.parent_method() # Badle huyen parent method ko call kiya


# --- BLOCK 2: CONSTRUCTOR ME SUPER() KA USE ---

# Ek main class banayi jiska naam employee rakha
class employee:
    # Employee ka constructor jo naam aur id set karega
    def __init__(self, name, id):
        self.name = name
        self.id = id

# employee class ko inherit karke programmer class banayi
class programmer(employee):
    # Programmer ka apna constructor jo naam, id ke sath language (lang) bhi lega
    def __init__(self, name, id, lang):
        # super() ka use karke parent class ke constructor ko naam aur id de di taaki wo khud set ho jayein
        super().__init__(name, id)
        self.lang = lang # Naye variable lang ko alag se save kiya
     

# employee class ka ek normal object banaya rohan naam se
rohan = employee("rohan das", "420")
# programmer class ka object banaya vibhu naam se jisme teeno details bheji
vibhu = programmer("vibhu", "2345", "python")

# super() ki wajah se vibhu object me name aur id bina dobara code likhe set ho gaye hain
print(vibhu.name)
print(vibhu.id)
print(vibhu.lang)

child_object = childclass()
child_object.child_method()
child_object.parent_method()



class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class programmer(employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
     

rohan = employee("rohan das", "420")
vibhu = programmer("vibhu", "2345", "python")
print(vibhu.name)
print(vibhu.id)
print(vibhu.lang)