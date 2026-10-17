#7. En una llantera se ha establecido una promoción de las llantas marca “Todo Terreno”, dicha promoción consiste en lo siguiente: 
#Si se compran menos de cinco llantas el precio es de $300.000 cada una, de $250.000 si se compran de cinco a 10 y de $200.000 si se compran más de 10. 
#Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compre. 
cantidad_llantas = int(input("Ingrese la cantidad de llantas: "))
if cantidad_llantas < 5:
    valor_llantas = 300000
elif cantidad_llantas <= 10:
    valor_llantas = 250000
else:
    valor_llanta = 200000
valor_total = cantidad_llantas*valor_llantas
print(f"El precio por llanta es: {valor_llantas}")
print(f"El valor total para pagar es: {valor_total}")
