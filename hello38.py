# =======================================================
# 1. READLINE BASIC LOOP (Line by line padhne ka dappa)
# =======================================================
f = open('hello37.py', 'r')
while True:
    line = f.readline() # 📜 File se ek baar mein sirf ek single line uthayega
    if not line:        # 🛑 Base Case: Agar file khatam ho gayi aur line khali mili, toh loop tod do
        break
    print(line)

# =======================================================
# 2. EMPTY LINE TEST (Khali line ka postmortem)
# =======================================================
f = open('hello37.py', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        # 🔬 VIP Observation: File ke ekdum end mein pahunchte hi loop break hone se pehle
        # yeh print dikhayega ki khali line ka type ekdam blank String ('') hi hota hai!
        print(line, type(line)) # Output:  <class 'str'>
        break

# =======================================================
# 3. DATA PARSING WITH SPLIT (Marksheet processing logic) 👑
# =======================================================
f = open('hello39.py', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    
    # ✂️ Jadoo combo: '.split(",")' line ko jahan-jahan comma hai wahan se tod kar ek list bana dega.
    # [0], [1], [2] se humne teeno subjects ke marks alag kiye aur unhe 'int()' mein badla!
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    
    # 🧮 f-strings ke andar tumne marks ko double (*2) karke print kiya hai
    print(f"Marks of student {i} in maths is: {m1*2}")
    print(f"Marks of student {i} in hindi is: {m2*2}")
    print(f"Marks of student {i} in english is: {m3*2}")
    print(line) 

# =======================================================
# 4. WRITELINES METHOD (Bulk mein data likhna)
# =======================================================
f = open('hello41.py', 'w')
lines = ['line1\n', 'line2\n', 'line3\n'] # 💡 Hack: '\n' lagane se teeno lines ek ke neeche ek aayengi
f.writelines(lines) # Pure list ka maal ek saath naye file mein chipka dega

# 🛠️ VIP Correction: Brackets '()' lagana compulsory hai taaki file memory se saaf ho sake
f.close() 
