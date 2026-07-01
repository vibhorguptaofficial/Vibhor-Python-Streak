# --- BLOCK 1: HYBRID INHERITANCE (MIXED STRUCTURE) ---
# Isme do ya do se zyada tarah ke inheritance ek sath mix hote hain

# Sabse pehli main class banayi jiska naam baseclass rakha (Main Parent)
class baseclass:
    pass

# baseclass ko copy karke pehli child class derived1 banayi (Single Inheritance)
class derived1(baseclass):
    pass

# baseclass ko hi copy karke doosri child class derived2 banayi (Hierarchical Inheritance)
class derived2(baseclass):
    pass 

# derived1 aur derived2 dono ko ek sath jodkar derived3 class banayi (Multiple Inheritance)
class derived3(derived1, derived2):
    pass


# --- BLOCK 2: HIERARCHICAL INHERITANCE (ONE PARENT, MANY CHILDREN) ---
# Isme ek hi main class se alag-alag azaad classes nikalti hain

# Phir se ek main class banayi jiska naam baseclass rakha
class baseclass:
    pass

# baseclass se pehli class d1 nikali
class d1(baseclass):
    pass

# baseclass se hi doosri alag class d2 nikali (Dono ka parent ek hi hai)
class d2(baseclass):
    pass

# d1 class ko inherit karke ek aur neeche wali class d3 banayi (Multilevel ka part joda)
class d3(d1):
    pass
