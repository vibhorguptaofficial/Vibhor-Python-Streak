a = True
print(a:= False)

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0 :
    print(numbers.pop())



# walrus operater  :=
# new to python 3.8
# assignment expreesion aka walrus operator 
# assigns values to variables as part of a larger exprssions


happy = False
print(happy)

print (Happy := True)



foods = list()
while True:
    food = input("what do you food like?:")
    if food == "quit":
        break
    foods.append(food)

#ye uper vala aur niche vala ek hi hai niche vala shortcut hai 

foods = list()
while (food := input("what do you food like?:")) != "quit":
    foods.append(food)