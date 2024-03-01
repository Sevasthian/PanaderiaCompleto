# """ menu = {
#     "productos salados": list({
#         "panes": [
#             {"nombre": "pan de sal", "valor": 2500},
#             {"nombre": "pan de nuez", "valor": 2900},
#             {"nombre": "pan de baguette", "valor": 2600},
#             {"nombre": "pan de redil", "valor": 2500},
#             {"nombre": "pan de 7 granos", "valor": 2300},
#             {"nombre": "pan de trigo", "valor": 2200},
#             {"nombre": "pan de uvas", "valor": 2100},
#             {"nombre": "pan de germen de trigo", "valor": 2800},
#             {"nombre": "pan de avena", "valor": 2000}
#         ]
#     }),
#     "menu dulce":list({
#         "panesdulces": [
#             {"nombre": "Pandebono", "valor": 3000},
#             {"nombre": "Conchas", "valor": 2900},
#             {"nombre": "Mantecadas", "valor": 3200},
#             {"nombre": "Rosquillas", "valor": 2500},
#             {"nombre": "Bollitos de leche", "valor": 3300},
#             {"nombre": "pan muerto", "valor": 3500},
#             {"nombre": "Marquesote", "valor": 3800},
#             {"nombre": "Garibaldi", "valor": 3600},
#             {"nombre": "Barritas de chocolate", "valor": 3700},
#             {"nombre": "cuernitos", "valor": 2500}
#         ]
#     }),
#     "pasteleria": {
#         "pasteles": [
#             {"nombre": "Cheesecake", "valor": 5000},
#             {"nombre": "Tiramisú", "valor": 5200},
#             {"nombre": "Tres Leches", "valor": 6000},
#             {"nombre": "Tarta de Santiago", "valor": 7000},
#             {"nombre": "Ópera", "valor": 8000}
#         ],
#         "promocionescategoria": [
#             {"indice": 0, "descuento por compras superiores a 3": 0.02}
#         ]
#     }
# }

# print("seleccione la categoria")
# listacategoria = menu.keys()
# listacategoria = list(listacategoria)
# for i,val in enumerate(listacategoria):
#     print(f"{i}.{val}")
# opcioncategoria = int(input())
# datoscategoria = menu.get(listacategoria[opcioncategoria])
# productoscategoria = datoscategoria["menu"]

# print(f"seleccione el producto de la categoria deseada {listacategoria[opcioncategoria]}")
# for i, val in  enumerate(productoscategoria):
#     print(f"{i}. {val}")
# opcionproducto = int(input())
# datoscategoria = menu.get(listacategoria[opcioncategoria])
# promocionesproducto = datoscategoria.get("promociones")

# promocionproductos = list()
# for val in promocionesproducto: 
#     if(val.get("indice") == opcionproducto):
#         promocionproductos.append(val)

# if(len(promocionproductos) == 0):
  
    
#     producto = datoscategoria.get('Producto')[opcionproducto]
#     nombreProducto = producto.get("nombre")
#     productovalor = producto.get("valor")
#     cantidad = int(input(f"Usuario cuantos{producto}desea: "))
#     valorAPagar = cantidad * productovalor
#     print(f"Usuario Su producto {nombreProducto} tiene un valos de ${productovalor} la cantidad solicitada es de {cantidad} que da un total a pagar de ${valorAPagar}")
#     dinero = int(input("Ingrese la cantidad de dinero disponible"))
#     if(dinero >= valorAPagar):
#         vueltos = dinero - valorAPagar
#         print(f"Usuario sus vueltos son {vueltos}, gracias por comprar nuestro producto")
#     else:
#         print(f"Usuario el monto es menor a valor total, porfavor busque plata")

# else:
    
#    print(f"promociones del producto son {datoscategoria.get('producto')[opcionproducto]}")

#    for i, val in enumerate(promocionproductos):
#        print(f"{i}. {val}")

#    print(f"{len(promocionproductos)}. Salir")   
#    opcionPromocion = int(input())
#    if(opcionPromocion != 2):
#        valorPromocion = promocionproductos[opcionPromocion].get("nombre")
#        nombrePromocion = promocionproductos[opcionPromocion].get("descuento")
#        unidadesPromocion = promocionproductos[opcionPromocion].get("unidades")
#        valorProducto = promocionproductos[opcionPromocion].get("unidades")
#         """

























PanesDulces = {
    'Panettone': 2500,
    'Brioche': 9000,
    'Challah': 21000,
    'Concha': 800,
    'Roscón': 4400,
    'Pan de muerto': 2300,
    'Pan de higo': 2230,
    'Pan de frutas': 5400,
    'Cinnamon roll': 1500,
    'Pan de naranja': 2280
    }

PanesSalados = {
    'Baguette': 1350,
    'Ciabatta': 1450,
    'Focaccia': 2180,
    'Pan de centeno': 3280,
    'Pan de ajo': 5320,
    'Pretzel': 3200,
    'Pan de cebolla': 3400,
    'Pan de queso': 2250,
    'Pan de aceitunas': 1380,
    'Pan de maíz': 1150
}

Postres = {
    'Tiramisú': 6200,
    'Cheesecake': 4350,
    'Crème brûlée': 7400,
    'Profiteroles': 1850,
    'Mousse de chocolate': 5200,
    'Flan': 5380,
    'Tarta de frutas': 6150,
    'Pastel de zanahoria': 1750,
    'Brownie': 3320,
    'Macarons': 1680
}

print("""Tipos de Panes disponibles: 
      1. PanesDulces 
      2. PanesSalados 
      3. Postres""")
Pan = int(input("Seleccione el tipo de pan: "))

if Pan == 1:
    Pan = "PanesDulces"
elif Pan == 2:
    Pan = "PanesSalados"
else:
    Pan = "Postres"

if Pan in ["PanesDulces", "PanesSalados", "Postres"]:
    print(f"Productos de la categoría {Pan}:")
    if Pan == "PanesDulces":
        productos = PanesDulces
    elif Pan == "Postres":
        productos = PanesSalados
    else:
        productos = Postres

    for i, (val, dinero) in enumerate(productos.items()):
        print(f"{i + 1}. {val} = ${dinero}")

    productoElegido = int(input("Seleccione un producto: "))

    if productoElegido in [1, 10, 0, 3]:
        productoElegido = list(productos.keys())[productoElegido - 1]
        promocion = input(f"El producto {productoElegido} tiene promoción de 2x1, ¿Desea aprovecharla? Contesta con un SI o NO: ").lower()


        if promocion =="SI":
            precioInicial = productos[productoElegido]
            print(f"Producto elegido: 2 x {productoElegido}")
            print(f"Precio final: ${precioInicial}")
            dinero = int(input("Ingrese la cantidad de dinero que va a pagar: $"))

            if dinero <precioInicial:
                print("Lo sentimos, no tienes suficiente dinero")
            else:
                print(f"Su cambio es de ${dinero - precioInicial}")
        else:
            precioInicial = productos[productoElegido]
            print(f"Producto elegido: {productoElegido}")
            print(f"Precio original: ${precioInicial}")
            dinero = int(input("Ingrese la cantidad de dinero que va a pagar: $"))

            if dinero < precioInicial:
                print("Lo sentimos, necesitas más dinero")
            else:
                print(f"Su cambio es de ${dinero - precioInicial}")
    else:
        if 1 <= productoElegido <= len(productos):
            productoElegido = list(productos.keys())[productoElegido - 1]
            precioInicial = productos[productoElegido]
            print(f"EL producto que a es elegido: {productoElegido}")
            print(f"El precio original: ${precioInicial}")
            dinero = int(input("Ingrese la cantidad de dinero que va a pagar: $"))

            if dinero < precioInicial:
                print("Lo sentimos, no tienes suficiente dinero")
            else:
                print(f"Su cambio es de ${dinero - precioInicial}")
        else:
            print("Error reinicia el programa.")
else:
    print("Error reinicia el programa.")