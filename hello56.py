# Ek class banayi jiska naam vector rakha
class vector:
    # Constructor banaya jo vector ke teeno components (i, j, k) ko object me save karega
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k


    # Magic method __str__ banaya taaki jab koi object ko print() kare toh vector format me dikhe
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
        
    # Magic method __add__ banaya jo do vectors ke beech me '+' ka nishan lagane par automatic chalu hoga
    def __add__(self, x):
       
        # Dono vectors ke i ko i se, j ko j se, aur k ko k se jodkar ek naya vector object return kiya
        return vector(self.i + x.i, self.j + x.j, self.k + x.k)
    

v1 = vector(3, 5, 8) # Pehla vector object banaya v1
print(v1)            # __str__ chalu hoga aur screen par print karega: 3i + 5j + 8k

v2 = vector(9, 45, 4) # Doosra vector object banaya v2
print(v2)             # Screen par print karega: 9i + 45j + 4k

# '+' ka nishan lagate hi upar wala __add__ function chalu hoga aur dono ko jodkar naya vector dikhaega
print(v1 + v2)

# Yeh check karne ke liye print kiya ki judne ke baad jo naya answer aaya hai uska type kya hai
print(type(v1 + v2))
