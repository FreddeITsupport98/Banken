pin = 1234

print("Hej, kära krister vänligen skriv ditt pinkod")

userPin = int(input("Skriv in din pinkod: "))
if pin != userPin:
    exit()


try: 
    with open("balance.txt", "r")as balanceFile:
        try:
            balance = balanceFile.readline()
            balance = float(balance)
        except (ValueError):
            print("filen är corrupt")
            balance = 0.0
except (FileNotFoundError):
    balance = 0.0 


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
        print("\v")
        balance = balance + float(input("sätt in dina pengar: "))
        
    elif menu == 2:
        print("utaggning...")
        print("\v")
        if balance <= 0:
            print("Du kan inte ta ut dina pengar")
        
        elif balance >= 0:
            

        else:
            balance = balance - float(input("ta ut dina pengar: "))


    elif menu == 3:
        print("Avsluta")
        exit()
    else:
        print("Fel")

    #while True:
     #       file = open("balance.txt", "r+")
     #       test = "ajshdjlkasjdöadö"
      #      file.write(test)
       #     file.close()
        #    i = i + 1
         #   passwd = "ajshdjlkasjdöadö"
          #  test = crypt.crypt(passwd)
           # print(test)