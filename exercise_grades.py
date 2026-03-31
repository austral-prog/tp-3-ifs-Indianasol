def grades():
    nota= int(input())
    if nota == 10 or nota==9:
        print("Excelente")
    elif nota==7 or nota==8:
        print("Bueno")
    elif nota ==6 or nota==5:
        print("Regular")
    elif nota<=4 and nota>=0:
        print("Insuficiente")
