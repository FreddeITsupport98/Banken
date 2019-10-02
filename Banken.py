import pickle
import os 


pin = 1234

print("Hej, kära krister vänligen skriv ditt pinkod")

userPin = int(input("Skriv in din pinkod: "))
if pin != userPin:
    exit()

menu = 0
balance = 0.0
# insättning
# utttag
# avslutning
while menu != 3:
    print("Ditt saldo är: ", balance)
    menu = int(input("Skriv ditt val[1 insättning, 2 utaggning, 3 avsluta]: "))
    if menu == 1:
        print("insättning..")
        print( "\v")
        balance = balance + float(input("sätt in dina pengar: "))

    elif menu == 2:
        print("utaggning")
        print( "\v")
        if balance > input(float(-1)):
            print("Invalid saldo")
            
        else:
            balance = balance - float(input("sätt in dina pengar: "))
        
        
    elif menu == 3:
        print("Avsluta")
        exit()
    else:
        print("Fel")
