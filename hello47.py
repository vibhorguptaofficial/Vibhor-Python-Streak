# Ek main class banayi jiska naam Employee rakha
class Employee:
    # Constructor function jo naya employee bante hi uska naam aur id set karega
    def __init__(self, name, id):
        self.name = name  # Employee ka naam class ke andar save kiya
        self.id = id      # Employee ki id class ke andar save kiya

    # Ek function banaya jo employee ki saari details screen par dikhayega
    def showdetails(self):
        print(f"The Details of Employee: The Employe's name is {self.name} and his id is {self.id}")

# Ek nayi class banayi programmer jo Employee class ki saari details ko inherit (copy) kar rahi hai
class programmer(Employee):
    # Programmer class ka apna khud ka naya function jo uski programming language batayega
    def showlanguage(self):
        print("the default language is python")

# Employee class ka ek object banaya e1 jisme 'rohan das' aur id 400 bheji
e1 = Employee("rohan das", 400)
# e1 ki details ko screen par print karne ke liye function call kiya
e1.showdetails()

# programmer class ka ek object banaya e2 jisme 'vibhu' aur id 4100 bheji
e2 = programmer("vibhu", 4100)
# e2 programmer class ka hai, fir bhi wo Employee class ka showdetails function use kar sakta hai (Inheritance)
e2.showdetails()
# e2 ke liye programmer class ka apna function showlanguage call kiya
e2.showlanguage()
