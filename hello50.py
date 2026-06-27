# Ek class banayi jiska naam Employee rakha
class Employee:
    Companyname = "Apple" # Yeh ek class variable hai jo saare employees ke liye same rahega
    noofemployee = 0      # Yeh bhi class variable hai jo employees ki kul ginti rakhega
    
    # Constructor banaya jo naya employee bante hi uska naam aur default settings karega
    def __init__(self, name):
        self.name = name          # Instance variable: Har employee ka apna alag naam hoga
        self.raise_amount = 0.2   # Instance variable: Har employee ka apna alag raise amount hoga
        Employee.noofemployee +=1 # Naya employee bante hi class ke noofemployee variable me 1 jod diya
        
    # Ek function banaya jo employee ki saari details print karega
    def showdetails(self):
        print(f"the name of tha Employee is {self.name} and the raise amount in {self.noofemployee} sized {self.Companyname} is {self.raise_amount}")

        
# Employee.showdetails(emp1) emp1.ya empn.showdetails() ki jagah ye bhi likh skte h dono hai ek hi
# -> Upar aapne jo comment me likha hai wo bilkul sahi hai, dono ka matlab ek hi hota hai

emp1 = Employee("Harry") # Pehla employee banaya 'Harry' (noofemployee ab 1 ho gaya)
emp1.raise_amount = 0.3  # Sirf emp1 ka raise amount badal kar 0.3 kiya
emp1.Companyname = "apple india" # Sirf emp1 ke liye company ka naam apple india kiya (instance variable ban gaya)
emp1.showdetails()       # emp1 ki details print ki

Employee.Companyname = "Google" # Poori class ke liye main Companyname ko badal kar Google kar diya
print(Employee.Companyname)     # Screen par Google print hoga

emp2 = Employee("vibhu") # Doosra employee banaya 'vibhu' (noofemployee badhkar 2 ho gaya)
emp2.Companyname = "tata" # Sirf emp2 ke liye company ka naam badal kar tata kiya
emp2.showdetails()       # emp2 ki details print ki (Yahan noofemployee 2 dikhayega)
