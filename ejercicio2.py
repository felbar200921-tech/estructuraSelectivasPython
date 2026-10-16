cantidad = int(input("Ingrese la cantidad de zapatillas que va a comprar: "))
Zapatillas = 100000
total = cantidad*Zapatillas
if cantidad >= 3:
    descuento = total*0.20
    total_descuento = total-descuento
    print(f"El valor de las zapatillas es:{total}")
    print(f"El valor de las zapatillas con descuento del 20% es:{total_descuento}")
else:
    descuento = total*0.10
    total_descuento = total-descuento
    print(f"El valor de las zapatillas es:{total}")
    print(f"El valor de las zapatillas con descuento del 10% es:{total_descuento}")