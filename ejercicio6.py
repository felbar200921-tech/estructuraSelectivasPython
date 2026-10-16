promedio = float(input("Ingrese el promedio del alumno: "))
pension = float(input("Ingrese el valor de la pensión: "))
if promedio >= 4.0:
    descuento = pension*0.30
    total_pension = pension-descuento
    print(f"El alumno obtuvo un descuento del 30% el valor total de la pensión es: {total_pension}")
else: 
    iva = pension*0.10
    total_pension = pension+iva 
    print(f"El valor total de la pensión con el 10% del IVA es: {total_pension}")