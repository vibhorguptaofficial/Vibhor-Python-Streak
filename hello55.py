# Ek main class banayi jiska naam shape rakha
class shape:
    # Constructor banaya jo do inputs (x aur y) lekar object me save karega
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Ek function banaya jo x aur y ko guna karke area (kshetrafal) nikalega
    def area(self):
        return self.x * self.y
    
# shape class ko inherit (copy) karke ek nayi circle class banayi
class circle(shape):
    # Circle ka constructor jo sirf ek input (radius/trijya) lega
    def __init__(self, radius):
        self.radius = radius
        # super() ka use karke parent class ko x aur y dono ki jagah radius bhej diya (taaki radius * radius ho sake)
        super().__init__(radius, radius)

    # Parent class ke area function ko override kiya taaki circle ka formula (3.14 * r * r) lag sake
    def area(self):
        # super().area() ka matlab hai parent class ka area function chalega jo radius * radius (x * y) karke dega
        return 3.14 * super().area()


rec = shape(3, 5) # shape class ka ek object banaya 'rec' jisme x=3 aur y=5 bheja
print(rec.area()) # area function chala jisme 3 * 5 gune hokar 15 print hoga

c = circle(5)     # circle class ka ek object banaya 'c' jisme radius=5 bheja
print(c.area())   # Circle ka area function chala jisme 3.14 * 5 * 5 hokar 78.5 print hoga
