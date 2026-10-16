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