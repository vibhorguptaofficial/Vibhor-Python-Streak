class person:

    def  __init__(self, n, o):
        print("hey i am a person")
        self.name = n  
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")



a = person("chiku", "maneger")
b = person("vibhu", "HR")
# print(a.name)
# a.name = "vibhu"
# a.occ = "HR"
a.info()
b.info()
