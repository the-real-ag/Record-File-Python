'''
R1- Write a menu driven program to perform following operations on a string based on user's choice:
a) Upper Case
b) Lower Case
c) Title Case
d) Sentence Case
e) No. of words
f) No. of digits
g) No. of vowels: 
  1) Lower Case
  2) Upper Case
h) Quit
'''

# Source Code
str = input("Enter the string: ")
print('''
a) Upper Case
b) Lower Case
c) Title Case
d) Sentence Case
e) No. of words
f) No. of digits
g) No. of vowels: 
h) Quit''')
while True:
    choice = input("\nEnter the letter of choice: ").upper() #Accepting the letter of the choice
    if choice=="A":
        print(str.upper())
    elif choice=="B":
        print(str.lower())
    elif choice=="C":
        print(str.title())
    elif choice=="D":
        print(str.capitalize())
    elif choice=="E":
        print(len(str.split(" "))) #Creating a list having separate words and finding the length of the list
    elif choice=="F":
        print(sum(1 for x in str if x.isdigit())) #Creating an iterable with 1's for each digit and adding to get the result
    elif choice=="G":
        print("Which type of vowels?\n\n1)Uppercase vowels\n2)Lowercase Vowels")
        cVowel = input("Enter option number: ") #Accepting the option number of choice
        if cVowel == "1":
            print(sum(1 for x in str if x in "AEIOU")) #Similar to digits, creating iterable of 1's and adding
        elif cVowel == "2":
            print(sum(1 for x in str if x in "aeiou")) #Similar to above choice
        else:
            print("Wrong choice.")
    elif choice=="H":
        break
    else:
        print("Wrong option") #Eror handling