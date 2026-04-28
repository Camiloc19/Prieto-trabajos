
print("Caso 2")

while True:

    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes (1-12): "))
    año = int(input("Ingrese el año: "))

    
    if mes == 1:
        nombre_mes = "Enero"
        dias_max = 31
    elif mes == 2:
        nombre_mes = "Febrero"
        dias_max = 28
    elif mes == 3:
        nombre_mes = "Marzo"
        dias_max = 31
    elif mes == 4:
        nombre_mes = "Abril"
        dias_max = 30
    elif mes == 5:
        nombre_mes = "Mayo"
        dias_max = 31
    elif mes == 6:
        nombre_mes = "Junio"
        dias_max = 30
    elif mes == 7:
        nombre_mes = "Julio"
        dias_max = 31
    elif mes == 8:
        nombre_mes = "Agosto"
        dias_max = 31
    elif mes == 9:
        nombre_mes = "Septiembre"
        dias_max = 30
    elif mes == 10:
        nombre_mes = "Octubre"
        dias_max = 31
    elif mes == 11:
        nombre_mes = "Noviembre"
        dias_max = 30
    elif mes == 12:
        nombre_mes = "Diciembre"
        dias_max = 31
    else:
        nombre_mes = "Invalido"
        dias_max = 0

    if mes < 1 or mes > 12 or dia < 1 or dia > dias_max:

        
        print("FECHA INCORRECTA.")
        print("")
        print("FAVOR VERIFICAR E INTENTAR DE NUEVO.")

    else:

       
        print("FECHA CORRECTA.")
        print("")

      
        nombre_evento = input("Ingrese el nombre del evento: ")

        hora_inicio = int(input("Ingrese hora de inicio: "))
        minutos_inicio = int(input("Ingrese minutos de inicio: "))

        hora_fin = int(input("Ingrese hora de fin: "))
        minutos_fin = int(input("Ingrese minutos de fin: "))

        if hora_inicio < 12 and hora_fin < 12:
            periodo = "AM."
        elif hora_inicio >= 12 and hora_fin >= 12:
            periodo = "PM."
        else:
            periodo = "AM/PM."

        print("FECHA:", str(dia) + " de " + nombre_mes + " del " + str(año))
        print("NOMBRE:", nombre_evento)
        print("HORARIO:", str(hora_inicio) + ":" + str(minutos_inicio) + " / " + str(hora_fin) + ":" + str(minutos_fin), periodo)

    continuar = input("Desea agregar otro evento? (si/no): ").lower()
    if continuar == "no":
        break