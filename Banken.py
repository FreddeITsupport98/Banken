pin = 1234 # enkel fördefinerad pinkod

print("Hej, kära krister vänligen skriv ditt pinkod") #programmen välkommer krister

userPin = int(input("Skriv in din pinkod: ")) # krister ska skriva in sin hemliga pinkod villket det är: 1234
if pin != userPin: #villkor som gär om pin är inte lika med userPin ska programmen stänga ner sig
    exit()


try:  # på börjar kollar om balance.txt existerar
    with open("balance.txt", "r+") as balanceFile: # öppnar balance.tct med variabel balanceFile
        try: # försök lässa linjen
            balance = balanceFile.readline()
            balance = float(balance) #convertarar till float värde utav balance
        except (ValueError): #visar värde fel
            print("filen är corrupt") # skriver ut värde fel
            balance = 0.0 # resetar till balance = 0.0
except: (FileNotFoundError) #Om filen inte hittas ska det
balance = 0.0 
menu = 0 # tillderalr menu att vara värde 0
# insättning
# utttag
# avslutning
while menu != 3: # medans menu är inte lika med 3
    print("Ditt saldo är: ", balance)
    menu = int(input("Skriv ditt val[1 insättning, 2 utaggning, 3 avsluta]: ")) #ger val till 3 olika menu
    
    if menu == 1: #it satas för menu 1 
        print("insättning..") # start text
        print("\v") # lägger till en blank rad
        balance = balance + float(input("sätt in dina pengar: ")) #ger input för float värde
        
    elif menu == 2:
        print("utaggning...")
        print("\v")
        if balance <= 0: #om värde mindre lika med 0 ska du få  medelande om pengar räcker inte till. Negativa  tal ska ge samma felmedellande och att krister ska inte ta ut pengerna
            print("Du kan inte ta ut dina pengar")
        
        elif balance >= 0:
            balance = balance - float(input("ta ut dina pengar: ")) # om du har pengar att ta ut så ska du kunna ta ut mer vad du har


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