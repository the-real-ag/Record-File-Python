'''R-6-Write a menu driven program to perform following functions in a text file 'story txt'
a) Add a new line
b) No. of vowels & constonants
c) No. of lines
d) No. of digits
e) No. Of Occurence of spec. word by user
5) lines starting with spec char
g) Quit()'''

def addLine(f):
    file = open(f,"a")
    file.write(input("Enter new line: "))
    file.close()

def vCCount(f):
    file = open(f, "r")
    v=0
    c=0
    for x in file.read():
        if x.lower() in "aeiou":
            v+=1
        elif x.isalpha():
            c+=1
    file.close()
    print(f"Vowel count is {v} and consonant count is {c}")

def countLines(f):
    file = open(f,"r")
    print("The number of lines are:", len(file.readlines()))
    file.close()

def countDigits(f):
    file = open(f, "r")
    print("The Number of digits are:", sum(1 for x in file.read() if x.isdigit()))
    file.close()

def wordOccur(f, word):
    file = open(f, "r")
    print(f"The number of words '{word}' are ",sum(x.count(word) for x in file.readlines()))
    file.close()

def chrLine(f,chr):
    file = open(f, "r")
    print('\n'.join([x for x in file.readlines() if x.startswith(chr)]))
    file.close()


#__main__
print('''
          
1) Add a new line
2) No. of vowels & constonants
3) No. of lines
4) No. of digits
5) No. Of Occurence of spec. word by user
6) lines starting with spec char
7) Quit
''')
while True:
    c = input("Enter Choice: ")
    f = "story.txt"
    if c=="1":
        addLine(f)
    elif c=="2":
        vCCount(f)
    elif c=="3":
        countLines(f)
    elif c=="4":
        countDigits(f)
    elif c=="5":
        wordOccur(f,input("Enter the word to be searched: "))
    elif c=="6":
        chrLine(f, input("Enter Character: "))
    elif c=="7":
        break
    else:
        print("Wrong choice")
    print("\n")


    