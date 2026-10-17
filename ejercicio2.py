#2. Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas se aplica un descuento del 20% 
#sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%. 
#Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar una vez aplicado el descuento. 
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
