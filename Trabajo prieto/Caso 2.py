print("Caso 2")

# VALIDAR MES
while True:
    mes = int(input("Ingrese el mes (1-12): "))
    if 1 <= mes <= 12:
        break
    else:
        print("FECHA INCORRECTA.")

# ASIGNAR NOMBRE Y DÍAS
if mes == 1:
    nombre_mes = "Enero"; dias_max = 31
elif mes == 2:
    nombre_mes = "Febrero"; dias_max = 28
elif mes == 3:
    nombre_mes = "Marzo"; dias_max = 31
elif mes == 4:
    nombre_mes = "Abril"; dias_max = 30
elif mes == 5:
    nombre_mes = "Mayo"; dias_max = 31
elif mes == 6:
    nombre_mes = "Junio"; dias_max = 30
elif mes == 7:
    nombre_mes = "Julio"; dias_max = 31
elif mes == 8:
    nombre_mes = "Agosto"; dias_max = 31
elif mes == 9:
    nombre_mes = "Septiembre"; dias_max = 30
elif mes == 10:
    nombre_mes = "Octubre"; dias_max = 31
elif mes == 11:
    nombre_mes = "Noviembre"; dias_max = 30
elif mes == 12:
    nombre_mes = "Diciembre"; dias_max = 31

# VALIDAR DÍA
while True:
    dia = int(input("Ingrese el día: "))
    if 1 <= dia <= dias_max:
        break
    else:
        print("FECHA INCORRECTA.")

# VALIDAR AÑO
while True:
    año = int(input("Ingrese el año: "))
    if año > 0:
        break
    else:
        print("Error de dato, intente de nuevo")

# EVENTO
nombre_evento = input("Ingrese el nombre del evento: ")

# VALIDAR HORAS
while True:
    hora_inicio = int(input("Ingrese hora de inicio (0-23): "))
    minutos_inicio = int(input("Ingrese minutos de inicio (0-59): "))
    if 0 <= hora_inicio <= 23 and 0 <= minutos_inicio <= 59:
        break
    else:
        print("Hora inválida.")

while True:
    hora_fin = int(input("Ingrese hora de fin (0-23): "))
    minutos_fin = int(input("Ingrese minutos de fin (0-59): "))
    if 0 <= hora_fin <= 23 and 0 <= minutos_fin <= 59:
        break
    else:
        print("Hora inválida.")

# PERIODO
if hora_inicio < 12 and hora_fin < 12:
    periodo = "AM"
elif hora_inicio >= 12 and hora_fin >= 12:
    periodo = "PM"
else:
    periodo = "AM/PM"

# SALIDA
print("\n--- DATOS DEL EVENTO ---")
print(f"FECHA: {dia} de {nombre_mes} del {año}")
print(f"NOMBRE: {nombre_evento}")
print(f"HORARIO: {hora_inicio}:{minutos_inicio} / {hora_fin}:{minutos_fin} {periodo}")