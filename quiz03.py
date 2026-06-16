questions = [
    [
        "bharat ki rajdhani kya hai ?",
        " lucknow",  " dehli",  " munbai",  " chandigard", "none",  2
    ],
    [
        "bharat main rajay kitne  hai ?",
        " 29",  " 27",  " 28",  " 7", "none",  2
    ],
    [
        "kho-kho team main kitne player hote hai ?",
        " 11 ",  " 9 ",  " 7 ",  " 10 ", "none",  2
    ],
    [
        "bharat ki rajdhani kya hai ?",
        " lucknow",  " dehli",  " munbai",  " chandigard", "none",  2
    ],
    [
        "bharat main rajay kitne  hai ?",
        " 29",  " 27",  " 28",  " 7", "none",  2
    ],
    [
        "kho-kho team main kitne player hote hai ?",
        " 11 ",  " 9 ",  " 7 ",  " 10 ", "none",  2
    ],
    [
        "bharat ki rajdhani kya hai ?",
        " lucknow",  " dehli",  " munbai",  " chandigard", "none",  2
    ],
    [
        "bharat main rajay kitne  hai ?",
        " 29",  " 27",  " 28",  " 7", "none",  2
    ],
    [
        "kho-kho team main kitne player hote hai ?",
        " 11 ",  " 9 ",  " 7 ",  " 10 ", "none",  2
    ],
    [
        "bharat ki rajdhani kya hai ?",
        " lucknow",  " dehli",  " munbai",  " chandigard", "none",  2
    ],
    
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nquestion for rs. {levels[i]}")
    print(f"  {question[0]}")

    print(f"a. {question[1]}                b. {question[2]}")
    print(f"c. {question[3]}                d. {question[4]}")

    reply = int(input("Enter your answer (1-4) or 0 to quit:\n "))
    if (reply == 0):
       money = levels[i-1]
       break
    if (reply == question[-1]):
       print(f"correct answer, you have won rs. {levels[i]}")
       if(i == 4):
         money = 10000
       elif(i == 9):
         money = 320000
       elif(i == 14):
         money = 10000000
    else:
       print("wrong answer!")
       break

print(f"your take home money is {money}")