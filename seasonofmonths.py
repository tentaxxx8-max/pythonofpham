def seasonnumber():
    while True:
        try:
            months = int(input("input your months 1-12: "))
        except ValueError:
            pass
        if months == 0:
            break
        if months < -1:
            print("please input invalid numbers")
        elif months > 12:
            print("please input months from 1 to 12")
        else:
            monthseason(months)

def monthseason(months):
    match months:
        case 1: print ("the season of january is spring")
        case 2: print ("the season of febuary is spring ")
        case 3: print ("the season of march is spring")
        case 4: print ("the season of april is fall")
        case 5: print ("the season of may is fall")
        case 6: print ("the season of june is fall")
        case 7: print ("the season of july is autumn")
        case 8: print ("the season of august is autumn")
        case 9: print ("the season of september is autumn")
        case 10: print ("the season of october is winter")
        case 11: print ("the season of november is winter")
        case 12: print ("the season of december is winter")