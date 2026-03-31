def weekday():
    dia= str(input())
    dia= dia.lower()
    if not (dia== "domingo" or dia=="sabado"):
        print("Dia habil")
    else:
        print("Fin de semana")
