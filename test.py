print(' Hypothenuse ')

print('______________________________________________')

while True:
    L1 = int(input('Value of L1:'))
    L2 = int(input('Value of L2:'))

    if L1 >= 0 and L2 >= 0:
        if L1 >= 0:
            if L1 == 0:
                print("L1 Zero")
            else:
                print("L1 Positive Number")

        if L2 >= 0:
            if L2 == 0:
                print("L2 Zero")
            else:
                print("L2 Positive Number")

        h = pow(L1, 2) + pow(L2, 2)
        print('Value of Hypot', h)

        print('____________________________________________')
    elif L1 < 0:
        print("L1 Negative Number, Please Recheck Input")
    elif L2 < 0:
        print("L2 Negative Number, Please Recheck Input")