name = "vibhu"
friend = "mohan"
anthorfriend = "ram"

# 1. Multi-line String: Triple quotes se hum badi kahaniyan likh sakte hain
apple = '''he said to ,
hi vibhu
hey i am vibhu
 " i am eating food.'''

# 2. String Concatenation: '+' se do strings ko jodna
print("hello," + name)

# 3. Indexing: Python mein ginti 0 se shuru hoti hai
# v=0, i=1, b=2, h=3, u=4
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# print(name[5]) # ⚠️ Galti: Kyuki 'u' aakhiri hai jo 4 par hai, 5th par kuch nahi hai (IndexError)

print("lets use a for loops\n")

# 4. Looping through String: 
# 'character' naam ka variable 'apple' ke har ek akshar (letter) ke paas jayega
for character in apple:
  print(character) # Har akshar nayi line mein print hoga
