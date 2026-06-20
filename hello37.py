# ==============================================================================
# PART 1: READING A FILE (File se Data Padhna)
# ==============================================================================

# 'r' mode ka matlab hai Read Mode. Yeh text file ko sirf padhne ke liye kholta hai.
f = open('hello36.py', 'r')

# 'rb' mode ka matlab hai Read Binary Mode. Yeh images, videos ya non-text files ke liye use hota hai.
f = open('hello36.py', 'rb')

# 'w' mode ka matlab hai Write Mode. Isse ek ekdam Nayi File ('hello39.py') ban jaati hai.
# NOTE: Agar pehle se is naam ki file hogi, toh uska puraana data delete (overwrite) ho jayega.
f = open('hello39.py', 'w')  

# f ko print karne par file ki details (naam, mode aur encoding) screen par dikhegi.
print(f)

# BUG FIX: read() karne ke liye hume file ko fir se 'r' (read) mode mein kholna padega.
f.close()                  # Pehle write mode wali file ko band kiya
f = open('hello39.py', 'r') # Ab use read mode mein khola taaki error na aaye

text = f.read()            # f.read() file ka saara text nikaal kar 'text' variable mein daal dega
print(text)                # Us text ko screen par print kiya

f.close()                  # Kaam khatam hone ke baad file ko hamesha close (band) karna zaroori hai


# ==============================================================================
# PART 2: WRITING A FILE (File mein Data Likhna)
# ==============================================================================

# 'w' (Write) mode: Yeh file ko kholta hai aur shuruwaat mein 'hello, word!' likh deta hai.
# Agar is file mein pehle se kuch likha hoga, toh wo saaf (clear) ho jayega.
f = open('hello38.py', 'w')
f.write('hello, word!')    # File ke andar text likha
f.close()                  # File ko band kiya aur data save ho gaya


# 'a' (Append) mode: Yeh sabse mazedaar hai! Yeh puraane data ko delete nahi karta.
# Yeh file ke aakhiri (end) mein jaakar naya text jodta (repeat) chala jata hai.
f = open('hello38.py', 'a')
f.write('\nhello, word!')  # '\n' lagane se naya 'hello, word!' nayi line se aage judega
f.close()                  # File ko securely close kiya
