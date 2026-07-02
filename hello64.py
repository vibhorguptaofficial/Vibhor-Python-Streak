import shutil
shutil.copy("hello64.py", "hello65.py")
import shutil
shutil.copy2("hello64.py", "hello65.py")
import shutil
shutil.copytree("python", "mypython")
import shutil
shutil.move("python/hello65.py", "hello65.py")
import os
os.remove("hello65.py")