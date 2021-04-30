year = int(input("\n\nHi\nWhich year do you want to check? : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Is a leap year")
        else :
            print("Is not a leap year")
    else: 
        print("Is leap year")
else:
    print("Is not leap year")
        

    