# 1. Complex Numbers: Maths wala logic, 8 real hai aur 9 imaginary
a = complex(8, 9)
print(a) # Output: (8+9j)

a1 = 19
b = "vibhu" # String data type
print(b)

# 2. Calculation: Complex number mein normal number jod rahe ho
print(a + a1) # Output: (27+9j) - Sirf real part (8+19) juda hai

# 3. Type Checking: 'type()' se pata chalta hai dabba kis tarah ka hai
print("the type of a is", type(a)) # <class 'complex'>
print("the type of b is", type(b)) # <class 'str'>

# 4. List: Ye "Changeable" (Mutable) dabba hai. 
# Tune list ke andar list rakhi hai (Nested List) - Pro coder move!
list1 = [8, 2.3, [-4, 5], ["apple", "bnanaa"]]
print(list1)

# 5. Tuple: Ye dabba ek baar band ho gaya toh badal nahi sakta (Immutable)
tuple1 = (("paarrot", "sparrow"), ("lion", "tiger"))
print(tuple1)

# 6. Dictionary: "Key-Value" pair wala dabba (Jaise asli dictionary hoti hai)
dict1 = {"Name": "sakshi", "age": 20, "canvote": True} 
print(dict1)
