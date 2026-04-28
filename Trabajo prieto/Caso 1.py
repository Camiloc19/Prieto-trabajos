print("Caso numero 1")

apellido_nombre = input("Ingrese Nombre y apellido: ")
categoria = input("Ingrese Categoria (Junior / Semi Senior / Senior): ").title()
antiguedad = int(input("Ingrese Antiguedad en años: "))

sueldo_basico=0

if categoria == "Junior":
    sueldo_basico = 1500
elif categoria == "Semi Senior":
    sueldo_basico = 2000
elif categoria == "Senior":
    sueldo_basico = 2500


if antiguedad >= 1 and antiguedad <= 5:
    porcentaje = 2
elif antiguedad >= 6 and antiguedad <= 10:
    porcentaje = 5
elif antiguedad >= 11 and antiguedad <= 20:
    porcentaje = 8
elif antiguedad > 20:
    porcentaje = 10


monto_antiguedad = sueldo_basico * porcentaje / 100
sueldo_total = sueldo_basico + monto_antiguedad


print("")
print("APELLIDO Y NOMBRE:", apellido_nombre)
print("CATEGORIA:", categoria)
print("ANTIGUEDAD:", antiguedad, "ANOS")
print("SUELDO BASICO: $", sueldo_basico)
print("MONTO ANTIGUEDAD: $", monto_antiguedad)
print("SUELDO TOTAL: $", sueldo_total)
print("")
print("OBSERVACIONES:")

if monto_antiguedad > sueldo_basico:
    print("EL EMPLEADO GANA MAS POR ANTIGUEDAD QUE POR BASICO")
else:
    print("EL EMPLEADO GANA MAS POR BASICO QUE POR ANTIGUEDAD")

print("EL PORCENTAJE DE AUMENTO ES:", porcentaje, "%")