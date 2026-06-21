# =======================================================
# 🗺️ 1. SEEK & TELL METHODS (Cursor ke sath khelna)
# =======================================================
with open('hello40.py', 'r') as f:
    # 🔬 type(f) se dikhayega ki yeh ek '_io.TextIOWrapper' class ka object hai
    print(type(f))
    
    # 🚀 seek(10): Computer ko strict order diya ki cursor ko direct 10th character (byte) par le jao!
    f.seek(10)

    # 📍 tell(): Yeh batata hai ki cursor abhi file mein kaunse number par baitha hai
    print(f.tell()) # Output: 10 (Kyunki humne seek se use 10 par sarakaya hai)
    
    # ✂️ f.read(5): 10th position se shuru karke sirf aage ke 5 characters hi padhega!
    data = f.read(5)
    print(data)


# =======================================================
# 🪓 2. TRUNCATE METHOD (File ka size chota karna)
# =======================================================
with open('hello42.py', 'w') as f:
    f.write('Hello World3!')
    
    # 👑 MASTERSTROKE: 'truncate(5)' ne computer ko order diya ki file mein sirf 
    # shuruat ke 5 bytes (characters) hi rakho, baaki ka saara maal permanent DELETE kar do!
    f.truncate(5)


# =======================================================
# 🔍 3. VERIFICATION (Check karna ki kya bacha)
# =======================================================
# 🚀 Jadoo check: hello42.py ko dubara kholne par sirf 'Hello' hi print hoga!
with open('hello42.py', 'r') as f:
    print(f.read()) # Output: Hello
