# --- BLOCK 1: EMPLOYEE CLASS WITH DASH SEPARATOR ---

# Ek class banayi jiska naam Employee rakha
class Employee:
    # Standard constructor banaya jo naam aur salary lekar object banata hai
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    

    # Classmethod decorator lagaya jisse yeh function pehle input me puri class (cls) ko leta hai
    @classmethod
    def fromstr(cls, string):
        # String ko dash (-) se alag kiya, pehla part naam aur doosra part salary (integer me) lekar naya object return kiya
        return cls(string.split("-")[0], int(string.split("-")[1]))

# Normal tarike se pehla employee 'e1' banaya
e1 = Employee("vibhu", 12000)
print(e1.name)
print(e1.salary)


string = "chiku-120000"
# Alternative constructor ka use karke string se seedhe doosra employee 'e2' banaya
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)

string = "harry-120000"
# Phir se string ka use karke teesra employee 'e3' banaya
e3 = Employee.fromstr(string)
print(e3.name)
print(e3.salary)


# --- BLOCK 2: PERSON CLASS WITH COMMA SEPARATOR ---

# Ek nayi class banayi jiska naam person rakha
class person:
    # Constructor banaya jo naam aur umar lekar object banata hai
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Doosra classmethod banaya jo comma (,) wale string par kaam karega
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",") # String ko comma se tod kar do alag variables me save kiya
        return cls(name, int(age))    # Naya person object banakar wapas bhej diya
    

# String se seedhe naya object banaya aur use person naam ke variable me save kiya
person = person.from_string("vibhu, 19")
print(person.name, person.age)
