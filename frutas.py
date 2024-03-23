
frutas = []
n = int(input("Ingrese la cantidad de frutas: "))
i = 0

while i < n:
    print(f"\nIngrese los datos de la fruta {i+1}:")
    id_fruta = input("ID de la fruta: ")
    nombre = input("Nombre de la fruta: ")
    precio_unitario = float(input("Precio unitario de la fruta: "))
    cantidad = int(input("Cantidad de la fruta: "))
    frutas.append({
        'id': id_fruta,
        'nombre': nombre,
        'precio_unitario': precio_unitario,
        'cantidad': cantidad
    })
    i += 1

opcion = 0
while opcion != '4':
    print("\nMenú de opciones:")
    print("1. Mostrar el costo total del salpicón")
    print("2. Mostrar todas las frutas ordenadas por costo  mayor a menor")
    print("3. Mostrar la fruta más barata")
    print("4. Salir")

    opcion = input(" Selecciona la opción: ")

    if opcion == '1':
        total = 0
        for fruta in frutas:
            total += fruta['precio_unitario'] * fruta['cantidad']
        print("\nCosto total del salpicón:", total)
    elif opcion == '2':
        for i in range(len(frutas)):
            for j in range(i + 1, len(frutas)):
                if frutas[i]['precio_unitario'] * frutas[i]['cantidad'] < frutas[j]['precio_unitario'] * frutas[j]['cantidad']:
                    frutas[i], frutas[j] = frutas[j], frutas[i]
        print("\nFrutas ordenadas por costo :")
        for fruta in frutas:
            print(fruta['nombre'], "-", fruta['precio_unitario'])
    elif opcion == '3':
        fruta_barata = frutas[0]
        for fruta in frutas:
            if fruta['precio_unitario'] < fruta_barata['precio_unitario']:
                fruta_barata = fruta
        print("\nFruta más barata:")
        print(fruta_barata['nombre'], "-", fruta_barata['precio_unitario'])
    elif opcion == '4':
        print("¡Gracias por la compra!")
    else:
        print("Error, ingrese un número del 1 al 4.")