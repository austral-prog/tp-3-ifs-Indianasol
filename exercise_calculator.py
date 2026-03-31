def calculator():
    num1= float(input())
    num2= float(input())
    operacion= input()

    if operacion not in ["+", "-", "*" , "/"]:
        print ("Operacion invalida")
    elif (num2==0) and operacion == "/":
        print("Error: division por cero")
    elif operacion == "+":
        resultado = num1+num2
        print (f"Resultado: {resultado}")
    elif operacion == "-":
        resultado = num1-num2
        print (f"Resultado: {resultado}")
    elif operacion == "*":
        resultado = num1*num2
        print (f"Resultado: {resultado}")
    elif operacion == "/":
        resultado = num1/num2
        print (f"Resultado: {resultado}")
