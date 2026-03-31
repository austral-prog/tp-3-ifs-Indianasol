def discount():
    precio_unitario= float(input())
    cant_unidades= int(input())

    if cant_unidades >= 10:
        subtotal= precio_unitario*cant_unidades
        descuento= subtotal*0.2
        total= subtotal-descuento
        print(f"Subtotal: {subtotal}")
        print(f"Descuento aplicado: 20%")
        print(f"Monto de descuento: {descuento}")
        print(f"Total final: {total}")
    elif cant_unidades <=9 and cant_unidades>=5:
        subtotal= precio_unitario*cant_unidades
        descuento= subtotal*0.1
        total= subtotal-descuento
        print(f"Subtotal: {subtotal}")
        print(f"Descuento aplicado: 10%")
        print(f"Monto de descuento: {descuento}")
        print(f"Total final: {total}")
    else:
        subtotal= precio_unitario*cant_unidades
        descuento= subtotal*0
        total= subtotal-descuento
        print(f"Subtotal: {subtotal}")
        print(f"Descuento aplicado: 0%")
        print(f"Monto de descuento: {descuento}")
        print(f"Total final: {total}")
