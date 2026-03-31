def password():
    contra= input()
    numero= ("0" in contra or "1" in contra or "2" in contra or "3" in contra or "4" in contra or "5" in contra or "6" in contra or "7" in contra or "8" in contra or "9" in contra)
    if numero and len(contra)>=8:
        print("Contraseña valida")

    if numero and len(contra)<=8:
        print("Contraseña muy corta")
    if not numero and len(contra)>=8:
        print("Debe contener un numero")
    if not numero and len(contra)<8:
        print("Contraseña muy corta")
        print("Debe contener un numero")
