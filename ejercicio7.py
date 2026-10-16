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
