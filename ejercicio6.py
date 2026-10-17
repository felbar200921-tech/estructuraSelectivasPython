#6.  Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: 
#si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, se le hará un descuento del 30% sobre la pensión; 
#si el promedio obtenido es menor que 4.0 deberá pagar la pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno. 
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
