'''R2-Write a menu driven program using functions to create a number-conversion program
1 Decimal to Binary
2) Decimal to Octal
3) Decimal to Hex
4) Binary to Decimal
5) Octal to Decimal
6) Hex to Decimal'''

def decToBOH(dec, b=False,o = False, h = False): #General Function for Decimal to Binary, Octal Or Hex
    dec = int(dec)
    base = 2 if b else 8 if o else 16 if h else 1 #Deciding the base value (1 is buffer value)
    val = ""
    while dec!=0:
        rem = dec%base
        if rem<10: # Condition applies for hex values
            val+=str(rem)
        else:
            val+=chr(ord("A")+ rem-10)
        dec//=base
    return val[::-1]
def BOHToDec(val, b = False, o = False, h = False): #General Function for Binary, Octal or Hex to Decimal
    base = 2 if b else 8 if o else 16 if h else 1 #Deciding Base value
    val = str(val)[::-1].upper()
    num = 0
    for i in range(len(val)):
        x = ord(val[i])-ord("A")+10 if val[i].isalpha() else int(val[i]) #Computing value to be added
        num+=x*(base**i)
    return num
# __main__
print('''1) Decimal to Binary
2) Decimal to Octal
3) Decimal to Hex
4) Binary to Decimal
5) Octal to Decimal
6) Hex to Decimal
7) End''')
while True:
    choice = input("Enter Choice(Number): ")
    if choice == "7":
        break
    elif choice not in "123456":
        print("Wrong choice")
        continue
    strVal = input("Enter Corresponding Starting Value: ")
    if choice=="1":
        print(decToBOH(strVal, b = True))
    elif choice == "2":
        print(decToBOH(strVal, o = True))
    elif choice == "3":
        print(decToBOH(strVal, h = True))
    elif choice == "4":
        print(BOHToDec(strVal, b = True))
    elif choice == "5":
        print(BOHToDec(strVal, o = True))
    elif choice == "6":
        print(BOHToDec(strVal, h = True))