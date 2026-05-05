productores = int(input("Ingresa el número de productores:\n"))

mejor_prom = 0
mejor_producto = 0

for n in range(productores):
    print(f"\nProductor {n+1}")

    toneladas = []
    suma_toneladas = 0
    suma_hectareas = 0

    for a in range(3):
        print(f"Año {a+1}")
        
        hec = float(input("Cantidad de hectáreas: "))
        ton = float(input("Cantidad de toneladas: "))

        toneladas.append(ton)
        suma_toneladas += ton
        suma_hectareas += hec

    # ordenar después de llenar la lista
    toneladas.sort(reverse=True)

    print("Lista ordenada por toneladas:", toneladas)

    prom_toneladas = suma_toneladas / 3
    prom_hectareas = suma_hectareas / 3

    print("Promedio toneladas:", prom_toneladas)
    print("Promedio hectáreas:", prom_hectareas)

    if prom_toneladas > mejor_prom:
        mejor_prom = prom_toneladas
        mejor_producto = n + 1

# fuera del ciclo
print("\nEl productor con mejor promedio es:", mejor_producto)