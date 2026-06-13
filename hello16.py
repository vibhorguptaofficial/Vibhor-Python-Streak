l = [4, 5, 6]
print(l)
print(type(l)) # <class 'list'> batayega

marks = [4, 5, 6]
print(marks)
print(type(marks))
# Indexing: Python mein ginti 0 se shuru hoti hai
print(marks[0]) # Pehla element
print(marks[1]) # Dusra element
print(marks[2]) # Teesra element

# List ki power: Ek hi dabbe mein Number, String aur Boolean sab aa sakte hain
marks = [4, 5, 6, "vibhu", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

marks = [4, 5, 6, "vibhu", True]
# Negative Indexing ka logic: marks[len(marks) - index]
print(marks[-3])            # Piche se teesra
print(marks[len(marks) -3]) # Wahi baat: 5 - 3 = 2 index wala element
print(marks[5-3])           # index 2
print(marks[2])             # seedha index 2 (6 print hoga)
print(marks[2+1])           # index 3 ("vibhu" print hoga)

# Membership Operator: Check karna ki koi cheez andar hai ya nahi
if 7 in marks:
    print("yes")
else:
    print("no")


marks = [4, 5, 6, "vibhu", True] 
print(marks)
print(marks[1:9])    # Slicing: 1 se 8 tak (jitne milenge utne print honge)
print(marks[1:9:3])  # Jump: 1 se shuru karke har teesra element uthao

# --- List Comprehension (Shortcuts se list banana) ---

lst = [i for i in range(4)] # Seedhi ginti: [0, 1, 2, 3]
print(lst)


lst = [i*i for i in range(4)] # Squares nikalna: [0, 1, 4, 9]
print(lst)


# Condition ke saath: Sirf Even numbers (2 se divide hone wale) ka square
lst = [i*i for i in range(10) if i%2==0]
print(lst)

# Sirf unka square jo 3 se divide hote hain
lst = [i*i for i in range(10) if i%3==0]
print(lst)

# Har number ka square (kyunki har number 1 se divide hota hai)
lst = [i*i for i in range(10) if i%1==0]
print(lst)

# Sirf unka square jo 5 se divide hote hain (0 aur 5)
lst = [i*i for i in range(10) if i%5==0]
print(lst)
