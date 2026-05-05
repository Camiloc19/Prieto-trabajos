# estado de la máquina
maquina_habilitada = True

# productos: codigo -> (nombre, precio)
productos = {
    21: ("Papas limón", 2500),
    26: ("Plátanitos Maduros", 2600),
    32: ("Ponqué Gala", 1900),
    36: ("Maní Salado", 2100),
    38: ("CocaCola Lata", 4500),
    41: ("Seven Up Lata", 3900)
}

# inventario inicial
inventario = {codigo: 5 for codigo in productos}

while True:
    print("\n**** MENU DE OPCIONES ****")
    print("1. Distribuidor")
    print("2. Cliente")
    print("3. Salir")

    opcion = input("Seleccione con que usuario desea ingresar: ")

    # ================= DISTRIBUIDOR =================
    if opcion == "1":
        # contraseña
        while True:
            clave = input("Ingrese la clave: ")
            if clave == "1001":
                print("Clave Correcta")
                break
            else:
                print("ingresa una contraseña validad.")

        # menú distribuidor
        while True:
            print("\n** Ingreso como Distribuidor **")
            print("1. Habilitar/Deshabilitar Máquina")
            print("2. Agregar Productos")
            print("3. Inventario")
            print("4. Salir")

            op = input("Seleccione lo que desea realizar: ")

            if op == "1":
                maquina_habilitada = not maquina_habilitada
                print("Máquina habilitada" if maquina_habilitada else "Máquina deshabilitada")

            elif op == "2":
                while True:
                    codigo = int(input("Ingrese código (0 para salir): "))
                    if codigo == 0:
                        break

                    if codigo in inventario:
                        cantidad = int(input("Cantidad a agregar: "))
                        inventario[codigo] += cantidad
                        print("Producto agregado")
                    else:
                        print("Código inválido")

            elif op == "3":
                print("\nInventario:")
                for cod, cant in inventario.items():
                    print(f"{cod} - {productos[cod][0]}: {cant}")

            elif op == "4":
                break

            else:
                print("Opción inválida")

    # ================= CLIENTE =================
    elif opcion == "2":

        if not maquina_habilitada:
            print("La máquina está deshabilitada")
            continue

        print("\nProductos disponibles:")
        for cod, (nombre, precio) in productos.items():
            print(f"{cod} - {nombre} - ${precio}")

        codigo = int(input("Ingrese código del producto: "))

        if codigo not in productos:
            print("Código inválido")
            continue

        if inventario[codigo] <= 0:
            print("Producto agotado")
            continue

        nombre, precio = productos[codigo]
        dinero = int(input("Ingrese dinero: "))

        if dinero > 10000 or dinero < precio:
            print(f"El precio de {nombre} es: ${precio}")
            print("Dinero insuficiente o excedido.")
            continue

        cambio = dinero - precio
        print(f"El precio de {nombre} es: ${precio}")

        # 💰 calcular cambio
        billetes_5000 = cambio // 5000
        cambio %= 5000

        billetes_2000 = cambio // 2000
        cambio %= 2000

        billetes_1000 = cambio // 1000
        cambio %= 1000

        monedas_200 = cambio // 200
        cambio %= 200

        monedas_100 = cambio // 100

        if billetes_5000 > 0:
            print(f"{billetes_5000} Billetes de Cinco mil")
        if billetes_2000 > 0:
            print(f"{billetes_2000} Billetes de Dos mil")
        if billetes_1000 > 0:
            print(f"{billetes_1000} Billetes de Mil")
        if monedas_200 > 0:
            print(f"{monedas_200} Monedas de Doscientos")
        if monedas_100 > 0:
            print(f"{monedas_100} Monedas de Cien")

        inventario[codigo] -= 1

        print("Gracias por su compra")

    # ================= SALIR =================
    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")