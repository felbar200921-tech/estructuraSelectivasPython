total_compra = int(input("Ingrese el total de la compra: "))
color = str(input("Ingrese el color: "))
match color:
    case "rojo":
        descuento = total_compra*0.15
        total_descuento = total_compra-descuento
        print(f"El total de la compra es: {total_compra} con el descuento del 15% por balota color rojo es: {total_descuento}")
    case "verde":
        descuento = total_compra*0.20
        total_descuento = total_compra-descuento
        print(f"El total de la compra es: {total_compra} con el descuento del 20% por balota color verde es: {total_descuento}")
    case _:
        print(f"No se obtuvo un descuento por color de balota diferente, asi que el valor total es: {total_compra}")
