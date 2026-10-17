#5. Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico; 
#la fórmula que se aplica es:  cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10  
#y si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 
sexo = str(input("Ingrese a continuación su sexo (M/F): "))
edad = int(input("Ingrese a continuación su edad: "))
if sexo=="M" or sexo=="m":
    num_pulsaciones = (210-edad)/10
    print(f"El número de pulsaciones es: {num_pulsaciones}")
elif sexo=="F" or sexo=="f":
    num_pulsaciones = (220-edad)/10
    print(f"El número de pulsaciones es: {num_pulsaciones}")
else: 
    print("Ingreso un carácter inválido.")
