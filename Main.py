import random

class Producto:
    def __init__(self, id, nombre, precio, ubicacion, descripcion, casa, referencia, pais_origen, unidades, garantia):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.casa = casa
        self.referencia = referencia
        self.pais_origen = pais_origen
        self.unidades = unidades
        self.garantia = garantia

productos = []

opcion = 0
while opcion != 6:
    print("\n--- Menú de opciones ---")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar información de un producto por nombre")
    print("4. Modificar producto")
    print("5. Eliminar producto del inventario")
    print("6. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        id = random.randint(1, 100)
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio unitario del producto: "))
        ubicacion = input("Ubicación en la tienda (A, B, C, D): ").upper()
        descripcion = input("Descripción del producto: ")
        casa = input("Casa a la que pertenece el producto (Marvel, DC, etc): ")
        referencia = input("Referencia (código alfanumérico): ")
        pais_origen = input("País de origen del producto: ")
        unidades = int(input("Número de unidades compradas del producto: "))
        garantia = input("Producto con garantía extendida (true/false): ").lower() == "true"

        if unidades > 50:
            print("¡Error! La cantidad máxima de unidades por producto es 50. Se ajustará a 50.")
            unidades = 50

        producto = Producto(id, nombre, precio, ubicacion, descripcion, casa, referencia, pais_origen, unidades, garantia)
        productos.append(producto)
        print("Producto registrado exitosamente.")

    elif opcion == 2:
        if not productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario de la tienda ---")
            for producto in productos:
                total = sum(p.unidades for p in productos if p.nombre == producto.nombre)
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Ubicación: {producto.ubicacion}, Descripción: {producto.descripcion}, Cantidad total: {total}")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto que desea buscar: ")
        encontrado = False
        for producto in productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"Información del producto:")
                print(f"ID: {producto.id}")
                print(f"Nombre: {producto.nombre}")
                print(f"Precio: {producto.precio}")
                print(f"Ubicación: {producto.ubicacion}")
                print(f"Descripción: {producto.descripcion}")
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == 4:
        nombre = input("Ingrese el nombre del producto que desea modificar: ")
        encontrado = False
        for producto in productos:
            if producto.nombre.lower() == nombre.lower():
                print("Ingrese los nuevos datos para el producto:")
                producto.precio = float(input("Precio unitario del producto: "))
                producto.ubicacion = input("Ubicación en la tienda (A, B, C, D): ").upper()
                producto.descripcion = input("Descripción del producto: ")
                producto.casa = input("Casa a la que pertenece el producto (Marvel, DC, etc): ")
                producto.referencia = input("Referencia (código alfanumérico): ")
                producto.pais_origen = input("País de origen del producto: ")
                producto.unidades = int(input("Número de unidades compradas del producto: "))
                producto.garantia = input("Producto con garantía extendida (true/false): ").lower() == "true"
                print("Producto modificado exitosamente.")
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == 5:
        nombre = input("Ingrese el nombre del producto que desea eliminar: ")
        for producto in productos:
            if producto.nombre.lower() == nombre.lower():
                confirmacion = input(f"¿Estás seguro que deseas eliminar '{producto.nombre}' del inventario? (s/n): ").lower()
                if confirmacion == "s":
                    productos.remove(producto)
                    print("Producto eliminado del inventario.")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("Producto no encontrado.")

    elif opcion == 6:
        print("Gracias por utilizar el sistema de gestión de inventario de la tienda de cómics. ¡Hasta luego!")

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
