class libray:
    books =  ["english", "hindi", "math", "sst", "science", "history"]
    no_of_books = len(books)
    print(len(books))
    def __init__(self, book):
        self.book = book
        libray.books.append(book)
        libray.no_of_books += 1
    def showdetails(self):
        print(f"the total no of books = {libray.no_of_books}")
        
          

        print(f"All Books Name Are Here!")
        for index, b in enumerate(libray.books, start=1):
          print(f" {index}.{b}")



lib1 = libray("physics")
lib1.showdetails()
lib2 = libray("chemistry")
lib2.showdetails()
lib3 = libray("physical")
lib3.showdetails()
lib4 = libray("coomerce")
lib4.showdetails()




# class libray:
#     def __init__(self):
#         self.nobook = 0
#         self.books = []
#     def addbooks(self, book):
#         self.books.append(book)
#         self.nobooks = len(self.books)

#     def showinfo(self):
#         print(f"the libary has {self.nobooks} books. the books are")
#         for book in self.books:
#             print(book)

# l1 = libray()
# l1.addbooks("vibhu hindi")
# l1.addbooks("vibhu hindi2")
# l1.addbooks("vibhu hindi3")
# l1.showinfo()
