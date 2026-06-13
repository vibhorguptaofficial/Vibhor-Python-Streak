l = [11, 45, 1, 2, 4, 6]
print(l)
# 1. append: List ke aakhir mein naya saaman (7) jodne ke liye
l.append(7)
print(l)

l = [11, 45, 1, 2, 4, 6]
print(l)
# 2. sort: List ko tarteeb (Ascending order) mein lagane ke liye (1, 2, 4...)
l.sort()
print(l)

l = [11, 45, 1, 2, 4, 6]
print(l)
# 3. sort(reverse=True): Bade se chote (Descending order) mein lagane ke liye
l.sort(reverse=True)
print(l)

l = [11, 45, 1, 2, 4, 6]
print(l)
# 4. reverse: Poori list ko bas ulta kar dena (bina kisi order ke)
l.reverse()
print(l)

l = [11, 45, 1, 2, 4, 6]
print(l)
# 5. index: Pata karna ki koi number (1) kis position par baitha hai
print(l.index(1)) 
print(l)

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# 6. count: Ginn-na ki koi number (1) list mein kitni baar aaya hai
print(l.count(1))
print(l)

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# 7. Reference Error: Yahan m = l karne se dono ek hi dabba ban gaye. 
# Agar m ko badloge toh l apne aap badal jayega! (Khatarnak hai ye)
m = l
m[0] = 0
print(l)

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# 8. copy(): Ye sahi tareeka hai. l ki ek alag photo (copy) banayi 'm' mein. 
# Ab m ko badalne se asli 'l' par koi asar nahi padega.
m = l.copy()
m[0] = 0
print(l)

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
m = [899, 900, 564]
# 9. extend: Poori ki poori ek nayi list 'm' ko 'l' ke aage jod dena
l.extend(m)
print(l)

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
m = [899, 900, 564]
# 10. Concatenation (+): Do lists ko jod kar ek teesri nayi list 'k' bana dena
k = l + m
print(k)

l = [11, 45, 1, 2, 4, 6]
print(l)
# 11. insert: Apni marzi ki position (index 1) par koi number (899) ghusana
l.insert(1, 899)
print(l)
