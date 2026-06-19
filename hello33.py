# ==============================================================================
# BLOCK 1: Standard Module Import
# ==============================================================================
import math  # Pure 'math' module ko import kiya

result = math.sqrt(3)  # math.sqrt() function ka use karke 9 ka square root nikaala
print(result)          # Output: 3.0 (Python mein sqrt() hamesha float value deta hai)


# ==============================================================================
# BLOCK 2: Importing Specific Functions and Constants (From ... Import)
# ==============================================================================
from math import sqrt, pi  # Module se sirf 'sqrt' function aur 'pi' constant ko directly bahar nikaala

result = sqrt(9) * pi  # Ab bina 'math.' likhe direct use kiya (3.0 * 3.14159)
print(result)          # Output: 9.42477796076938


# ==============================================================================
# BLOCK 3: Importing with Local Alias for Functions (as)
# ==============================================================================
from math import pi, sqrt as s  # 'sqrt' function ka naam locally chota karke 's' rakh diya

result = s(9) * pi  # s(9) ka matlab math.sqrt(9) hi hai, time bachane ke liye chota kiya
print(result)       # Output: 9.42477796076938


# ==============================================================================
# BLOCK 4: Standard Module Level Alias (Industry Standard)
# ==============================================================================
import math as m  # Pure math module ko ek short-name (alias) 'm' de diya

result = m.sqrt(9) * m.pi  # Ab 'math.' ki jagah sirf 'm.' ka use karke functions chalaaye
print(result)              # Output: 9.42477796076938


# ==============================================================================
# BLOCK 5: Long Custom Module Alias (Alternative Way)
# ==============================================================================
import math as math_bulitin_python  # Module ka ek lamba custom naam (alias) rakha

result = math_bulitin_python.sqrt(9) * math_bulitin_python.pi  # Naye lambe naam se functions ko call kiya
print(result)  # Output: 9.42477796076938 (Code ekdam sahi chalega, koi error nahi)


# ==============================================================================
# BLOCK 6: Deep Module Inspection (dir, ldexp, nan)
# ==============================================================================
import math  # Module ko fir se standard tarike se import kiya

# dir(math) module ke andar chhupe saare available functions aur constants ki list dikhata hai
print(dir(math))  

# math.ldexp(x, i) ek mathematical function hai jo (x * 2^i) calculate karta hai
# type() se check kiya ki ye kis tarah ka object hai
print(math.ldexp, type(math.ldexp))  # Output: <built-in function ldexp> <class 'builtin_function_or_method'>

# math.nan ka matlab hota hai 'Not a Number' (invalid mathematical operations ke liye use hota hai)
print(math.nan)  # Output: nan
