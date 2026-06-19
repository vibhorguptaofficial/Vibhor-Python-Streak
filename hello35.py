import os

# =======================================================
# 📂 1. AUTOMATED FOLDER CREATION (Folder banane ka jadoo)
# =======================================================
# Check kar raha hai ki kya 'data' naam ka dabba pehle se hai? Agar nahi hai toh banayega
if (not os.path.exists("data")):
    os.mkdir("data")


# 🔄 Loop chala kar automatic 99 folders banaye 'data' ke andar
for i in range(1,100):
    # 📐 Note: 'i+1' ki wajah se ginti day2 se shuru hokar day100 tak jayegi!
    if not os.path.exists(f"data/day{i+1}"):
       os.mkdir(f"data/day{i+1}")

   



# =======================================================
# 📝 2. AUTOMATED BULK RENAME (Naam badalna ek jhatke mein)
# =======================================================
# Pure 99 folders ka naam 'day' se badal kar 'tutorial' kar diya

for i in range(1,100):
    if os.path.exists(f"data/day{i+1}") and not os.path.exists(f"data/tutorial{i+1}"):
        os.rename(f"data/day{i+1}", f"data/tutorial{i+1}" )

# =======================================================
# 🗺️ 3. DIRECTORY OPERATIONS (Rasta dekhna aur badalna)
# =======================================================
# os.listdir(): 'data' ke andar jitne bhi folders hain, unki ek list banakar 'folders' variable mein daal di
folders = os.listdir("data")

# os.getcwd(): Current Working Directory (Yaani computer abhi kis folder mein baith kar kaam kar raha hai)
print(os.getcwd())

# os.chdir(): 🚀 Computer ka rasta badal kar direct 'users' folder ke andar ghusa diya!
# 🚨 Windows user ho toh 'C:/Users' ya sahi local path dena compulsory hai warna error aayega!
#os.chdir("/users")
#print(os.getcwd()) # Naya rasta print karega


# =======================================================
# 🔍 4. DEEP SEARCH LOOP (Folder ke andar ka maal dekhna)
# =======================================================
# Loop chala kar ek-ek folder ka naam print karega aur uske andar rakhi hui files ki list dikhayega
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}")) # Har tutorial folder ke andar ka saaman print hoga
