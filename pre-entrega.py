# Lista principal
productos = []

# Texto del menú
menu = """                        

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        BIENVENIDO AL MENU PRINCIPAL.
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

Ingrese la operación que desea realizar:
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir 

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

opcion = int(input(menu))

# Menú principal
while opcion != 5:
    if opcion == 1: # Agregar producto
        nombre = input("Ingrese nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío")
        else:
            categoria = input("Ingrese categoría del producto: ").strip()
            if categoria == "":
                print("La categoría no puede estar vacía")
            else:
                precio = input("Ingrese precio del producto: ").strip()
                if precio != "":
                    precio = int(precio)   
                    if precio > 0:
                        productos.append([nombre, categoria, precio])
                        print("Producto agregado correctamente")
                    else:
                        print("El precio debe ser mayor a 0")
                else:
                    print("El precio no puede estar vacío")              
    elif opcion == 2: # Mostrar productos
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for i in range(len(productos)):
                print(f"{i+1}. Nombre: {productos[i][0]} - Categoría: {productos[i][1]} - Precio: {productos[i][2]}")
    elif opcion == 3: #Buscar productos
        buscar_prod = input("Ingrese el nombre del producto a buscar: ").strip()
        if buscar_prod == "":
            print("Ingresar un nombre válido")
        else:
            encontrado = False
            for prod in productos:
                if prod[0].lower() == buscar_prod.lower():
                    print(f"Nombre: {prod[0]} - Categoría: {prod[1]} - Precio: {prod[2]}")
                    encontrado = True
            if not encontrado:
                print("No se encontraron resultados")
    elif opcion == 4: #Eliminar el producto
        if len(productos) == 0:
           print("No hay productos registrados")
        else: 
            for i in range(len(productos)):
                print(f"{i+1}. Nombre: {productos[i][0]} - Categoría: {productos[i][1]} - Precio: {productos[i][2]}")
                
            posicion = input("Ingrese el número del producto a eliminar: ").strip()
            if posicion != "":
                posicion = int(posicion)
                if 0 < posicion <= len(productos):
                    eliminado = productos.pop(posicion - 1)
                    print(f"Producto eliminado: {eliminado[0]}")
                else:
                    print("Numero invalido")
            else:
                print("Debe ingresar un número")
    else:
        print("Ingrese una opción correcta")

    # Mostrar el menú
    opcion = int(input(menu))

print("¡Gracias por usar nuestro sistema!")
