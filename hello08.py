# Strings are immutable: Iska matlab hai ki ek baar string ban gayi toh badal nahi sakti. 
# Saare methods ek nayi string bana kar dete hain.

a = "vibhu"
print(len(a)) # 1. len(): Bata raha hai ki "vibhu" mein 5 letters hain.
print(a.upper()) # 2. upper(): Saare letters ko CAPITAL (VIBHU) kar dega.

a = "VIBHU"
print(a.lower()) # 3. lower(): Sabko small letters mein badal dega.

a = "!!!vibhu !!!!!!!!!!! vibhu"
print(a.upper()) # Sab Capital
print(a.lower()) # Sab Small
print(a.rstrip("!")) # 4. rstrip(): Sirf RIGHT side wale "!" ko saaf karega.
print(a.replace("vibhu" , "chiku")) # 5. replace(): "vibhu" ki jagah "chiku" likh dega.
print(a.split(" ")) # 6. split(): Jahan-jahan space hai, wahan se tukde karke ek list bana dega.

blogheading = "introduntion tO jS "
print(blogheading.capitalize()) # 7. capitalize(): Sirf pehla letter bada karega, baaki sab small.

str1 = "welcome to comsule1!!!"
print(len(str1))
print(len(str1.center(50))) # 8. center(): Text ko 50 characters ke beech mein le aayega.

print(a.count("VIBHU")) # 9. count(): Gin raha hai ki "VIBHU" kitni baar aaya (zero kyunki small/capital ka farak hota hai).

str1 = "welcome to my console!!!!"
print(str1.endswith("!!!!!")) # 10. endswith(): Check kar raha hai ki kya ye "!!!!!" par khatam ho raha hai? (False)
print(str1.endswith("!!!!")) # (True)
print(str1.endswith("to", 4, 10)) # Slice karke check kar raha hai ki 4 se 10 ke beech "to" hai ya nahi.

str1 = "he's name is dam. he is an honest man."
print(str1.find("is")) # 11. find(): "is" pehli baar kaunsi position par aaya wo batayega.
print(str1.find("ishh")) # Agar nahi mila toh '-1' dega (error nahi dega).

# str1.index("ishh") # 12. index(): Find jaisa hai, par agar word na mile toh ye PROGRAM CRASH kar deta hai (Error).

str1 = "WelcomeToTheConsule"
print(str1.isalnum()) # 13. isalnum(): Kya sirf A-Z aur 0-9 hain? (True)

str1 = "welcome"
print(str1.isalpha()) # 14. isalpha(): Kya sirf A-Z hain? (True)

str1 = "welcome00"
print(str1.isalpha()) # (False kyunki 00 numbers hain)

str1 = "hello world"
print(str1.islower()) # 15. islower(): Check karega sab small mein hain ya nahi.

str1 = "hello worlD"
print(str1.islower()) # (False kyunki 'D' capital hai)

str1 = "we wish you a very merry chrismas"
print(str1.isprintable()) # 16. isprintable(): Kya ye print ho sakta hai? (True)

str1 = "we wish you a very merry chrismas\n"
print(str1.isprintable()) # (False kyunki \n (new line) dikhta nahi hai)

str1 = "         " # usingspacebar
print(str1.isspace()) # 17. isspace(): Kya sirf khali jagah (White space) hai? (True)

str2 = "    " # usingtab
print(str2.isspace()) # (True)

str1 = "World Health Organigation"
print(str1.istitle()) # 18. istitle(): Kya har word ka pehla letter bada hai? (True)

str2 = "To Kill a Mocking bird"
print(str2.istitle()) # (False kyunki 'bird' ka 'b' small hai)

str1 = "Python is a Interpreted Launguage"
print(str1.startswith("python")) # 19. startswith(): Kya "python" (small p) se shuru ho raha hai? (False)

str1 = "Python is a Interpreted Launguage"
print(str1.swapcase()) # 20. swapcase(): Bade ko chhota aur chhote ko bada kar dega.

str1 = "his name is dam. he is an honest man."
print(str1.title()) # 21. title(): Har word ka pehla letter capital kar dega.
