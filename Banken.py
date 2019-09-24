pin = 1234

print("Hej, kära krister vänligen skriv ditt pinkod")

userPin = int(input("Skriv in din pinkod: "))
if pin != userPin:
    exit()

menu = 0
# insättning
# utttag
# avslutning
while menu != 3:
    if menu == 1:
        print("insättning..")
        print( "\v")
        a = float(input("sätt in ditt pengar"))
        print(a)
        
    elif menu == 2:
        print("insättning")
    elif menu == 3:
        print("fel eller avsluta")
        exit()
