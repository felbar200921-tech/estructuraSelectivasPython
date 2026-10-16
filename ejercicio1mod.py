# CONDICIONES UTILIZADAS:
# Comparaciones con >= sobre el promedio: 90 (sobresaliente), 80 (buena) y 70 (justo).
# El else cubre todo lo demás: promedio menor a 70, desaprobado.
# ¿POR QUÉ ESTE ORDEN?
# Python revisa de arriba hacia abajo y ejecuta solo la primera condición verdadera.
# Va de la más exigente (90) a la menos exigente (70); si empezara por 70,
# un promedio de 95 diría "aprobado con lo justo".
# Uso elif para que se muestre un solo mensaje y else para el resto de casos.
# ¿QUÉ PASA SI CAMBIA UNA NOTA?
# Cambia el promedio y con él el mensaje. Ejemplos:
# 80, 75, 70 -> promedio 75.0 -> "Has aprobado con lo justo"
# 80, 75, 100 -> promedio 85.0 -> "Has aprobado con una nota buena"
# 80, 75, 20 -> promedio 58.33 -> "Has desaprobado"
# También cambian la nota más alta y la más baja.
nombre = input("Ingrese el nombre del estudiante: ")
nota1 = int(input("Ingrese a continuación la primer nota: "))
nota2 = int(input("Ingrese a continuación la segunda nota: "))
nota3 = int(input("Ingrese a continuación la tercer nota: "))
promedio = round((nota1+nota2+nota3)/3,2)
print(f"Resultados del aprendiz {nombre}")
print(f"promedio: {promedio}")
print("La nota más alta es:", max(nota1, nota2, nota3))  
print("La nota más baja es:", min(nota1, nota2, nota3))
if promedio >= 90:
    print("Has aprobado con una nota sobresaliente")
elif promedio>=80:
    print("Has aprobado con una nota buena")
elif promedio>=70: 
    print("Has aprobado con lo justo")
else: 
    print("Has desaprobado")
